clear all; close all; clc;
f = @(Z) Z.^5 + Z.^2 - Z + 1; 
fp = @(Z) 5*Z.^4 + 2*Z -1 ;

%roots
root1 = 0.66236 + 1i*0.56228 ; 
root2 = 0.66236 - 1i*0.56228; 
root3 = 0 + 1i*1;
root4 = 0- 1i*1;
root5 =-1.32472;
%grid space
nx = 2000; ny = 2000;
xmin = -2; xmax = 2; 
ymin = -2; ymax = 2;

x = linspace(xmin, xmax, nx);
y = linspace(ymin, ymax, ny);
[X,Y] = meshgrid(x,y);
%meshgrid just takes in two vectors and gives you a matrix of x and y
Z=X + 1i*Y;

n_iters = 40;
for n=1:n_iters
    Z = Z - f(Z)./fp(Z);
end
 

eps = 0.001;
Z1 = abs(Z-root1) < eps;
Z2 = abs(Z-root2)<eps;
Z3 = abs(Z-root3)<eps;
Z4 = abs(Z-root4)<eps;
Z5 = abs(Z-root5)<eps;
Z6 = ~(Z1+Z3+Z2+Z4+Z5);

figure;
map = [0.95 0.05 0 ; 0.05 0.80 0.80 ; 0.23 0.81 0.03; 0.81 0.035 0.70;0.4 0.6980 1.0;0 0 0];%red, green, blue, red
colormap(map)

Z = (Z1 + 2*Z2 + 3*Z3 + 4*Z4+5*Z5 + 6*Z6);
image([xmin xmax], [ymin ymax], Z);
set(gca,  'YDir', 'normal'); %VIP, image processing people use y direction inverted.. we as math people use it from -ve to +ve

axis equal; axis tight;
%equal: same on both axes, axis tight, no white space where there is none
set(gca, 'XTick', linspace(xmin, xmax, 5), 'YTick', linspace(ymin, ymax, 5));
xlabel('$x$', 'Interpreter','latex', 'FontSize',14);
ylabel('$y$', 'Interpreter', 'latex', 'FontSize', 14);
title('fractal from $f(z)= z^5 + z^2 - z + 1$','Interpreter','latex', 'FontSize', 16);
