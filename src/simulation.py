import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from constantes import *
from soleil import Soleil
from planete import Planete

class Simulation:
    def __init__(self, sun_radius=sun_radius, M_sun=M_sun, earth_radius=earth_radius, M_earth=M_earth,
                 x_earth=x_earth, y_earth=y_earth, z_earth=z_earth, vx_earth=vx_earth, vy_earth=vy_earth, vz_earth=vz_earth):
        self._planets = []
        self._planets.append(Planete("Earth", earth_radius, M_earth, x_earth, y_earth, z_earth, vx_earth, vy_earth, vz_earth))
        self._sun = Soleil(sun_radius, M_sun)
        self._run()
    
    def _run(self):
        # Échelle d'affichage : mettre les positions en unités relatives (1 ~= 1 AU)
        if x_earth != 0:
            scale = 1.0 / x_earth
        else:
            scale = 1.0

        # initialiser les listes de positions avec la position initiale (mise à l'échelle)
        self._planets[0]._pos_x.append(self._planets[0].get_position[0] * scale)
        self._planets[0]._pos_y.append(self._planets[0].get_position[1] * scale)
        self._planets[0]._pos_z.append(self._planets[0].get_position[2] * scale)

        for i in range(steps):
            pos = self._planets[0].get_position
            r = np.linalg.norm(pos)  # distance Terre-Soleil (norme 3D)
            if r == 0:
                acc = np.array([0.0, 0.0, 0.0])
            else:
                acc = -G * M_sun * pos / r**3
            # appliquer l'accélération pour mettre à jour la vitesse, puis la position
            self._planets[0].apply_acceleration(acc, dt)
            self._planets[0].update_position(dt)
            # stocker la position mise à l'échelle pour le tracé
            self._planets[0]._pos_x.append(self._planets[0].get_position[0] * scale)
            self._planets[0]._pos_y.append(self._planets[0].get_position[1] * scale)
            self._planets[0]._pos_z.append(self._planets[0].get_position[2] * scale)
        self._plot()
    
    def _plot(self):
        fig = plt.figure(figsize=(9,6))
        ax = fig.add_subplot(111, projection='3d')
        # Tracer en unités mises à l'échelle (1 ~= 1 AU)
        grid = np.linspace(-2.5, 2.5, 150)
        X, Y = np.meshgrid(grid, grid)
        Z = np.zeros_like(X)
        ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.15)

        # appliquer la même échelle que dans _run
        if x_earth != 0:
            scale = 1.0 / x_earth
        else:
            scale = 1.0

        ax.plot_surface(self._sun.get_X_sun * scale, self._sun.get_Y_sun * scale, self._sun.get_Z_sun * scale, color='gold', shade=True)
        # marqueur central fixe pour le Soleil (taille en points)
        ax.scatter([0.0], [0.0], [0.0], color='gold', s=200)
        animated_earth, = ax.plot([self._planets[0]._pos_x[0]], [self._planets[0]._pos_y[0]], [self._planets[0]._pos_z[0]+0.05], 'o', color='blue')
        
        def _update(i):
            animated_earth.set_data([self._planets[0]._pos_x[i]], [self._planets[0]._pos_y[i]])
            animated_earth.set_3d_properties([self._planets[0]._pos_z[i] + 0.05])
            return animated_earth,

        ani = animation.FuncAnimation(fig, _update, frames=len(self._planets[0]._pos_x), interval=10, blit=True)
        ax.set_xlabel('x (AU)'); ax.set_ylabel('y (AU)'); ax.set_zlabel('z (AU)')
        ax.set_title("Simulation Système Solaire: Terre orbitant autour du Soleil")
        self._set_axes_equal(ax)
        plt.show()
    
    def _set_axes_equal(self, ax):
        x_limits, y_limits, z_limits = ax.get_xlim3d(), ax.get_ylim3d(), ax.get_zlim3d()
        x_range, y_range, z_range = [abs(l[1]-l[0]) for l in (x_limits, y_limits, z_limits)]
        max_range = max(x_range, y_range, z_range)
        centers = [np.mean(l) for l in (x_limits, y_limits, z_limits)]
        ax.set_xlim3d([centers[0]-max_range/2, centers[0]+max_range/2])
        ax.set_ylim3d([centers[1]-max_range/2, centers[1]+max_range/2])
        ax.set_zlim3d([centers[2]-max_range/2, centers[2]+max_range/2])

