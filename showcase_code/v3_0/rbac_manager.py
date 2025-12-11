# core/rbac_manager.py

from typing import TYPE_CHECKING

from .logger_manager import get_logger

logger = get_logger(__name__)

if TYPE_CHECKING:
    from core.core_init import Core

class RBACManager:
    """
    Менеджер для проверки прав доступа на основе ролей (Role-Based Access Control).
    """
    def __init__(self, core_instance: "Core"):
        self.core = core_instance
        self.db_manager = core_instance.postgres_manager

    async def get_user_role(self, user_id: int) -> str:
        """Получает имя роли пользователя по его ID."""
        if not isinstance(user_id, int):
            logger.error("user_id must be an integer.")
            return 'guest'

        query = "SELECT r.name FROM users u JOIN roles r ON u.role_id = r.id WHERE u.id = $1;"
        result = await self.db_manager.fetchrow(query, user_id)

        if result:
            return result['name']
        
        logger.warning(f"Пользователь с ID {user_id} не найден. Используется роль по умолчанию: 'guest'.")
        return 'guest'
    
    async def check_permission(self, role_name: str, permission_name: str) -> bool:
        """
        Проверяет, имеет ли указанная роль требуемое разрешение.
        Возвращает True, если разрешение есть, иначе False.
        """
        if not isinstance(role_name, str) or not isinstance(permission_name, str):
            logger.error("role_name and permission_name must be strings.")
            return False
        role_name = role_name.lower()
        permission_name = permission_name.lower()
        if role_name == 'admin':
            return True
        
        query = """
            SELECT EXISTS (
                SELECT 1 
                FROM roles r
                JOIN role_permissions rp ON r.id = rp.role_id
                JOIN permissions p ON rp.permission_id = p.id
                WHERE r.name = $1 AND p.name = $2
            );
        """

        result = await self.db_manager.fetchrow(query, role_name.lower(), permission_name.lower())

        return result['exists'] if result else False
    
    async def get_user_role_by_identifier(self, identifier: str) -> str:
        """Получает имя роли пользователя по его строковому Telegram ID."""
        if not isinstance(identifier, str):
            logger.error(f"[RBACManager] Identifier должен быть строкой, получено: {type(identifier)}.")
            return 'guest'

        try:
            telegram_user_id = int(identifier)
        except ValueError:
            logger.error(f"[RBACManager] Некорректный формат Telegram ID: '{identifier}'. Ожидается числовое значение.")
            return 'guest'

        query = "SELECT r.name FROM users u JOIN roles r ON u.role_id = r.id WHERE u.telegram_id = $1;"
        result = await self.db_manager.fetchrow(query, telegram_user_id)
        
        if result:
            return result['name']
        
        await self.core.notification_manager.publish_notification(text=f"[RBAC] Пользователь Telegram с ID '{identifier}' не найден. Используется роль по умолчанию: 'guest'.", 
                                                            ugrgency='warning', 
                                                            destinations=['web_ui']
                                                            )
        logger.warning(f"[RBACManager] Пользователь Telegram с ID '{identifier}' не найден. Используется роль по умолчанию: 'guest'.")
        return 'guest'
