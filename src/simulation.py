import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from constantes import *
from soleil import Soleil
from planete import Planete


class Simulation:
    def __init__(
        self,
        sun_radius=sun_radius,
        M_sun=M_sun,
        earth_radius=earth_radius,
        M_earth=M_earth,
        x_earth=x_earth,
        y_earth=y_earth,
        z_earth=z_earth,
        vx_earth=vx_earth,
        vy_earth=vy_earth,
        vz_earth=vz_earth,
        mars_radius=mars_radius,
        M_mars=M_mars,
        x_mars=x_mars,
        y_mars=y_mars,
        z_mars=z_mars,
        vx_mars=vx_mars,
        vy_mars=vy_mars,
        vz_mars=vz_mars,
        mercury_radius=mercury_radius,
        M_mercury=M_mercury,
        x_mercury=x_mercury,
        y_mercury=y_mercury,
        z_mercury=z_mercury,
        vx_mercury=vx_mercury,
        vy_mercury=vy_mercury,
        vz_mercury=vz_mercury,
        venus_radius=venus_radius,
        M_venus=M_venus,
        x_venus=x_venus,
        y_venus=y_venus,
        z_venus=z_venus,
        vx_venus=vx_venus,
        vy_venus=vy_venus,
        vz_venus=vz_venus,
        jupiter_radius=jupiter_radius,
        M_jupiter=M_jupiter,
        x_jupiter=x_jupiter,
        y_jupiter=y_jupiter,
        z_jupiter=z_jupiter,
        vx_jupiter=vx_jupiter,
        vy_jupiter=vy_jupiter,
        vz_jupiter=vz_jupiter,
    ):
        self._planets = []
        
        self._planets.append(
            Planete(
                "Earth",
                earth_radius,
                M_earth,
                x_earth,
                y_earth,
                z_earth,
                vx_earth,
                vy_earth,
                vz_earth,
            )
        )
        
        self._planets.append(
            Planete(
                "Mars",
                mars_radius,
                M_mars,
                x_mars,
                y_mars,
                z_mars,
                vx_mars,
                vy_mars,
                vz_mars,
            )
        )
        
        self._planets.append(
            Planete(
                "Mercure",
                mercury_radius,
                M_mercury,
                x_mercury,
                y_mercury,
                z_mercury,
                vx_mercury,
                vy_mercury,
                vz_mercury,
            )
        )
        
        self._planets.append(
            Planete(
                "Venus",
                venus_radius,
                M_venus,
                x_venus,
                y_venus,
                z_venus,
                vx_venus,
                vy_venus,
                vz_venus,
            )
        )
        
        self._planets.append(
            Planete(
                "Jupiter",
                jupiter_radius,
                M_jupiter,
                x_jupiter,
                y_jupiter,
                z_jupiter,
                vx_jupiter,
                vy_jupiter,
                vz_jupiter,
            )
        )
        
        self._sun = Soleil(sun_radius, M_sun)
        self._run()

    def _run(self):
        # Échelle d'affichage : mettre les positions en unités relatives (1 ~= 1 AU)
        scale = 1.0 / x_mercury

        # initialiser les listes de positions avec la position initiale (mise à l'échelle)
        for planet in self._planets:
            planet._pos_x.append(planet.get_position[0] * scale)
            planet._pos_y.append(planet.get_position[1] * scale)
            planet._pos_z.append(planet.get_position[2] * scale)

        for i in range(steps):
            for planet in self._planets:
                pos = planet.get_position
                r = np.linalg.norm(pos)  # distance planète-Soleil (norme 3D)
                acc = -G * M_sun * pos / r**3
                # appliquer l'accélération pour mettre à jour la vitesse, puis la position
                planet.apply_acceleration(acc, dt)
                planet.update_position(dt)
                # stocker la position mise à l'échelle pour le tracé
                planet._pos_x.append(planet.get_position[0] * scale)
                planet._pos_y.append(planet.get_position[1] * scale)
                planet._pos_z.append(planet.get_position[2] * scale)
        self._plot()

    def _plot(self):
        fig = plt.figure(figsize=(9, 6))
        ax = fig.add_subplot(111, projection="3d")
        # Tracer en unités mises à l'échelle (1 ~= 1 AU)
        grid = np.linspace(-2.5, 2.5, 150)
        X, Y = np.meshgrid(grid, grid)
        Z = np.zeros_like(X)
        ax.plot_surface(X, Y, Z, cmap="plasma", alpha=0.15)

        # appliquer la même échelle que dans _run
        scale = 1.0 / x_mercury

        ax.plot_surface(
            self._sun.get_X_sun * scale,
            self._sun.get_Y_sun * scale,
            self._sun.get_Z_sun * scale,
            color="gold",
            shade=True,
        )
        # marqueur central fixe pour le Soleil (taille en points)
        ax.scatter([0.0], [0.0], [0.0], color="gold", s=200)
        (animated_earth,) = ax.plot(
            [self._planets[0]._pos_x[0]],
            [self._planets[0]._pos_y[0]],
            [self._planets[0]._pos_z[0] + 0.05],
            "o",
            color="blue",
        )
        (animated_mars,) = ax.plot(
            [self._planets[1]._pos_x[0]],
            [self._planets[1]._pos_y[0]],
            [self._planets[1]._pos_z[0] + 0.05],
            "o",
            color="red",
        )
        
        (animated_mercury,) = ax.plot(
            [self._planets[2]._pos_x[0]],
            [self._planets[2]._pos_y[0]],
            [self._planets[2]._pos_z[0] + 0.05],
            "o",
            color="gray",
        )
        
        (animated_venus,) = ax.plot(
            [self._planets[3]._pos_x[0]],
            [self._planets[3]._pos_y[0]],
            [self._planets[3]._pos_z[0] + 0.05],
            "o",
            color="orange",
        )
        
        (animated_jupiter,) = ax.plot(
            [self._planets[4]._pos_x[0]],
            [self._planets[4]._pos_y[0]],
            [self._planets[4]._pos_z[0] + 0.05],
            "o",
            color="brown",
        )

        def _update(i):
            animated_earth.set_data(
                [self._planets[0]._pos_x[i]], [self._planets[0]._pos_y[i]]
            )
            animated_earth.set_3d_properties([self._planets[0]._pos_z[i] + 0.05])
            
            animated_mars.set_data(
                [self._planets[1]._pos_x[i]], [self._planets[1]._pos_y[i]]
            )
            animated_mars.set_3d_properties([self._planets[1]._pos_z[i] + 0.05])
            
            animated_mercury.set_data(
                [self._planets[2]._pos_x[i]], [self._planets[2]._pos_y[i]]
            )
            animated_mercury.set_3d_properties([self._planets[2]._pos_z[i] + 0.05])
            
            animated_venus.set_data(
                [self._planets[3]._pos_x[i]], [self._planets[3]._pos_y[i]]
            )
            animated_venus.set_3d_properties([self._planets[3]._pos_z[i] + 0.05])
            
            animated_jupiter.set_data(
                [self._planets[4]._pos_x[i]], [self._planets[4]._pos_y[i]]
            )
            animated_jupiter.set_3d_properties([self._planets[4]._pos_z[i] + 0.05])
            
            return animated_earth, animated_mars, animated_mercury, animated_venus, animated_jupiter
        ani = animation.FuncAnimation(
            fig, _update, frames=len(self._planets[0]._pos_x), interval=10, blit=True
        )
        ax.set_xlabel("x (AU)")
        ax.set_ylabel("y (AU)")
        ax.set_zlabel("z (AU)")
        ax.set_title("Simulation Système Solaire: Terre orbitant autour du Soleil")
        self._set_axes_equal(ax)
        plt.show()

    def _set_axes_equal(self, ax):
        x_limits, y_limits, z_limits = ax.get_xlim3d(), ax.get_ylim3d(), ax.get_zlim3d()
        x_range, y_range, z_range = [
            abs(l[1] - l[0]) for l in (x_limits, y_limits, z_limits)
        ]
        max_range = max(x_range, y_range, z_range)
        centers = [np.mean(l) for l in (x_limits, y_limits, z_limits)]
        ax.set_xlim3d([centers[0] - max_range / 2, centers[0] + max_range / 2])
        ax.set_ylim3d([centers[1] - max_range / 2, centers[1] + max_range / 2])
        ax.set_zlim3d([centers[2] - max_range / 2, centers[2] + max_range / 2])
