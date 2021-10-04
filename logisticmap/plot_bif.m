mu_min=2.4; mu_max=4; %range of mu values
n_mu=500; %number of mu pixels
mu_edges=linspace(mu_min,mu_max,n_mu+1); %edges of mu pixels
mu=(mu_edges(1:n_mu)+mu_edges(2:n_mu+1))/2; %values of mu on which to perform computation





m = matfile('x_mat.mat');
x_data = m.x_data;
length(x_data)
%ax = gca
i = 1;
%disp(mu)
for m = mu
    for k = 1: length(x_data)

  
        plot(m,x_data(k, i),'.')
        axis([0 5 0 1])
       
    end
    i = i +1;
    hold on;
        %disp(x_data(k, i))
    pause(0.000000000001)
end

