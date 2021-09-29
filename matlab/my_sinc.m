% if end
% if else end

function y=my_sinc(x)
if x~= 0 
    y = sin(x)/x;
else
    y = 1;
end

