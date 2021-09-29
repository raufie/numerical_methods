class Roots:
    def __init__(self, f, interval, theta, true_root=None):
        self.f = f
        self.interval = interval
        self.theta = theta
        self.true_root = true_root

    def apply_bisection(self):
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
                    print("f(x1),f(x2) both greater than 0")
                    break

                root = (self.interval[0]+self.interval[1])/2
                error = (abs(self.interval[0]-self.interval[1]) /
                         abs(self.interval[0]+self.interval[1]))*100
                print("root = "+str("{:.2f}".format(root)) +
                      " Error = "+str("{:.2f}".format(error)))

            else:
                print("f(x1),f(x2) both greater than 0")
                break

            if(abs(f(x1)-f(x2)) < theta):
                print("converged")
                print("root is " + str((x1+x2)/2))
                break

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
                print("converged")
                print("approx root is " + str(root))
                print("f(root) = " + str(self.f(*root)))
                break
            i += 1


r = Roots(lambda x, y: x**2-y**3 - 1, [[-5, -5], [5, 5]], 0.001)
r.apply_bisection_2_params()
