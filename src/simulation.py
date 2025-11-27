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
        color_earth=color_earth,
        mars_radius=mars_radius,
        M_mars=M_mars,
        x_mars=x_mars,
        y_mars=y_mars,
        z_mars=z_mars,
        vx_mars=vx_mars,
        vy_mars=vy_mars,
        vz_mars=vz_mars,
        color_mars=color_mars,
        mercury_radius=mercury_radius,
        M_mercury=M_mercury,
        x_mercury=x_mercury,
        y_mercury=y_mercury,
        z_mercury=z_mercury,
        vx_mercury=vx_mercury,
        vy_mercury=vy_mercury,
        vz_mercury=vz_mercury,
        color_mercury=color_mercury,
        venus_radius=venus_radius,
        M_venus=M_venus,
        x_venus=x_venus,
        y_venus=y_venus,
        z_venus=z_venus,
        vx_venus=vx_venus,
        vy_venus=vy_venus,
        vz_venus=vz_venus,
        color_venus=color_venus,
        jupiter_radius=jupiter_radius,
        M_jupiter=M_jupiter,
        x_jupiter=x_jupiter,
        y_jupiter=y_jupiter,
        z_jupiter=z_jupiter,
        vx_jupiter=vx_jupiter,
        vy_jupiter=vy_jupiter,
        vz_jupiter=vz_jupiter,
        color_jupiter=color_jupiter,
        saturn_radius=saturn_radius,
        M_saturn=M_saturn,
        x_saturn=x_saturn,
        y_saturn=y_saturn,
        z_saturn=z_saturn,
        vx_saturn=vx_saturn,
        vy_saturn=vy_saturn,
        vz_saturn=vz_saturn,
        color_saturn=color_saturn,
        uranus_radius=uranus_radius,
        M_uranus=M_uranus,
        x_uranus=x_uranus,
        y_uranus=y_uranus,
        z_uranus=z_uranus,
        vx_uranus=vx_uranus,
        vy_uranus=vy_uranus,
        vz_uranus=vz_uranus,
        color_uranus=color_uranus,
        neptune_radius=neptune_radius,
        M_neptune=M_neptune,
        x_neptune=x_neptune,
        y_neptune=y_neptune,
        z_neptune=z_neptune,
        vx_neptune=vx_neptune,
        vy_neptune=vy_neptune,
        vz_neptune=vz_neptune,
        color_neptune=color_neptune,
        display_scale=1.0,
        _camera_angle_turning = False,
    ):
        self._planets = []
        self._camera_angle = 45.0 
        self._camera_angle_turning = _camera_angle_turning

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
                color_earth,
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
                color_mars,
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
                color_mercury,
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
                color_venus,
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
                color_jupiter,
            )
        )

        self._planets.append(
            Planete(
                "Saturn",
                saturn_radius,
                M_saturn,
                x_saturn,
                y_saturn,
                z_saturn,
                vx_saturn,
                vy_saturn,
                vz_saturn,
                color_saturn,
            )
        )

        self._planets.append(
            Planete(
                "Uranus",
                uranus_radius,
                M_uranus,
                x_uranus,
                y_uranus,
                z_uranus,
                vx_uranus,
                vy_uranus,
                vz_uranus,
                color_uranus,
            )
        )

        self._planets.append(
            Planete(
                "Neptune",
                neptune_radius,
                M_neptune,
                x_neptune,
                y_neptune,
                z_neptune,
                vx_neptune,
                vy_neptune,
                vz_neptune,
                color_neptune,
            )
        )

        self._sun = Soleil(sun_radius, M_sun)
        self._display_scale = display_scale
        self._run()

    def _run(self):
        # Échelle d'affichage : utiliser la plus grande orbite initiale comme référence
        # (la planète la plus éloignée sera ~1.0 dans l'affichage)
        max_orbit = 0.0
        for planet in self._planets:
            r0 = abs(planet.get_position[0])
            if r0 > max_orbit:
                max_orbit = r0

        self._scale = 1.0 / max_orbit

        # initialiser les listes de positions avec la position initiale (mise à l'échelle)
        for planet in self._planets:
            scaled = self._scale_position(planet.get_position)
            planet._pos_x.append(scaled[0])
            planet._pos_y.append(scaled[1])
            planet._pos_z.append(scaled[2])

        for i in range(steps):
            for planet in self._planets:
                pos = planet.get_position
                r = np.linalg.norm(pos)  # distance planète-Soleil (norme 3D)
                acc = -G * M_sun * pos / r**3
                # appliquer l'accélération pour mettre à jour la vitesse, puis la position
                planet.apply_acceleration(acc, dt)
                planet.update_position(dt)
                # stocker la position mise à l'échelle pour le tracé
                scaled = self._scale_position(planet.get_position)
                planet._pos_x.append(scaled[0])
                planet._pos_y.append(scaled[1])
                planet._pos_z.append(scaled[2])
        self._plot()

    def _plot(self):
        fig = plt.figure(figsize=(20, 12))
        manager = plt.get_current_fig_manager()
        try:
            manager.full_screen_toggle()  # plein écran natif
        except:
            pass

        ax = fig.add_subplot(111, projection="3d")

        # ---- ZOOM UTILISATEUR ----
        zoom_scale = 0.9  # facteur de zoom (scroll in/out)

        def on_scroll(event):
            cur_xlim = ax.get_xlim3d()
            cur_ylim = ax.get_ylim3d()
            cur_zlim = ax.get_zlim3d()

            x_center = np.mean(cur_xlim)
            y_center = np.mean(cur_ylim)
            z_center = np.mean(cur_zlim)

            if event.button == "up":  # zoom in
                scale = zoom_scale
            else:  # zoom out
                scale = 1 / zoom_scale

            ax.set_xlim3d(
                [
                    (cur_xlim[0] - x_center) * scale + x_center,
                    (cur_xlim[1] - x_center) * scale + x_center,
                ]
            )

            ax.set_ylim3d(
                [
                    (cur_ylim[0] - y_center) * scale + y_center,
                    (cur_ylim[1] - y_center) * scale + y_center,
                ]
            )

            ax.set_zlim3d(
                [
                    (cur_zlim[0] - z_center) * scale + z_center,
                    (cur_zlim[1] - z_center) * scale + z_center,
                ]
            )

            fig.canvas.draw_idle()

        fig.canvas.mpl_connect("scroll_event", on_scroll)

        max_coord = 0.0
        for p in self._planets:
            if p._pos_x:
                max_coord = max(max_coord, np.nanmax(np.abs(p._pos_x)))
                max_coord = max(max_coord, np.nanmax(np.abs(p._pos_y)))
                max_coord = max(max_coord, np.nanmax(np.abs(p._pos_z)))
        limit = max_coord * 1.5

        grid = np.linspace(-limit, limit, 300)
        X, Y = np.meshgrid(grid, grid)
        Z = np.zeros_like(X)
        ax.plot_surface(X, Y, Z, cmap="plasma", alpha=0.08)

        scale = getattr(self, "_scale", (1.0 / x_earth))

        # Soleil
        ax.plot_surface(
            self._sun.get_X_sun * scale,
            self._sun.get_Y_sun * scale,
            self._sun.get_Z_sun * scale,
            color="gold",
            shade=True,
        )
        real_radius_sun = self._sun.get_circumference / (2 * np.pi)
        scaled_radius_sun = self._scale_radius(real_radius_sun)
        sun_vis_size = max(40, scaled_radius_sun * 12500) # modificateur taille du soleil
        ax.scatter([0.0], [0.0], [0.0], color="gold", s=sun_vis_size)

        # Planètes
        animated_objs = []
        colors = [planet.get_color for planet in self._planets]

        for idx, planet in enumerate(self._planets):
            # Rayon réel via la circonférence
            real_radius = planet.get_circumference / (2 * np.pi)
            # Rayon compressé avec la même loi que les positions
            scaled_radius = self._scale_radius(real_radius)
            # Marker visible (points, pas mètres)
            vis_size = max(4, scaled_radius * 500)  # 500 = facteur visuel ajustable

            (animated,) = ax.plot(
                [planet._pos_x[0]],
                [planet._pos_y[0]],
                [planet._pos_z[0]],
                "o",
                color=colors[idx % len(colors)],
                markersize=vis_size,
            )
            animated_objs.append(animated)

        def _update(i):
            for idx, animated in enumerate(animated_objs):
                p = self._planets[idx]
                animated.set_data([p._pos_x[i]], [p._pos_y[i]])
                animated.set_3d_properties([p._pos_z[i]])

            # Camera orbitale
            if self._camera_angle_turning:
                self._camera_angle += 0.25
                ax.view_init(elev=20, azim=self._camera_angle)

            return tuple(animated_objs)

        if self._camera_angle_turning:
            
            ani = animation.FuncAnimation(
            fig,
            _update,
            frames=len(self._planets[0]._pos_x),
            interval=20,  
            blit=False,  # Permet de redessiner la vue caméra à chaque frame
        )
        else:
            ani = animation.FuncAnimation(
                fig,
                _update,
                frames=len(self._planets[0]._pos_x),
                interval=10,
                blit=True,
            )

        ax.set_xlabel("x (AU)")
        ax.set_ylabel("y (AU)")
        ax.set_zlabel("z (AU)")
        ax.set_title("Simulation Système Solaire (Vue Plein Écran)")

        self._set_axes_equal(ax)
        plt.show()

    def _set_axes_equal(self, ax):
        """Set 3D plot axes to equal scale.

        Args:
            ax (matplotlib.axes._subplots.Axes3DSubplot): 3D axes object.
        """
        x_limits, y_limits, z_limits = ax.get_xlim3d(), ax.get_ylim3d(), ax.get_zlim3d()
        x_range, y_range, z_range = [
            abs(l[1] - l[0]) for l in (x_limits, y_limits, z_limits)
        ]
        max_range = max(x_range, y_range, z_range)
        centers = [np.mean(l) for l in (x_limits, y_limits, z_limits)]
        ax.set_xlim3d([centers[0] - max_range / 2, centers[0] + max_range / 2])
        ax.set_ylim3d([centers[1] - max_range / 2, centers[1] + max_range / 2])
        ax.set_zlim3d([centers[2] - max_range / 2, centers[2] + max_range / 2])

    def _scale_position(self, pos, k=0.25):
        """Scale the position vector for better visualization.

        Args:
            pos (np.ndarray): position vector.
            k (float, optional): scaling exponent. Defaults to 0.35.

        Returns:
            np.ndarray: scaled position vector.
        """
        r = np.linalg.norm(pos)
        if r == 0:
            return pos

        r_scaled = r**k  
        return pos / r * r_scaled

    def _scale_radius(self, radius, k=0.35):
        ref = 1.0 / self._scale 
        r_norm = radius / ref
        r_scaled = r_norm ** k
        return r_scaled
