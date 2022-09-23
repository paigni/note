def check_correct_inp(inp: int) -> bool:
    """
    Функция проверяет введённый аргумент в заданном диапазоне
    Args:
        inp: Аргумент пользователя
    Returns:
        Статус проверки
    """
    if inp >= 1:
        return True
    return False


def check_list(note_list):
    if not note_list:
        return True
    return False


