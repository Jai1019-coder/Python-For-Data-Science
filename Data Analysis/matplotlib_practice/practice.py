import matplotlib.pyplot as plt
x = [i for i in range(1,21)]
y = [j**2 for j in x]
plt.plot(x,y)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Basic Line Plot')
plt.show()