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

            root = (interval[0]+interval[1])/2
            error = (abs(interval[0]-interval[1]) /
                     abs(interval[0]+interval[1]))*100
            print("root = "+str("{:.2f}".format(root)) +
                  " Error = "+str("{:.2f}".format(error)))

        else:
            print("f(x1),f(x2) both greater than 0")

        if(abs(f(x1)-f(x2)) < theta):
            print("converged")
            print("root is " + str((x1+x2)/2))
            break


def f(x):
    return x*x


r_max = 1
apply_bisection(lambda x: f(x) - r_max, [0, 5], 0.01)
