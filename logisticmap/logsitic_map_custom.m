mu_min=2.4; mu_max=4; %range of mu values
n_mu=500; %number of mu pixels
n_x=400; %number of x pixels
mu_edges=linspace(mu_min,mu_max,n_mu+1); %edges of mu pixels
mu=(mu_edges(1:n_mu)+mu_edges(2:n_mu+1))/2; %values of mu on which to perform computation
x_edges=linspace(0,1,n_x+1); %edges of x pixels

n_trans=20000; %transient iterations
n_data=5;  %number of x values per mu value

x_data=zeros(n_data,n_mu); %x-data used to construct figure

x_0=0.5; %initial condition

% WRITE THE COMPUTATIONAL ENGINE OF THE CODE.
% USE THE ALREADY DEFINED PARAMETERS AND VARIABLES: n_mu, mu, x_0, n_trans, n_data.
% YOUR FINAL RESULT WILL BE THE VARIABLE x_data, and this variable will be assessed.

%loop one
i = 1;
%length(mu)
length(x_data(1,:))
for m = mu
    x = x_0;
    %now lets iterate the logistic map for mu and get the converged
    %solution
    for j=1:n_trans
        x = m*x*(1- x);
    
    end
    
    %now we must get multiple data points iterating on this x value for
    %this mu
    
    for k = 1: n_data
        %this must be the same thing again just list of it so we can plot
        x = m*x*(1- x);
        x_data(k,i) = x;
    end
    
    i = i+1;
    
end


%save('x_mat','x_data')

i = 1;
%disp(mu)
for m = mu
    for k = 1: n_data
        plot(m,x_data(k, i),'.')
        axis([0 5 0 1])
       
    end
    i = i +1;
    hold on;
        %disp(x_data(k, i))
    pause(0.000000000001)
end


