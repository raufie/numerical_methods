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
    return 4*(x**3)-6*(x**2) + 7*x - 2.3
    # return (x**10) - 1


def run_iteration(x1, x2, xr_old, t):
    xr = (x1+x2)/2
    fx1 = f(x1)
    fx2 = f(x2)
    if xr_old != None:
        e_a = abs((xr-xr_old)/xr)*100
    else:
        e_a = " - "
    e_t = abs((t-xr)/t)*100
    fxr = f(xr)
    print("x_1 = "+str("{: .4f}".format(x1)).ljust(8), end=" | ")
    print("x_r = "+str("{: .4f}".format(xr)).ljust(8), end=" | ")
    print("x_2 = "+str("{: .4f}".format(x2)).ljust(8), end=" | ")

    print("fx1 = "+str("{: .4f}".format(fx1)).ljust(8), end=" | ")
    print("fx2 = "+str("{: .4f}".format(fx2)).ljust(8), end=" | ")
    print("fxr = "+str("{: .4f}".format(fxr)).ljust(8), end=" | ")
    if xr_old != None:
        print("e_a = "+str("{: .4f}".format(e_a)).ljust(8), end=" | ")
    else:
        print(str("     -    ").ljust(14), end="|")
    print("e_t = " + str("{: .4f}".format(e_t)).ljust(8))
    return xr, fx1, fx2, fxr


def run_tabular(x1, x2, t):
    # <- [xL,xU], t = True root
    # -> needs the run iteration function
    #

    xr_old = None
    for i in range(10):
        xr, fx1, fx2, fxr = run_iteration(x1, x2, xr_old, t)
        if fx1*fxr < 0:
            x2 = xr
        else:
            x1 = xr
        xr_old = xr


def apply_newton(x_0, f, f_):
    x_n = x_0
    for i in range(10):
        x_n = x_n - (f(x_n) / f_(x_n))
        print(x_n,  f(x_n))


def apply_secant(x_0, x_1, f):
    x_n_1 = x_0

    x_n = x_1
    # calculating by hand
    #
    try:
        for i in range(10):
            f_ = (f(x_n)-f(x_n_1))/(x_n - x_n_1)
            x_n_1 = x_n
            x_n = x_n - (f(x_n) / f_)
            print(x_n,  f(x_n))
    except:
        print("xn - xn-1 probably reached 0 (machine epsilon limitation)")


# apply_bisection(f, [0, 2], 0.0001)
# run_tabular(0, 1, 0.45)
# apply_newton(1, lambda x: x**2 - 3, lambda x: 2*(x))
apply_secant(1, 2, lambda x: x**2 - 3)
