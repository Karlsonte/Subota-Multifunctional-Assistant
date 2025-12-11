# core/discovery_manager.py

import asyncio
import inspect
from inspect import iscoroutine
from typing import TYPE_CHECKING
import aiohttp
from async_upnp_client.search import async_search
from async_upnp_client.ssdp_listener import SsdpListener
from core.logger_manager import get_logger
from modules.network_utils import get_interface_ip
import xml.etree.ElementTree as ET
from zeroconf import ServiceBrowser, Zeroconf, ServiceListener

if TYPE_CHECKING:
    from core.core_init import Core

import logging
logging.getLogger('zeroconf').setLevel(logging.DEBUG)

logger = get_logger(__name__)

DEVICE_EVENT_TYPE = 'device_discovered'

MDNS_SERVICES = [
    "_services._dns-sd._udp.local.",
    "_http._tcp.local.",
    "_ipp._tcp.local.",
    "_ssh._tcp.local.",
    "_workstation._tcp.local." 
]
# other code

async def _listener_loop(self):
        """Пассивно слушает широковещательные объявления (SSDP NOTIFY)."""
        try:
            # SsdpListener автоматически привязывается к указанному IP
            listener = SsdpListener(
                async_callback=self._handle_device_event,
                source=(self.ip_address, 0) # Bind to specific IP, port 0 to let OS choose
            )

            if asyncio.iscoroutine(listener):
                listener = await listener

            await listener.async_start()
            
            # Keep the listener task alive indefinitely
            await asyncio.Future() 
                
        except asyncio.CancelledError:
            logger.info("[DiscoveryManager] Listener отменен.")
            raise
        except Exception as e:
            logger.error(f"[DiscoveryManager] Ошибка в listener loop: {e}")
            await asyncio.sleep(5)
# other code

async def _handle_discovered_device(self, event_type: str, payload: dict = None):
        """Обрабатывает событие обнаружения устройства."""
        if event_type != DEVICE_EVENT_TYPE:
            return

        protocol = payload.get('protocol', 'ssdp')
        usn = payload.get('usn', 'N/A')
        
        # СЦЕНАРИЙ 1: mDNS (информация уже есть в payload)
        if protocol == 'mdns':
            logger.info(f"[DiscoveryManager]: mDNS устройство {payload['friendly_name']} обработано.")
            # Используем данные, уже извлеченные в MDNSDiscoveryListener
            device_to_save = {
                'usn': usn,
                'st': payload['type'],
                'location': payload['location'], # Это будет адрес:порт
                'ip_address': payload['ip_address'],
                'friendly_name': payload['friendly_name'],
                'model_name': 'mDNS Service',
                'manufacturer': 'Unknown'
            }
            await self._save_device_to_db(device_to_save)
            return

        location = payload['location']
        
        logger.info(f"[DiscoveryManager]: Обработка нового устройства по URL: {location}")
        
        try:
            # 1. Получаем контекстный менеджер
            resp_ctx = self._session.get(location)

            # FIX: если мок возвращает корутину, дожидаемся
            if inspect.iscoroutine(resp_ctx):
                resp_ctx = await resp_ctx

            # 2. Входим в async with
            async with resp_ctx as response:
                response.raise_for_status()
                description_xml = await response.text()

            # 3. Извлечение IP-адреса
            import urllib.parse
            parsed_url = urllib.parse.urlparse(location)
            ip_address = parsed_url.hostname

            # 4. Парсим XML
            root = ET.fromstring(description_xml)
            NS = {'upnp': 'urn:schemas-upnp-org:device-1-0'}
            device_tag = root.find('upnp:device', NS)

            def safe_get_text(parent, tag_name):
                tag = parent.find(f'upnp:{tag_name}', NS)
                return tag.text if tag is not None else None

            friendly_name = safe_get_text(device_tag, 'friendlyName')
            model_name = safe_get_text(device_tag, 'modelName')
            manufacturer = safe_get_text(device_tag, 'manufacturer')

            # 5. Save device
            device_to_save = {
                'usn': usn,
                'st': payload['type'],
                'location': location,
                'ip_address': ip_address,
                'friendly_name': friendly_name,
                'model_name': model_name,
                'manufacturer': manufacturer
            }
            await self._save_device_to_db(device_to_save)

        except aiohttp.ClientError as e:
            logger.error(f"[DiscoveryManager]: Не удалось загрузить XML-описание с {location}: {e}")
        except Exception as e:
            logger.error(f"[DiscoveryManager]: Ошибка при парсинге или сохранении устройства {location}: {e}")
