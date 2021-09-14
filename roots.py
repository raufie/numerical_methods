import numpy as np


def apply_bisection(f, interval, theta):
    while True:
        x1 = interval[0]
        x2 = interval[1]
        if f(x1)*f(x2) < 0:
            # divide and continue
            mid = (x1+x2) / 2
            if f(x1)*f(mid) < 0:
                interval = [x1, mid]
                print(interval)
            elif f(mid)*f(x2) < 0:
                interval = [mid, x2]
                print(interval)
            else:
                print("f(x1),f(x2) both greater than 0")
        else:
            print("f(x1),f(x2) both greater than 0")

        if(abs(f(x1)-f(x2)) < theta):
            print("converged")
            print("root is " + str((x1+x2)/2))
            break


apply_bisection(lambda x: x**2 - 4, [0, 3], 0.01)
