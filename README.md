# Calculator
A simple python calculator made while practicing OOP and best documentation practices.

##  Installation

```python
pip install git+https://github.com/SyroQT/TC-Calculator
```


## Usage
```python
from src.calculator import Calculator
c = Calculator(6) # Can provide initial state default is 0

print(c) # Output is 6 (the state) type str
print(c.state) # Output is 6 (the state) type int/float
```

Operations supported

```python
c.add(42) # adds to state
c.sub(3) # subs from state
c.mult(9) # multiplies state
c.div(2) # divides the state
c.root() # takes math.sqrt() of state
c.reset() # resets the state to 0
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

