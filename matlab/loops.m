clc;
ntimes = 10000;
x = 0.532;
r = 2.5;
for n=1:ntimes
    x = r*x*(1-x);
end
fprintf('%f\n',x)

