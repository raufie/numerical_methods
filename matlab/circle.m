clear all, close all, clc;
theta  = linspace(0,pi*2);
x = cos(theta);y = sin(theta)
plot(x,y);
axis equal;
axis([-1.1,1.1,-1.1,1.1])
ax = gca; %get current axis handel
ax.XTick = [-1 -0.5 0. 0.5 1];
ax.YTick = [-1 -0.5 0. 0.5 1];
xlabel('$x$', 'interpreter','latex', 'FontSize',14)
ylabel('$y$', 'interpreter', 'latex', 'FontSize', 14)
title('Plot of a circle', 'interpreter','latex', 'FontSize', 16);