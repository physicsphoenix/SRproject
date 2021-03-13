import math as m
# Input data
R = 40.0
c = 18.0 
v = c*0.7
n = 4


# Calculate values 
x_start = R*(3/2-(1+v/c)/4/n)
x_tank  = (R/2)*(5-3*v/n/c+2*v/c)
y_tank  = (  2*R + R*(n-1)/n + R/2/n/c*m.sqrt(c**2-v**2))
dt = R/n/c
dx = R*v/n/c

# print values
print('Given:' )
print(' R = radius of plunger     = {:5.2f} cm'.format(R))
print(' c = speed of water wave   = {:5.2f} cm/s'.format(c))
print(' v = simulated velocity    = {:5.2f} cm/s'.format(v))
print(' n = number of impressions = {}'.format(n))
print('If the left wall of the tank is x = 0 then:')
print(' first impressions is at {:5.2f}'.format(x_start))
print(' the tank length is      {:5.2f}'.format(x_tank))
print(' the tank width is       {:5.2f}'.format(y_tank))
print(' the plunger will make {} impressions {:5.2f} cm appart every {:5.2f}s'.
      format(n,dx,dt))
