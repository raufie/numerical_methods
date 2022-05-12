def iter(x1, x2, x3):
    x1 = (27-2*x2 + x3)/10
    x2 = (-61.5-2*x3+3*x1)/-6
    x3 = (-21.5 - x2 - x1)/5
    return x1, x2, x3


def main():
    x1 = x2 = x3 = 0
    for i in range(5):
        x1_old = x1
        x2_old = x2
        x3_old = x3
        x1, x2, x3 = iter(x1, x2, x3)
        print("iter ", i+1)
        print("x1= ", "{:.4f}".format(x1), "x2=", "{: .4f}".format(
            x2), "x3= ", "{:.4f}".format(x3), end=" ")
        print("error x3 = ", "{:.4f}".format(abs((x3-x3_old)/x3)*100))


main()
