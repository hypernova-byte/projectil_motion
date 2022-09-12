import math
import numpy as np
import matplotlib.pyplot as plt

#launch degree / radian degree
launch_angle_degrees = 38
launch_angle = launch_angle_degrees * math.pi / 180

launch_speed = 5
#gravitational konstant
g = -9.81
#how far the diagram goes in the future
time_range = 101
measuring_times = []
#all the positions the projectile pases through
x_positions = np.array([])
y_positions = np.array([])

#splitting vector into x and y velocities
x_velocity = math.cos(launch_angle) * launch_speed
y_velocity = math.sin(launch_angle) * launch_speed

for i in range(time_range):

    measuring_times.append(i/100)
    np_measuring_times = np.array(measuring_times)
    
    y_positions = np_measuring_times * y_velocity + 0.5 * g * np_measuring_times ** 2
    x_positions = np_measuring_times * x_velocity 
    

print(y_positions)

title = "ball flying", launch_speed, "meters per second at ", launch_angle_degrees, "degrees"

y_positions = [value for value in y_positions if value >= 0]
x_positions = x_positions[:len(y_positions)]
print(y_positions)

plt.plot(x_positions, y_positions)
plt.xlabel("meters traveled in x-direction")
plt.ylabel("meters traveled in y-direction")
plt.title(title)

plt.show()



