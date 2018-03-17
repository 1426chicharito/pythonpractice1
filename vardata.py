def celc_far(a):
    if a == 0:
        print("the temperature in Fahrenheit is 32")
    else:
        b = 32 + 1.8*a
        print("the temperature in Fahrenheit is {0}".format(b))
a = input(print("enter temperature in degree"))
celc_far(int(a))
