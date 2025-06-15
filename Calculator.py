class calculator:
    def __init__(self):
        pass

    def add(self, *args: int):
        try:
            if not args:
                print("No number provided!")
            else:
                print(sum(args)) 
        except TypeError:
            print("⚠️  Addition is done only with numbers.")

    def subtract(self,*args:int):
        try:
            result = args[0]
            for i in args[1:]:
                result -= i
            print(result)
        except TypeError:
            print("Can't subtract with strings.")
        except IndexError:
            print("You should give a input.")

    def multiply(self, *args: int):
        if not args:
            print("No number provided.")
        else:
            result = 1
            for i in args:
                result *= i

            if isinstance(result, str):  # Ensures result is not a string
                print("⚠️  You should give a number!")
            else:
                print(result)

    def divide(self,*args:int):
        try:
            result = args[0]
            for i in args[1:]:
                result /= i
            print(result)
        except ZeroDivisionError:
            print("Can't divide with zero.")
        except TypeError:
            print("can't divide with strings.")
        except IndexError:
            print("You should give a input.")

user = calculator()
user.multiply(3,6)
user.divide()
user.subtract()