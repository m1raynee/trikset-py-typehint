"""Представляет методы управления выполнением скрипта и доступ к функциям операционной системы."""
from typing import Any, Callable, List


def quit() -> None:
    """Устанавливает флаг окончания работы для событийно-ориентированной программы.
    Как только будет завершён текущий обработчик события, исполнение скрипта закончится.
    """
    raise NotImplementedError


def random(min: int, max: int) -> int:
    """Возвращает случайное число из заданного диапазона.

    Параметры
    ---------
    min: :class:`int`
        Минимальное значение
    max: :class:`int`
        Максимальное значение
    """
    raise NotImplementedError


def readAll(fileName: str) -> List[str]:
    """Считывает всё содержимое указанного файла в массив строк.

    Параметры
    ---------
    fileName: :class:`str`
        Название файла с расширением
    """
    raise NotImplementedError


def removeFile(fileName: str) -> None:
    """Удаляет указанный файл.

    Параметры
    ---------
    fileName: :class:`str`
        Название файла с расширением
    """
    raise NotImplementedError


def system(command: str) -> None:
    """Выполняет переданную команду.

    Параметры
    ---------
    command: :class:`str`
        Команда консоли операционной системы"""


def time() -> int:
    """Возвращает временной штамп — количество миллисекунд,
    прошедших с начала 1 января 1970 года по Гринвичу.
    """
    raise NotImplementedError


class _timeoutconnector:
    @classmethod
    def connect(self, func: Callable[[], Any]) -> None:
        raise NotImplementedError


class _qtimer:
    @property
    def timeout(self) -> _timeoutconnector:
        raise NotImplementedError


def timer(n: int) -> _qtimer:
    """Создаёт и возвращает таймер (класс `«QTimer»`), посылающий сигнал `timeout` каждые `n` миллисекунд.

    Параметры
    ---------
    n: :class:`int`
        Время в миллисекундах
    """
    raise NotImplementedError


def wait(msCount: int):
    """Приостанавливает выполнение скрипта на переданное количество миллисекунд.

    Параметры
    ---------
    msCount: :class:`int`
        Время в миллисекундах
    """
    raise NotImplementedError


def writeToFile(fileName: str, text: str) -> None:
    """Записывает сроку в файл.

    Параметры
    ---------
    fileName: :class:`str`
        Название файла с расширением
    text: :class:`str`
        Записываемая строка
    """
    raise NotImplementedError
