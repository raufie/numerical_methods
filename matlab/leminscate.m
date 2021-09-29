% Assign theta, x, and y below. Do not change these variable names. 
theta = linspace(-pi/4, pi/4, 1000)
x = cos(theta).*sqrt(2.*cos(2.*theta))
y = sin(theta).*sqrt(2.*cos(2.*theta))
% graphics
plot(x,y,'r',-x,y,'r')
axis equal;
axis([-1 1 -1 1])
xlabel('$x$', 'Interpreter', 'latex', 'FontSize',14);
ax = gca;
ylabel('$y$', 'Interpreter', 'latex', 'FontSize',14);
title('Leminscate', 'Interpreter', 'latex', 'FontSize', 16)
ax.YLabel.Rotation = 0
ax.YTickLabelRotation=90;