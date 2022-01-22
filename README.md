# trikset.py-typehint
Python type hint library for TRIK. Use at your own risk if you're advanced TRIK user.

# Installing

Windows:
```
py -m pip install trik-py-typehint
```
Unix/Mac OS:
```
python3 -m pip install trik-py-typehint
```

# Usage
```python

import sys
import time
import random
import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from trik import *


class Program():
    __interpretation_started_timestamp__ = time.time() * 1000

    pi = 3.141592653589793

    def execMain(self):

        brick.display().addLabel("Hi from typed TRIK Python!", 1, 1, 20)
        brick.display().redraw()

        brick.stop()
        return

    def main():
        program = Program()
        program.execMain()

if __name__ == '__main__':
    main()
```
