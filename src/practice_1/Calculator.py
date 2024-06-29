class Calculator:

    def add(self, value_left, value_right) -> float:
        if not isinstance(value_right and value_left, (int, float)):
            raise TypeError("")

        return value_left + value_right

    def subtract(self, value_left, value_right) -> float:
        if not isinstance(value_right and value_left, (int, float)):
            raise TypeError("")

        return value_left - value_right

    def multiply(self, value_left, value_right) -> float:
        if not isinstance(value_right and value_left, (int, float)):
            raise TypeError("")

        return value_left * value_right

    def divide(self, value_left, value_right) -> float:
        if not isinstance(value_right and value_left, (int, float)):
            raise TypeError("")

        if(value_right == 0):
            raise ValueError()

        return value_left / value_right
