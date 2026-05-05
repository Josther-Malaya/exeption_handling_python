class CalculatorEngine:

    def evaluate(self, expression):
        try:
            result = eval(expression)
            return str(result)
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero!")
        except Exception:
            raise ValueError("Invalid input!")