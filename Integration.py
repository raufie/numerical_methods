class Integration:
    def __init__(self, a, b, N):
        self.a = a
        self.b = b
        self.N = N
        self.h = (b-a)/N
# trapz

    def getTrapezoidal(self, f):
        s = 0
        for i in range(1, self.N):
            s += f(self.a+self.h*i)
        s = (f(self.a)+f(self.b)) + s*2
        s *= (self.h/2)
        return s
# simpz3/8

    def getSimps3(self, f):
        s = 0
        for i in range(1, self.N):
            if i % 2 == 1:
                s += (4*f(self.a + self.h*i))
            else:
                s += (2*f(self.a + self.h*i))
        s += (f(self.a)+f(self.b))
        s *= (self.h/3)
        return s

    def getSimps8(self, f):
        s = 0
        for i in range(1, self.N):
            if i % 3 != 0:
                s += (3*f(self.a + self.h*i))
            else:
                s += (4*f(self.a + self.h*i))
        s += (f(self.a)+f(self.b))
        s *= (3*self.h/8)
        return s


if __name__ == "__main__":
    a = 0
    b = 3
    N = 9

    def f(x):
        return (x**2/(1+x**3))
    integ = Integration(a, b, N)
    print('trapezoidal', integ.getTrapezoidal(f))
    print('simpsons', integ.getSimps3(f))
    print('simpsons 3/8th', integ.getSimps8(f))
