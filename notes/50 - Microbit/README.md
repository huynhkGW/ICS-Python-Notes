# The BBC Micro:bit and Python


## Useful Links
- [Micro:bit Web IDE](https://python.microbit.org/v/2)
- [Python Quick Guide](https://microbit.org/get-started/user-guide/python/)
- [Micro:bit Python Docs](https://microbit-micropython.readthedocs.io/en/latest/index.html)


## Serial Communication

### Sending data from the microbit
```python3
from microbit import *

while True:
    reading = accelerometer.get_x()
    print(reading)
    if reading > 20:
        display.show("R")
    elif reading < -20:
        display.show("L")
    else:
        display.show("-")
    sleep(500)  #note the delay.  It is possible to send information too quickly.  Better to slow it down.
  ```
