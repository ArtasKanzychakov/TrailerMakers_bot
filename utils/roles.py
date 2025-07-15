ADMIN_IDS = [123456789]  # Замените на реальные ID

def is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS
