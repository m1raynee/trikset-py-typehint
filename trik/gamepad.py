"""Служит для работы с программируемым пультом управления «TRIK Gamepad»."""

from typing import Callable, Any, Literal, Optional


class button:
    """Посылается, когда пользователь нажал на одну из пяти кнопок внизу пульта."""

    @classmethod
    def connect(cls, func: Callable[[int, str], Any]) -> None:  # TODO: ensure types
        raise NotImplementedError


_BUTTON_NUMBER = Literal[1, 2, 3, 4, 5]
_PAD_ID = Literal[0, 1]


def buttonWasPressed(buttonNumber: _BUTTON_NUMBER) -> bool:
    """Возвращает `True`, если на пульте была нажата кнопка с указанным номером.
    Сбрасывает запомненное нажатие для этой кнопки.
    """
    raise NotImplementedError


def isPadPressed(padId: _PAD_ID) -> bool:
    """Возвращает, нажата ли в данный момент область управления на пульте.
    Области управления имеют номера 0 и 1.
    """
    raise NotImplementedError


class pad:
    """Посылается, когда пользователь нажал на область управления на пульте или переместил палец по ней."""

    @classmethod
    def connect(cls, func: Callable[[int, str], Any]) -> None:
        raise NotImplementedError


def padX(padId: _PAD_ID) -> Optional[int]:
    """Если указанная область управления на пульте нажата, возвращает текущую x-координату нажатия."""
    raise NotImplementedError


def padY(padId: _PAD_ID) -> Optional[int]:
    """Если указанная область управления на пульте нажата, возвращает текущую y-координату нажатия."""
    raise NotImplementedError


class padUp:
    """Посылается, когда пользователь оторвал палец от области управления с указанным номером."""

    @classmethod
    def connect(cls, func: Callable[[_PAD_ID, int, int], Any]) -> None:
        """
        Параметры
        ---------
        padId: `Literal[0, 1]`
            Номер области управления
        x, y: :class:`int`
            Координаты последнего известного нажатия от -100 до 100.
            Координата (-100, -100) соответствует левому верхнему углу области управления.
        """
        raise NotImplementedError


def reset() -> None:
    """Сбрасывает запомненные события от пульта."""
    raise NotImplementedError


def wheel() -> int:
    """Если на пульте включён «руль» (события от акселерометра устройства), возвращает текущий наклон пульта.
    Наклон кодируется числом от -100 до 100, -100 соответствует крайнему левому положению «руля», 100 — крайнему правому.
    """
    raise NotImplementedError


class wheelEvent:
    """Посылается, когда на пульте включён «руль» (события от акселерометра устройства) и пользователь повернул устройство."""

    @classmethod
    def connect(cls, func: Callable[[int], Any]) -> None:
        """
        Параметры
        ---------
        percent: :class:`int`
            Число от -100 до 100, -100 соответствует крайнему левому положению «руля», 100 — крайнему правому.
        """
