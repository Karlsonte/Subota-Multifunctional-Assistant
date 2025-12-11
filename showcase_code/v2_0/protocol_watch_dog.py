import traceback
import time
import os
import cv2
from dotenv import load_dotenv
from Main.core.plugin import Plugin
from Main.visual_ai.cameras.cam_motion import MotionDetectionCam
from Main.visual_ai.camera_control_center import CameraControlCenter
from Main.core.event_hendler import EventHandler
from Main.bots.notification_service import AlertHandler
from Main.bots.email.email_service import GmailService
from Main.modules.my_loging import log_data
from Main.bots.telegramm import run_bot_sync
from Main.core.thread_manager import thread_manager

class WatchDogPlugin(Plugin):

    def __init__(self):
        super().__init__()
        self.event_handler = EventHandler()
        self.center = CameraControlCenter()
        self.event_counters = {}
        self.last_sent = {}

        self.center._register_camera_class("motion", MotionDetectionCam)
        self.center._register_callback(self.alert_callback)
        self.center._register_callback(self.camera_callback)


    @property
    def keywords(self):
        return ["охран", "движен", "слеж", "патруль", "пёс", "собака", "сторож"]

    def camera_callback(self, camera_id, event_type, objects, frame):
        metadata = {
            'camera_id': camera_id,
            'event_type': event_type,
            'objects': objects,
            'timestamp': time.time()
        }
        self.event_handler.handle_event(
            event_source="camera",
            event_type=event_type,
            event_data=frame,
            metadata=metadata
        )

    def alert_callback(self, camera_id, event_type, objects, frame):
        timestamp = time.time()
        self.event_counters[camera_id] = self.event_counters.get(camera_id, 0) + 1
        counter = self.event_counters[camera_id]
        last = self.last_sent.get(camera_id, 0)

        if counter % 20 == 0 and (timestamp - last) > 30:
            try:
                print(f"[{time.strftime('%H:%M:%S')}] Камера {camera_id}: {event_type} - {objects}")
                self.last_sent[camera_id] = timestamp

                # Получаем камеру по id
                cam = self.center.cameras.get(camera_id)
                photo_path = None

                if event_type == "motion" and "person" in objects:
                    if hasattr(cam, 'save_photo_path') and hasattr(cam, 'save_photo'):
                        try:
                            photo_path = cam.save_photo(
                                frame=frame,
                                reason=f"event_{event_type}",
                                photo_path=cam.save_photo_path
                            )
                            print(f"Сохранено фото: {photo_path}")
                        except Exception as e:
                            print(f"Ошибка сохранения фото: {e}")

                metadata = {
                    'camera_id': camera_id,
                    'event_type': event_type,
                    'objects': objects,
                    'timestamp': timestamp,
                    'event_counter': counter,
                    'photo_path': photo_path
                }

                self.event_handler.handle_event(
                    event_source="alert_motion",
                    event_type=event_type,
                    event_data=photo_path if photo_path else frame,
                    metadata=metadata
                )
            except Exception as e:
                print(f"Ошибка при отправке уведомления: {e}")

    def handle_motion_event(self, event_data, metadata):
        camera_id = metadata['camera_id']
        event_type = metadata['event_type']
        objects = metadata['objects']
        frame = event_data

    def execute(self, command: str) -> tuple:
        try:
            load_dotenv()
            TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
            FIRST_ID = os.getenv('TG_ID_FIRST')

            if not TG_BOT_TOKEN or not FIRST_ID:
                raise ValueError("Не заданы необходимые переменные окружения")

            email_service = GmailService()
            alert_handler = AlertHandler(bot_token=TG_BOT_TOKEN, first_id=FIRST_ID, email_sender=email_service)

            alert_handler.center = self.center

            self.event_handler.register_handler("camera", "motion", self.handle_motion_event)
            self.event_handler.register_handler("alert_motion", "motion", alert_handler.create_handler())
            thread_manager.run_once("telegram_bot", lambda: run_bot_sync(TG_BOT_TOKEN))

            self.center.add_camera("motion", "cam1", camera_index=2)

            log_data("Протокол слежения за движением активирован", "System")

            return True, "Сторожевой протокол активирован. Начинаю наблюдение."

        except Exception as e:
            error_message = f"ERROR in {self.__class__.__name__}: {str(e)}\n{traceback.format_exc()}"
            log_data(error_message, 'Errors')
            return True, "Произошла ошибка при запуске протокола сторожа."
        
    def stop(self):
        print("Остановка камеры cam1...")
        self.center.stop_camera("cam1")
        print("Остановка завершена.")
