class Bisection:
    def __init__(self, f, interval, theta=0.001, true_root=None):
        self.f = f
        self.interval = interval
        self.x1_original = interval[0]
        self.x2_original = interval[1]

        self.theta = theta
        self.true_root = true_root

    def fit(self, verbose=False):
        f = self.f
        theta = self.theta
        while True:
            x1 = self.interval[0]
            x2 = self.interval[1]
            root = x1+x2/2
            if f(x1)*f(x2) < 0:
                # divide and continue
                mid = (x1+x2) / 2
                if f(x1)*f(mid) < 0:
                    self.interval = [x1, mid]
                # print(self.interval, end=" ")
                elif f(mid)*f(x2) < 0:
                    self.interval = [mid, x2]
                # print(self.interval, end=" ")
                else:
                    print(
                        "f(x1),f(x2) both greater than 0") if verbose == True else None
                    break

                root = (self.interval[0]+self.interval[1])/2
                error = (abs(self.interval[0]-self.interval[1]) /
                         abs(self.interval[0]+self.interval[1]))*100
                print("root = "+str("{:.2f}".format(root)) +
                      " Error = "+str("{:.2f}".format(error))) if verbose == True else None

            else:
                print("f(x1),f(x2) both greater than 0") if verbose == True else None
                break

            if(abs(f(x1)-f(x2)) < theta):

                print((x1+x2)/2)
                return self.interval

    def get_iteration_table(self):
        t = self.true_root
        x1 = self.x1_original
        x2 = self.x2_original
        # <- [xL,xU], t = True root
        # -> needs the run iteration function
        #

        xr_old = None
        for i in range(10):
            xr, fx1, fx2, fxr = self.__run_iteration(x1, x2, xr_old, t)
            if fx1*fxr < 0:
                x2 = xr
            else:
                x1 = xr
            xr_old = xr
    # helper f_n

    def __run_iteration(self, x1, x2, xr_old, t):
        xr = (x1+x2)/2
        fx1 = self.f(x1)
        fx2 = self.f(x2)
        if xr_old != None:
            e_a = abs((xr-xr_old)/xr)*100
        else:
            e_a = " - "
        e_t = abs((t-xr)/t)*100
        fxr = self.f(xr)
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

  # Redundant--

    def apply_bisection_2_params(self):
        f = self.f
        theta = self.theta
        # iteratively
        i = 0
        while True:
            x1 = self.interval[0][0]
            y1 = self.interval[0][1]
            x2 = self.interval[1][0]
            y2 = self.interval[1][1]

            root = [x1+x2/2, y1+y2/2]
            if f(x1, y1)*f(x2, y2) < 0:
                # divide and continue
                mid = [(x1+x2) / 2, (y1+y2)/2]
                if f(x1, y1)*f(*mid) < 0:
                    self.interval = [[x1, y1], mid]
                    print(self.interval, end=" ")
                elif f(*mid)*f(x2, y2) < 0:
                    self.interval = [mid, [x2, y2]]
                    print(self.interval, end=" ")
                else:
                    print("f(x1, y1),f(x2, y2) both greater than 0")
                    break

                root = [(self.interval[0][0]+self.interval[0][1])/2,
                        (self.interval[1][0]+self.interval[1][1])/2]

                # error = (abs(self.interval[0][0]-self.interval[0][1]) /
                #          abs(self.interval[0][0]+self.interval[1][1]))*100
                error = abs(f(x1, x2)-f(x2, y2))
                print("root = ("+str("{:.2f}".format(root[0]))+", " + str("{:.2f}".format(root[1])) + ")" +
                      " Error (AE) = "+str("{:.2f}".format(error)))

            else:
                print("f(x1),f(x2) both greater than 0")
                break

            # if(abs(f(x1, x2)-f(x2, y2)) < theta):
            #     print("converged")
            #     print("root is " + str(root))
            #     break
            if (i > 10):
                print("iterations increased 10")
                print(root)
                print("f(root) = " + str(self.f(*root)))
                break
            i += 1


class Newton:
    def __init__(self, x0, f, f_, iterations=10):
        self.interval = [x0]
        self.f = f
        self.f_ = f_

    def fit(self, verbose=True):
        x_n = self.interval[0]
        for i in range(10):
            x_n = x_n - (self.f(x_n) / self.f_(x_n))
            print(x_n,  self.f(x_n)) if verbose == True else None
        print(x_n)
        return x_n
        # r = Roots(lambda x, y: x**2-y**3 - 1, [[-5, -5], [5, 5]], 0.001)
        # r.apply_bisection_2_params()


class Secant:
    def __init__(self, x0, x1, f, iterations=10):
        self.interval = [x0, x1]
        self.f = f
        self.f_ = f_

    def fit(self, verbose=True):
        x_n_1 = self.interval[0]

        x_n = self.invertal[1]
        # calculating by hand
        #
        try:
            for i in range(10):
                f_ = (self.f(x_n)-self.f(x_n_1))/(x_n - x_n_1)
                x_n_1 = x_n
                x_n = x_n - (self.f(x_n) / f_)
                print(x_n,  self.f(x_n)) if verbose == True else None
        except:
            print("xn - xn-1 probably reached 0 (machine epsilon limitation)")
            return x_n
        return x_n


class Convergence:
    def __init__(self, err, p):
        self.err = err
        self.p = p

    def check_convergence(self, iters):
        print("iter", 0, " ", end="")
        print(self.err)
        for i in range(iters):
            self.err = 1/2 * (self.err)**self.p
            print("iter", i+1, " ", end="")
            print(self.err)


b = Bisection(lambda x: x**2 - 1, interval=[0, 5], theta=0.0001, true_root=1)
b.fit(verbose=False)
# b.get_iteration_table()
n = Newton(1, lambda x: x**2 - 3, lambda x: 2*(x))
n.fit(verbose=False)

s = Newton(1, 2, lambda x: x**2 - 3)
n.fit(verbose=True)
