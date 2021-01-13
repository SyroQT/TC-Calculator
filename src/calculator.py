from math import sqrt


class Calculator:
    """A simple calculator class

    Attributes:
    -----------
        state

    Methods:
    --------
        add()
        sub()
        mult()
        div()
        root()
        reset()

    """

    def __init__(self, state: (float) = 0) -> None:
        """Init with base state which needs to be a number"""
        if type(state) not in [float, int]:
            raise ValueError("State needs to be a number")
        self.__state = state

    def __repr__(self):
        return str(self.__state)

    @property
    def state(self):
        """Getter for state returns current state"""
        return self.__state

    def add(self, value: (float)) -> None:
        """Adds value to the state"""
        self.__state += value

    def sub(self, value: (float)) -> None:
        """Subtracts value from state"""
        self.__state -= value

    def mult(self, value: (float)) -> None:
        """Multiplies state by value"""
        self.__state *= value

    def div(self, value: (float)) -> None:
        """Divides state by value"""
        self.__state /= value

    def root(self) -> None:
        """Takes square root of state"""
        self.__state = sqrt(self.__state)

    def reset(self) -> None:
        """Sets state to 0"""
        self.__state = 0
