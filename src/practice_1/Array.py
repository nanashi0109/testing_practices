class Array:

    def __init__(self, args):
        self.array = args

    def sum(self) -> float:
        summa = 0

        if not self.array:
            return None

        for i in self.array:
            summa += i

        return summa

    def multiply(self) -> float:
        multiply = 1

        if not self.array:
            return None

        for i in self.array:
            multiply *= i

        return multiply

    def average(self) -> float:
        if not self.array:
            return None

        return self.sum() / len(self.array)