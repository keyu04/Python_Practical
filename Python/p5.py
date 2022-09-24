def maxn(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        maxn=num1
    elif (num2 > num1) and (num2 > num3):
        maxn=num2
    else:
        maxn = num3
    print("The Max numbers is : ", maxn)
def minn(num1, num2, num3):
    if (num1 < num2) and (num1 < num3):
        minn = num1
    elif (num2 < num1) and (num2 < num3):
        minn=num2
    else:
        minn=num3
    print("The Min numbers is : ", minn)

number1 = int(input('Enter First number : '))
number2 = int(input('Enter Second number : '))
number3 = int(input('Enter Third number : '))
maxn(number1, number2, number3)
minn(number1, number2, number3)
