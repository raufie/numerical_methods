k = 0.05; 
% Assign theta, x, and y below. Do not change these variable names. 
theta = linspace(-10*pi, 10*pi, 2000);
x = exp(k.*theta).*cos(theta);
y = exp(k.*theta).*sin(theta);
% Graphics
plot(x,y);
axis equal;
xlabel('$x$', 'Interpreter', 'latex', 'FontSize', 14);
ylabel('$y$', 'Interpreter', 'latex', 'FontSize', 14);
title('Logarithmic Spiral','Interpreter','latex','FontSize', 16);
