try:
    num = int(input("Enter the value:  "))
    result = 10/num
    print(result)
except ValueError:
    print(" Please enter a valid number")
except ZeroDivisionError:
    print("Value cannot be divided by zero")
else:
    print(" the result",result)
finally:
    print("cleaning up the resouces")