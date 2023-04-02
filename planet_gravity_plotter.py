import numpy as np
import matplotlib.pyplot as plt

# Dictionary of planet data, including mass and radius
planets = {
    "Mercury": {"mass": 3.3011e23, "radius": 2.4397e6},
    "Venus": {"mass": 4.8675e24, "radius": 6.0518e6},
    "Earth": {"mass": 5.972e24, "radius": 6.371e6},
    "Mars": {"mass": 6.4171e23, "radius": 3.3895e6},
    "Jupiter": {"mass": 1.8982e27, "radius": 6.9911e7},
    "Saturn": {"mass": 5.6834e26, "radius": 5.8232e7},
    "Uranus": {"mass": 8.6810e25, "radius": 2.5362e7},
    "Neptune": {"mass": 1.0243e26, "radius": 2.4622e7}
}

# Print the name of existing planets in planets dictionary
for planet_name in planets:
    print(planet_name)
# Ask the user for the name of the planet
planet_name = input("Enter the name of the planet: ")

# Get the planet data from the dictionary
planet_data = planets.get(planet_name)

# If the planet name is not in the dictionary, exit the program
if planet_data is None:
    print("Invalid planet name.")
    exit()

# Calculate the gravitational constant (G) and the planet's gravitational acceleration (g)
G = 6.6743e-11
g = G * planet_data["mass"] / planet_data["radius"] ** 2

# Create an array of distances from the planet (in meters)
distances = np.linspace(0, 3 * planet_data["radius"], 1000)

# Calculate the gravitational force on a spaceship at each distance
forces = G * planet_data["mass"] / distances ** 2

# Calculate the gravitational force on a spaceship at the planet's surface
surface_force = G * planet_data["mass"] / planet_data["radius"] ** 2

# Plot the graph of gravitational force vs. distance
plt.plot(distances, forces)
plt.axhline(y=surface_force, linestyle="--", color="gray")
plt.xlabel("Distance from planet (m)")
plt.ylabel("Gravitational force on spaceship (N)")
plt.title(f"Gravitational force on spaceship near {planet_name}")
plt.show()
