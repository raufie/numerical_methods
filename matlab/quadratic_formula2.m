function [p,q] = quadratic_formula2(a,b,c)
if b < 0
    p = (-b + sqrt(b^2 - 4*a*c))/2*a 
    q = 2*c/(-b + sqrt(b^2 - 4*a*c))
else 
    p = 2*c/(-b - sqrt(b^2 - 4*a*c))
    q = (-b - sqrt(b^2 - 4*a*c))/2*a
end