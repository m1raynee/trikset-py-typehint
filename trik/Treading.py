from typing import Callable


def joinThread(treadId: str) -> None:
    """Ожидает завершения указанного потока.

    Параметры
    ---------
    treadId: :class:`str`
        id потока
    """
    raise NotImplementedError


def killThread(treadId: str) -> None:
    """Заканчивает исполнение указанного потока.

    Параметры
    ---------
    treadId: :class:`str`
        id потока
    """
    raise NotImplementedError


def receiveMessage(wait: bool) -> str:
    """Запрашивает принятое сообщение.

    Параметры
    ---------
    wait: :class:`bool`
        Если `True`, то ожидает, пока не придет сообщение.
    """
    raise NotImplementedError


def sendMessage(treadId: str, message: str) -> None:
    """Посылает сообщение указанному потоку.

    Параметры
    ---------
    treadId: :class:`str`
        id потока
    message: :class:`str`
        Сообщение
    """
    raise NotImplementedError


def startThread(newThreadId: str, functionName: Callable):
    """Запускает переданную в качестве параметра функцию в отдельном потоке.
    Параметры
    ---------
    newTreadId: :class:`str`
        id нового потока
    functionName: Callable
        Функция
    """
