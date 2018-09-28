
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np

#takes given values for y and x and plots them, then plots a linear fit and
#displays the linear fit equation on the graph.

y = [-0.415, -0.375, -0.525, -1.625, -1.055, -1.265, -0.795] 
 
x = [5.19e14, 5.09e14, 5.49e14, 8.22e14, 6.88e14, 7.41e14, 6.17e14] 
    
plt.plot(x, y) 
plt.xlabel('frequency') 
plt.ylabel('stopping potential') 
plt.title('photo electric effect') 

slope, intercept = np.polyfit(x, y, 1)
abline_values = [slope * i + intercept for i in x]

# Plot the best fit line over the actual values
plt.plot(x, y, '--')
plt.plot(x, abline_values, 'b')
plt.title('linear fit')
plt.xlabel('frequency') 
plt.ylabel('stopping potential') 
a = round(intercept,3)
slo = round(slope, 18)
plt.text(5.5e14,-0.4, 'y = %sx + %a '%(slo,a))
plt.show()
print("y =" ,slope,"x +",intercept )

