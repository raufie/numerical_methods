tol = 1.e-08;
x = 0.1;
r = 2.5;
error = 2*tol;
while error > tol;
    xold = x;
    x = r*x*(1-x);
    error = abs (x-xold);
end
fprintf('%f\n',x)