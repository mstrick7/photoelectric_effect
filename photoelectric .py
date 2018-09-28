
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import csv

#reads data from excel table imported to csv, then prints plot

#plot for 577nm
x=[]
y=[]
with open('photoelectriclab04notext.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
plt.plot(x,y, marker='o')
plt.title('577 nm')
plt.xlabel('V')
plt.ylabel('I')
plt.grid(True)
plt.xlim(-2,1)
plt.show()


#plot for 589nm
x=[]
y=[]
with open('photoelectriclab04notext.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[2]))
plt.plot(x,y, marker='o')
plt.title('589 nm')
plt.xlabel('V')
plt.ylabel('I')
plt.grid(True)
plt.xlim(-2,1)
plt.show()


#plot for 656nm
x=[]
y=[]
with open('photoelectriclab04notext.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[3]))
plt.plot(x,y, marker='o')
plt.title('656 nm')
plt.xlabel('V')
plt.ylabel('I')
plt.grid(True)
plt.xlim(-2,1)
plt.show()


#plot for 546nm
x=[]
y=[]
with open('photoelectriclab04notext.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[4]))
plt.plot(x,y, marker='o')
plt.title('546 nm')
plt.xlabel('V')
plt.ylabel('I')
plt.grid(True)
plt.xlim(-2,1)
plt.show()


#plot for 365nm
x=[]
y=[]
with open('photoelectriclab04notext.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[5]))
plt.plot(x,y, marker='o')
plt.title('365 nm')
plt.xlabel('V')
plt.ylabel('I')
plt.grid(True)
plt.xlim(-2,1)
plt.show()


##plot for 436nm
x=[]
y=[]
with open('photoelectriclab04notext.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[6]))
plt.plot(x,y, marker='o')
plt.title('436 nm')
plt.xlabel('V')
plt.ylabel('I')
plt.grid(True)
plt.xlim(-2,1)
plt.show()


#plot for 405nm
x=[]
y=[]
with open('photoelectriclab04notext.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[7]))
plt.plot(x,y, marker='o')
plt.title('405 nm')
plt.xlabel('V')
plt.ylabel('I')
plt.grid(True)
plt.xlim(-2,1)
plt.show()


#plot for 486nm
x=[]
y=[]
with open('photoelectriclab04notext.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[8]))
plt.plot(x,y, marker='o')
plt.title('486 nm')
plt.xlabel('V')
plt.ylabel('I')
plt.grid(True)
plt.xlim(-2,1)
plt.show()


#plot for 656nm
x=[]
y=[]
with open('photoelectriclab04notext.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[9]))
plt.plot(x,y, marker='o')
plt.title('656 nm')
plt.xlabel('V')
plt.ylabel('I')
plt.grid(True)
plt.xlim(-2,1)
plt.show()

