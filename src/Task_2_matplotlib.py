import matplotlib.pyplot as plt

x = [1,2,3]
y = [4,5,6]

plt.plot(x,y)
plt.grid(True)
plt.show()

x_1 = range(1,20)
y_1 = []

for i in x_1:
    y_1.append(i*3)

plt.plot(x_1,y_1, color='red')
plt.title('wykres')
plt.grid(True)

plt.show()