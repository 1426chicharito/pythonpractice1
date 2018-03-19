def cel_far(*args):
    for a in args:

        if   a<-273.15:
            print("The lowest possible temperature that physical matter can reach is -273.15 °")
        else:
            b = 32 + 1.8*a

        print("the temperature in Fahrenheit is {0}".format(b))
        for i in range(0,4):
            with open("data.txt","r+") as file:
                    a=file.write("the temperature in Fahrenheit is {0}".format(b))

cel_far(2,0,4,5)
