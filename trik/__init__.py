from typing import List
from . import brick, gamepad, mailbox, script, Treading


__all__ = ("brick", "gamepad", "mailbox", "script", "Treading", "getPhoto")


def getPhoto() -> List[int]:
    """Функция возвращает одномерный массив байт, в который записаны пиксели изображения
    в формате rgb32, снятого с камеры (размер изображения — 160x120).
    Данная функция может быть использована для решения задач распознавания маркеров.
    """
    raise NotImplementedError


# include is js thing so is skipped
