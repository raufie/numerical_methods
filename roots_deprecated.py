import numpy as np


def apply_bisection(f, interval, theta):

    while True:
        x1 = interval[0]
        x2 = interval[1]
        root = x1+x2/2
        if f(x1)*f(x2) < 0:
            # divide and continue
            mid = (x1+x2) / 2
            if f(x1)*f(mid) < 0:
                interval = [x1, mid]
               # print(interval, end=" ")
            elif f(mid)*f(x2) < 0:
                interval = [mid, x2]
               # print(interval, end=" ")
            else:
                print("f(x1),f(x2) both greater than 0")
                break

            root = (interval[0]+interval[1])/2
            error = (abs(interval[0]-interval[1]) /
                     abs(interval[0]+interval[1]))*100
            print("root = "+str("{:.2f}".format(root)) +
                  " Error = "+str("{:.2f}".format(error)))

        else:
            print("f(x1),f(x2) both greater than 0")
            break

        if(abs(f(x1)-f(x2)) < theta):
            print("converged")
            print("root is " + str((x1+x2)/2))
            break


def f(x):
    return -12 - 21*x + 18 * x**2 - 2.75*x**3


def run_iteration(x1, x2, xr_old, t):
    xr = (x1+x2)/2
    fx1 = f(x1)
    fx2 = f(x2)
    e_a = abs((xr-xr_old)/xr)*100
    e_t = abs((t-xr)/t)*100
    fxr = f(xr)
    print("x_1 = "+str("{: .4f}".format(x1)), end=" | ")
    print("x_r = "+str("{: .4f}".format(xr)), end=" | ")
    print("x_2 = "+str("{: .4f}".format(x2)), end=" | ")

    print("fx1 = "+str("{: .4f}".format(fx1)), end=" | ")
    print("fx2 = "+str("{: .4f}".format(fx2)), end=" | ")
    print("fxr = "+str("{: .4f}".format(fxr)), end=" | ")
    print("e_a= "+str("{: .4f}".format(e_a)), end=" | ")
    print("e_t = " + str("{: .4f}".format(e_t)))
    return xr, fx1, fx2, fxr


def run_tabular(x1, x2, t):
    # <- [xL,xU], t = True root
    # -> needs the run iteration function
    #

    xr_old = 1
    for i in range(10):
        xr, fx1, fx2, fxr = run_iteration(x1, x2, xr_old, t)
        if fx1*fxr < 0:
            x2 = xr
        else:
            x1 = xr
        xr_old = xr


#apply_bisection(f, [0, 2], 0.0001)
# run_tabular()
