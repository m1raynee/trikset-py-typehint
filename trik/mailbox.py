"""Реализует связь между роботами в сети посредством механизма почтовых ящиков."""

from typing import Any, Callable, Optional, Union


def connect(ipAddress: str, port: Optional[int] = None) -> None:
    """Подключается к роботу с заданным IP-адресом по заданному порту
    (или порту по умолчанию), сообщает ему свой бортовой номер и регистрируется
    в сети «почтовых ящиков».

    Параметры
    ---------
    ipAdress: :class:`str`
        IP-адрес робота
    port: Optional[:class:`int`]
        Порт подключения. Если не указан, используется порт по умолчанию.
    """
    raise NotImplementedError


def hasMessages() -> bool:
    """Возвращает `True`, если роботу пришло новое сообщение."""


def myHullNumber() -> int:
    """Возвращает бортовой номер робота."""


class newMessage:
    @classmethod
    def connect(cls, func: Callable[[int, str], Any]) -> None:
        raise NotImplementedError


def receive() -> str:
    """Получает новое сообщение или блокирует исполнение скрипта до тех пор, пока сообщение не придёт."""
    raise NotImplementedError


def send(boardNumber: Union[str, int], message: Optional[str] = None) -> None:
    """Посылает роботу с указанным бортовым номером (или всем роботам) указанное сообщение."""
    raise NotImplementedError
