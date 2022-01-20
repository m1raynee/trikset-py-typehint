"""Объект «brick» представляет контроллер ТРИК и предоставляет доступ к устройствам робота."""

from enum import Enum
from typing import Any, Callable, List, Literal

# cspell: disable

_COLOR = Literal[
    "white",
    "red",
    "darkRed",
    "green",
    "darkGreen",
    "blue",
    "darkBlue",
    "cyan",
    "darkCyan",
    "magenta",
    "darkMagenta",
    "yellow",
    "darkYellow",
    "gray",
    "darkGray",
    "lightGray",
    "black",
]
_MOTOR_NAME = Literal["M1", "M2", "M3", "M4", "S1", "S2", "S3", "S4", "S5", "S6"]
_SENSOR_NAME = Literal["A1", "A2", "A3", "A4", "A5", "A6", "D1", "D2"]


class KeysEnum(Enum):
    Left = 105
    Up = 103
    Down = 108
    Enter = 28
    Right = 106
    Power = 116
    Esc = 1


class accelerometer:
    """Представляет акселерометр контроллера ТРИК."""

    def __init__(self) -> None:
        raise NotImplementedError

    def read(self) -> List[int]:
        """Возвращает текущее показание сенсора в виде массива
        из трёх элементов, соответствующих показаниям сенсора
        по каждой из осей.
        """
        raise NotImplementedError

    class newData:
        @classmethod
        def connect(cls, func: Callable) -> None:
            raise NotImplementedError


class battery:
    """Предоставляет доступ к информации о батарее или блоке питания."""

    def __init__(self) -> None:
        raise NotImplementedError

    def readVoltage(self) -> int:
        """Возвращает текущий вольтаж батареи (или блока питания) в вольтах."""
        raise NotImplementedError


class colorSensor:
    "Видеокамера в режиме датчика цвета."

    def __init__(self, port: str) -> None:
        raise NotImplementedError

    def init(self, show_to_screen: bool) -> None:
        "Включает видеокамеру и инициализирует её в режиме датчика цвета."
        raise NotImplementedError

    def read(self, x: int, y: int) -> List[int]:
        """Возвращает массив с координатами доминирующего цвета
        в цветовой шкале RGB в указанном участке кадра.

        Кадр делится на квадраты сеткой, по умолчанию 3 на 3, размерность сетки
        можно задать в `model-config.xml` на роботе. Квадраты индексируются с 1.
        То есть (1, 1) — это левый верхний край кадра, (2, 2) — его центр.
        Возвращаемое значение — массив из трёх элементов от 0 до 255, индексирующийся с 0.
        Нулевой элемент содержит интенсивность красного (0 — совсем нет, 255 — очень много),
        первый — интенсивность зелёного, второй — интенсивность синего.
        Например, (0, 0, 0) — чёрный, (255, 255, 255) — белый, (255, 0, 0) — красный.

        Параметры
        ---------
        x: :class:`int`
            Координата участке кадра по оси Ох
        y: :class:`int`
            Координата участке кадра по оси Оy
        """
        raise NotImplementedError

    def stop(self) -> None:
        """Выключает видеокамеру и прекращает работу датчика."""
        raise NotImplementedError


class display:
    """Предоставляет доступ к дисплею робота.

    Размер экрана: 240*320 пикселей."""

    _ARRAY_FORMAT = Literal["rgb32", "grayscale8" "rgb888"]

    def __init__(self) -> None:
        raise NotImplementedError

    def addLabel(self, text: str, x: int, y: int):
        """Вывести на экран указанный текст в указанные координаты.
        Если в указанных координатах уже был текст, он будет заменён новым.

        Изменения на дисплее произойдут только после вызова метода «redraw».

        Параметры
        ---------
        text: :class:`str`
            Выводимый текст
        x: :class:`int`
            Координата экрана по оси Ох
        y: :class:`int`
            Координата экрана по оси Оy
        """
        raise NotImplementedError

    def clear(self) -> None:
        """Очистить окно для рисования."""
        raise NotImplementedError

    def drawArc(self, x: int, y: int, l: int, h: int, _from: int, to: int) -> None:
        """Нарисовать дугу эллипса, вписанного в прямоугольник с левым верхним углом в указанных
        координатах и имеющий заданную ширину и высоту.

        Изменения на дисплее произойдут только после вызова метода «redraw».

        Параметры
        ---------
        x: :class:`int`
            Координата левого верхнего угла по оси Ох
        y: :class:`int`
            Координата левого верхнего угла по оси Оy
        l: :class:`int`
            Ширина прямоугольника
        h: :class:`int`
            Высота прямоугольника
        from: :class:`int`
            Начальный угол, ограничивающий дугу
        to: :class:`int`
            Конечный угол, ограничивающий дугу
        """
        raise NotImplementedError

    def drawEllipse(self, x: int, y: int, l: int, h: int, filled: bool = False) -> None:
        """Нарисовать эллипс, вписанный в прямоугольник с левым верхним углом в указанных
        координатах и имеющий заданную ширину и высоту.

        Изменения на дисплее произойдут только после вызова метода «redraw».

        Параметры
        ---------
        x: :class:`int`
            Координата левого верхнего угла по оси Ох
        y: :class:`int`
            Координата левого верхнего угла по оси Оy
        l: :class:`int`
            Ширина прямоугольника
        h: :class:`int`
            Высота прямоугольника
        filled: :class:`bool`
            Заливать фигуру или нет, по умолчанию False
        """
        raise NotImplementedError

    def drawLine(self, x0: int, y0: int, x1: int, y1: int) -> None:
        """Нарисовать линию с началом и концом в заданных координатах.

        Изменения на дисплее произойдут только после вызова метода «redraw».

        Параметры
        ---------
        x0: :class:`int`
            Координата начала линии по оси Ох
        y0: :class:`int`
            Координата начала линии по оси Оy
        x1: :class:`int`
            Координата конца линии угла по оси Ох
        y1: :class:`int`
            Координата конца линии угла по оси Оy
        """
        raise NotImplementedError

    def drawPoint(self, x: int, y: int) -> None:
        """Нарисовать точку в заданных координатах.

        Изменения на дисплее произойдут только после вызова метода «redraw».

        Параметры
        ---------
        x0: :class:`int`
            Координата точки по оси Ох
        y0: :class:`int`
            Координата точки по оси Оy
        """
        raise NotImplementedError

    def drawRect(self, x: int, y: int, l: int, h: int, filled: bool = False) -> None:
        """Нарисовать прямоугольник с левым верхним углом в указанных координатах
        и имеющий заданную ширину и высоту.

        Изменения на дисплее произойдут только после вызова метода «redraw».

        Параметры
        ---------
        x: :class:`int`
            Координата левого верхнего угла по оси Ох
        y: :class:`int`
            Координата левого верхнего угла по оси Оy
        l: :class:`int`
            Ширина прямоугольника
        h: :class:`int`
            Высота прямоугольника
        filled: :class:`bool`
            Заливать фигуру или нет, по умолчанию False
        """
        raise NotImplementedError

    def hide(self) -> None:
        """Закрыть и очистить окно для рисования."""
        raise NotImplementedError

    def redraw(self) -> None:
        """Перерисовать окно для рисования.

        Изменения на дисплее произойдут только после вызова этого метода.
        """
        raise NotImplementedError

    def removeLabels(self) -> None:
        """Удалить с экрана весь текст, добавленный на него вызовами метода «addLabel»."""
        raise NotImplementedError

    def setBackground(self, color: _COLOR) -> None:
        """Установить фон экрана в указанный цвет.

        Параметры
        ---------
        color: :class:`str`
            Возможные цвета:
            - white,
            - red, darkRed,
            - green, darkGreen,
            - blue, darkBlue,
            - cyan, darkCyan,
            - magenta, darkMagenta,
            - yellow, darkYellow,
            - gray, darkGray, lightGray,
            - black.
        """
        raise NotImplementedError

    def setPainterColor(self, color: _COLOR) -> None:
        """Установить цвет кисти, которой рисуются графические примитивы.

        Параметры
        ---------
        color: :class:`str`
            Возможные цвета:
            - white,
            - red, darkRed,
            - green, darkGreen,
            - blue, darkBlue,
            - cyan, darkCyan,
            - magenta, darkMagenta,
            - yellow, darkYellow,
            - gray, darkGray, lightGray,
            - black.
        """
        raise NotImplementedError

    def setPainterWidth(self, d: int) -> None:
        """Установить толщину кисти, которой рисуются графические примитивы, в пикселях.

        Параметры
        ---------
        d: :class:`int`
            Толщина
        """
        raise NotImplementedError

    def show(
        self, array: List[int], width: int, height: int, format: _ARRAY_FORMAT
    ) -> None:
        """Вывести на дисплей контроллера изображение, преобразованное из однородного массива данных.

        Параметры
        ---------
        array: list[:class:`int`]
            Одномерный целочисленный массив, имеющий размеры `width` на `height`
        width: :class:`int`
            Ширина изображения
        height: :class:`int`
            Высота изображения
        format: :class:`str`
            Формат, в котором представлен каждый элемент массива.
            Сейчас поддержаны форматы: «rgb32», «grayscale8», «rgb888»
        """
        raise NotImplementedError

    def showImage(self, imagePath: str) -> None:
        """Вывести на экран изображение, предварительно загруженное на робот.

        Параметры
        ---------
        imagePath: :class:`str`
            Имя файла с изображением
            (в форматах BMP, GIF, JPG, JPEG, PNG, PBM, PGM, PPM, TIFF, XBM, XPM),
            путь указывается либо абсолютным, либо относительно папки trik.
        """
        raise NotImplementedError


class encoder:
    """Представляет энкодеры силовых моторов, подключающиеся к портам E1, E2, E3, E4."""

    _PORT_NAME = Literal["E1", "E2", "E3", "E4"]

    def __init__(self) -> None:
        raise NotImplementedError

    def read(self, portName: _PORT_NAME) -> int:
        """Возвращает текущее показание энкодера в градусах на заданном порту.

        Параметры
        ---------
        portName: :class:`str`
            Порт
        """
        raise NotImplementedError

    def reset(self, portName: _PORT_NAME) -> None:
        """Сбрасывает в 0 текущее показание энкодера.

        Параметры
        ---------
        portName: :class:`str`
            Порт
        """
        raise NotImplementedError

    def readRawData(self, portName: _PORT_NAME) -> int:
        """Возвращает текущее показание энкодера в «тиках» на заданном порту.

        Параметры
        ---------
        portName: :class:`str`
            Порт
        """
        raise NotImplementedError


class BIOS:
    """typing purposes"""

    def __init__(self) -> None:
        raise NotImplementedError


class gyroscope:
    """Представляет гироскоп контроллера ТРИК.
    В состоянии покоя среднее значение выходного сигнала гироскопа
    не равно нулю и называется смещением нуля (bias) или
    систематической ошибкой (bias error).

    Параметр обусловлен многими факторами и может изменяться,
    например, в зависимости от окружающей температуры.

    Для правильной работы гироскопа необходимо вычитать смещение нуля
    из приходящих значений. Вычислить его можно с помощью метода «calibrate».
    Так как калибровка занимает длительное время, то при частом запуске модели
    можно выполнять ее один раз, после чего запоминать значение в переменную с
    помощью «getCalibrationVaules», а при запуске программы вместо калибровки
    вызывать «setCalibrationValues».
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def calibrate(self, mesc: int) -> None:
        """Вычисляет смещение нуля в течение указанного времени и инициализирует
        гироскоп этим параметром, сбрасывает текущие углы наклона.

        Параметры
        ---------
        mesc: :class:`int`
            Время калибровки в миллисекундах.
            Рекомендуемое время калибровки — 10-20 секунд.
        """
        raise NotImplementedError

    class calibrationFinished:
        @classmethod
        def connect(cls, func: Callable) -> None:
            raise NotImplementedError

    def getCalibrationValues(self) -> BIOS:
        """Возвращает объект, в котором содержатся необходимые данные о смещении нуля."""
        raise NotImplementedError

    def isCalibrated(self) -> bool:
        """Возвращает `True` в случае завершении калибровки, `False` — в противном случае."""
        raise NotImplementedError

    class newData:
        @classmethod
        def connect(cls, func: Callable) -> None:
            raise NotImplementedError

    def read(self) -> List[int]:
        """Возвращает массив из семи элементов:
        - 0-2 — угловые скорости по трем осям (в миллиградусах/секунды),
        - 3 — время последнего замера (в микросекундах),
        - 4-6 — углы наклона по трем осям (в миллиградусах).
        """
        raise NotImplementedError

    def readRawData(self) -> List[int]:
        """Возвращает массив из трех элементов с угловыми скоростями по трем осям."""
        raise NotImplementedError

    def setCalibrationValues(self, values: BIOS) -> None:
        """Устанавливает объект, содержащий необходимые параметры о смещении нуля.
        Параметры
        ---------
        mesc: :class:`int`
            Время калибровки в миллисекундах.
            Рекомендуемое время калибровки — 10-20 секунд.
        """
        raise NotImplementedError


class keys:
    """Служит для работы с кнопками на пульте робота."""

    def __init__(self) -> None:
        raise NotImplementedError

    class buttonPressed:
        """Посылается, когда кнопка с указанным кодом нажата или отпущена."""

        @classmethod
        def connect(self, func: Callable[[KeysEnum, Literal[0, 1]], Any]):
            """
            Параметры
            ---------
            func: Callable[[:class:`KeysEnum`, Literal[0, 1]], Any]
                Первый параметр — код кнопки,
                второй — 1, если кнопка нажата, 0, если отпущена.
            """
            raise NotImplementedError

    def isPressed(self, key: KeysEnum) -> bool:
        """Возвращает `True`, если кнопка с указанным кодом нажата в данный момент.

        Параметры
        ---------
        key: :class:`KeysEnum`
            Кнопка с кодом
        """
        raise NotImplementedError

    def reset(self) -> None:
        """Сбрасывает запомненные нажатия кнопок."""
        raise NotImplementedError

    def wasPressed(self, key: KeysEnum) -> bool:
        """Возвращает, была ли нажата кнопка с указанным кодом,
        сбрасывает запомненные нажатия для этой кнопки.

        Параметры
        ---------
        key: :class:`KeysEnum`
            Кнопка с кодом
        """
        raise NotImplementedError


class led:
    """Предоставляет управление светодиодом на корпусе робота."""

    def __init__(self, port: str) -> None:
        raise NotImplementedError

    def red(self) -> None:
        """Включает светодиод в режим «красный»."""
        raise NotImplementedError

    def green(self) -> None:
        """Включает светодиод в режим «зелёный»."""
        raise NotImplementedError

    def orange(self) -> None:
        """Включает светодиод в режим «оранжевый»."""
        raise NotImplementedError

    def off(self) -> None:
        """Выключает светодиод."""
        raise NotImplementedError


class lineSensor:
    """Видеокамера в режиме датчика линии."""

    def __init__(self) -> None:
        raise NotImplementedError

    def detect(self) -> None:
        """Определяет доминирующий цвет в вертикальной полосе в центре кадра
        и запоминает его как цвет линии. После этого метод «read» начинает
        возвращать данные для этой линии.
        """
        raise NotImplementedError

    def init(self, show_to_screen: bool) -> None:
        """Включает видеокамеру и инициализирует её в режиме датчика линии.
        Булевый параметр определяет, выводить ли на экран изображение с камеры.

        Параметры
        ---------
        show_to_screen: :class:`bool`
            Выводить ли на экран изображение с камеры
        """
        raise NotImplementedError

    def read(self) -> List[int]:
        """Возвращает массив, в ячейках которого находятся следующие данные:
        - в нулевой ячейке координата по оси X центра линии относительно центра кадра
        (от -100 до 100, -100 — центр линии на краю кадра слева);
        - в первой ячейке — вероятность перекрёстка
        (число от 0 до 100, показывающее сколько точек цвета линии находится в горизонтальной полосе в центре кадра);
        - во второй ячейке — относительный размер линии, число от 0 до 100
        (100 — линия занимает почти весь кадр, 0 — линии нет на кадре).
        """
        raise NotImplementedError

    def stop(self) -> None:
        """Выключает видеокамеру и прекращает работу датчика."""
        raise NotImplementedError


class motor:
    """Предоставляет управление мотором робота (силовым или сервомотором),
    подключающимся к портам M1, …, M4, S1, ..., S6.
    """

    def __init__(self, motorName: _MOTOR_NAME) -> None:
        raise NotImplementedError

    def brake(self, durationMs: int) -> None:
        """Блокировка моторов для торможения в течение указанного времени в миллисекундах.

        Параметры
        ---------
        durationMs: :class:`int`
            Время в миллисекундах
        """
        raise NotImplementedError

    def power(self) -> int:
        """Возвращает текущую мощность мотора (от -100 до 100)."""
        raise NotImplementedError

    def powerOff(self) -> None:
        """Выключает мотор."""
        raise NotImplementedError

    def setPower(self, power: int) -> None:
        """Включает мотор с указанной мощностью.

        Параметры
        ---------
        power: :class:`int`
            Мощность задаётся в диапазоне от -100 («полный назад») до 100 («полный вперёд»).
            0 соответствует `force break`, то есть мотор останавливается, при этом он заблокирован
            и остаётся под напряжением.
        """
        raise NotImplementedError


class objectSensor:
    """Видеокамера в режиме датчика объекта. Захватывает контрастный объект
    в центре кадра и возвращает его координаты и размер в кадре.
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def detect(self) -> None:
        """Определяет доминирующий цвет в центре кадра и запоминает его
        как цвет объекта. После этого метод «read» начинает возвращать
        данные для объекта.
        """
        raise NotImplementedError

    def init(self, show_to_screen: bool) -> None:
        """Включает видеокамеру и инициализирует её в режиме датчика объекта.

        Параметры
        ---------
        show_to_screen: :class:`int`
            Определяет, выводить ли на экран изображение с камеры
        """
        raise NotImplementedError

    def read(self) -> List[int]:
        """Возвращает массив, в ячейках которого находятся следующие данные:
        - в нулевой ячейке координата по оси X центра объекта относительно центра кадра
        (от -100 до 100, -100 — центр объекта на краю кадра слева);
        - в первой ячейке — координата по оси Y центра объекта относительно центра кадра
        (от -100 до 100, -100 — центр объекта на краю кадра сверху);
        - во второй ячейке — относительный размер объекта, число от 0 до 100
        (100 — объекта занимает почти весь кадр, 0 — объекта нет на кадре).
        """
        raise NotImplementedError

    def stop(self) -> None:
        """Выключает видеокамеру и прекращает работу датчика."""
        raise NotImplementedError


class marker:
    """Предоставляет доступ к рисованию маркером заданного цвета на полу.
    Доступен только в режиме 2D модели.
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def down(self, color: _COLOR) -> None:
        """Начать рисование маркером заданного цвета на полу.
        При движении робота в двумерной модели за ним будет оставаться цветная линия.
        Если был установлен маркер другого цвета, он будет заменен.

        Параметры
        ---------
        color: :class:`str`
            Возможные цвета:
            - white,
            - red, darkRed,
            - green, darkGreen,
            - blue, darkBlue,
            - cyan, darkCyan,
            - magenta, darkMagenta,
            - yellow, darkYellow,
            - gray, darkGray, lightGray,
            - black.
        """
        raise NotImplementedError

    def up(self) -> None:
        """Закончить рисование маркером."""
        raise NotImplementedError

    def isDown(self) -> bool:
        """Возвращает `True`, если маркер активен, `False` - если нет."""
        raise NotImplementedError

    def setDown(self, pos: bool) -> None:
        """Вызывает метод `down("black")`, или `up()` в зависимости от аргумента."""
        raise NotImplementedError


class sensor:
    def __init__(self, sensorName: _SENSOR_NAME) -> None:
        """Представляет сенсор (аналоговый или цифровой), подключающийся к портам A1, …, A6, D1, D2.

        Параметры
        ---------
        sensorName: :class:`str`
            Имя порта
        """
        raise NotImplementedError

    def read(self) -> int:
        """Возвращает текущее показание сенсора (цифрового или аналогового), подключённого к данному порту.
        Возвращается приведённое значение, зависящее от конфигурации порта, которая описывается
        в файле `model-config.xml` в папке trik на роботе.

        Например, ИК-датчик расстояния возвращает значение в сантиметрах.
        """
        raise NotImplementedError

    def readRawData(self) -> int:
        """Возвращает текущее «сырое» показание сенсора (цифрового или аналогового),
        подключённого к данному порту. Диапазон значений зависит от конкретного сенсора
        и не учитывает конфигурацию робота (возвращаются физические показания сенсора,
        например, задержка принятого ультразвукового сигнала).
        """
        raise NotImplementedError
