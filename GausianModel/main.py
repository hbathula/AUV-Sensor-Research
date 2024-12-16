import numpy as np
import matplotlib.pyplot as plt

#generate 200 evenly spaced values between -10 and 10 along x-axis
#np.linspace creates an array of values with specified range
x = np.linspace(-100, 100, 2000)

#generates 200 evenly spaced value between -10 and 10 along y-axis
y = np.linspace(-100, 100, 2000)


#creates a 2D grid of x and y values
X, Y = np.meshgrid(x, y)


#defines coordinates of the source point (center of plume) at (0,0) in the 2D grid
source_x, source_y = 0, 0

#represents the width of plume in each direction
sigma_x, sigma_y = 20, 3

Z = np.exp(-((X - source_x)**2 / (2 * sigma_x**2) + (Y-source_y)**2 / (2 * sigma_y**2)))

log_Z = np.log10(Z)

plt.figure(figsize=(10,8))

'#50 contour levels specified to create smooth gradient'
plt.contourf(X, Y, log_Z, levels = 50, cmap="gray")

'#adds color bar next to plot'
plt.colorbar(label='log10 likelihood')

contour_levels = [-5, -4, -3, -2, -1]  # Increasing order
contours = plt.contour(X, Y, log_Z, levels=contour_levels, colors='yellow')
plt.clabel(contours, inline=True, fontsize=8)

# Mark the source point (representing zero detection likelihood at the source)
plt.plot(source_x, source_y, 'ro')  # Source location marked in red
plt.xlabel('Distance in km (x)')
plt.ylabel('Distance in km (y)')
plt.title('Oil Leak Concentration Plume (Log Detection Likelihood)')
plt.show()





