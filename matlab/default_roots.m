%roots.m(takes polynomial gives all complex roots) and fzero.m are default functions
%x^3-3x^2+4x-2=0
p = [1,-3,4,-2];
r = roots(p);
%fzero find one root of a non linear function
% f here must be defined as an anonymous function or a sub function
%also needs a guess
f = @(x,a) x - exp(-a*x);
a=0.5;
x0 = 0;
r =  fzero(@(x)f(x,a), x0);

r = roots([1,0,0,0,0,0,-1])