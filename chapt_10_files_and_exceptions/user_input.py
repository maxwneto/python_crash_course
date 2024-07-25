number1 = input("Type the numerator: ")
number2 = input("Type the denominator: ")


try:
    result = int(number1) / int(number2)

except ZeroDivisionError:
    print("Denominator must be higher than 0!")

else:
    msg = "{} / {} is: {:.2f}"
    print(msg.format(number1, number2, result))