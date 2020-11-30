import matplotlib.pyplot as plt
import csv

x = []
y = []
z=  []
with open('node.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))

plt.plot(x,y, label='CPU Usage')
plt.plot(x,z, label='RAM Usage')
plt.xlabel('time in seconds')
plt.ylabel('% usage')

plt.title('x86- I7')
plt.legend()
plt.show()
