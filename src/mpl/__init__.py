import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100)
y = x * 2
z = x ** 2

# Task 1
figure = plt.figure()
axes = figure.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y, 'b')
axes.set_xlabel('Ось x')
axes.set_ylabel('Ось y')
axes.set_title('Header')
plt.show()

# Task 2
figure = plt.figure()
axes = figure.add_axes([0.1, 0.1, 0.8, 0.8])
axes_small = figure.add_axes([0.5, 0.5, 0.2, 0.2])
axes.set_xlabel('Ось x большого графика')
axes.set_ylabel('Ось y большого графика')
axes_small.set_xlabel('Ось x малого графика')
axes_small.set_ylabel('Ось y малого графика')
axes.set_title('Header')
plt.show()

# Task 3
figure = plt.figure()
axes = figure.add_axes([0.1, 0.1, 0.8, 0.8])
axes_small = figure.add_axes([0.55, 0.45, 0.2, 0.2])
axes.set_title('Header')
axes.plot(x, y, 'b')
axes_small.plot(x, y, 'b')
plt.show()

# Task 4
x = np.linspace(0, 5, 11)
y = x ** 2
figure, axes = plt.subplots(nrows=1, ncols=2,figsize=(12,3))

axes[0].plot(x, y, 'b')

axes[1].plot(x, y, 'r--')
plt.show()
