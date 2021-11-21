from pylab import legend
from pylab import plot, show 
from pylab import title,xlabel,ylabel
nyc_temp_chicago = [76, 75, 74, 73, 73, 72, 72, 74, 75, 75, 75, 76]
nyc_temp_ny =      [75, 75, 77, 77, 76, 76, 76, 75, 75, 75, 76, 76]

#time = range(70, 82)
time = ['12 AM', '1 AM', '2 AM', '3 AM', '4 AM', '5 AM', '6 AM', '7 AM', '8 AM', '9 AM', '10 AM', '11 AM']
plot(time, nyc_temp_chicago, time, nyc_temp_ny)
legend(['Chicago', 'New York'])
title('Temperature change NYC and Chicago')
xlabel('Time')
ylabel('Temperature')

show()