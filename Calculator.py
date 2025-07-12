import math

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
            print(f"{result:.2f}")
        except ZeroDivisionError:
            print("Can't divide with zero.")
        except TypeError:
            print("can't divide with strings.")
        except IndexError:
            print("You should give a input.")


        #✅ The Formula:
        #    LCM(𝑎,𝑏)=        𝑎×𝑏
        #                   GCD(𝑎,𝑏)


    def lcm(self,*args:int):
        try:
            result = args[0]
            for num in args[1:]:
                result = (result * num) // math.gcd(result,num)
            
            if isinstance(result,str):
                print("⚠️  can't find lcm of strings.")
            else:
                print(result)
        except TypeError:
            print("⚠️  can't find lcm of strings.")
        except IndexError:
            print("⚠️  no numbers provided.")
            

user = calculator()
user.lcm(4,6,12)