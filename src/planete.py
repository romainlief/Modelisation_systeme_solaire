import numpy as np
from math import pi

class Planete:
    def __init__(self, name, radius, mass, x, y, z, vx, vy, vz, color):
        self._name = name
        self._radius = radius
        self._mass = mass

        # position et vitesse 
        # vecteur position (x, y, z) et vitesse (vx, vy, vz)
        self._pos = np.array([x, y, z], dtype=float)
        self._vel = np.array([vx, vy, vz], dtype=float)

        # maillage sphérique pour représentation visuelle de la planète
        u = np.linspace(0, 2*np.pi, 40)
        v = np.linspace(0, np.pi, 20)

        X = radius * np.outer(np.cos(u), np.sin(v))
        Y = radius * np.outer(np.sin(u), np.sin(v))
        Z = radius * np.outer(np.ones_like(u), np.cos(v))

        self._X = X + x
        self._Y = Y + y
        self._Z = Z + z
        
        self._pos_x = []
        self._pos_y = []
        self._pos_z = []
        
        self._color = color
        
        self._circumference = 2 * radius * pi
        
    def update_position(self, dt):
        self._pos += self._vel * dt
        
    @property
    def get_name(self):
        return self._name
    
    @property
    def get_radius(self):
        return self._radius
    
    @property
    def get_mass(self):
        return self._mass
    
    @property
    def get_position(self):
        return self._pos
    
    @get_position.setter
    def set_position(self, new_pos):
        self._pos = new_pos
    
    @property
    def get_velocity(self):
        return self._vel
    
    def apply_acceleration(self, acc : np.ndarray, dt: float):
        self._vel += np.array(acc, dtype=float) * dt
    
    @property
    def get_X(self):
        return self._X
    
    @get_X.setter
    def set_X(self, new_X):
        self._X = new_X
    
    @property
    def get_Y(self):
        return self._Y
    
    @get_Y.setter
    def set_Y(self, new_Y):
        self._Y = new_Y
    
    @property
    def get_Z(self):
        return self._Z
    
    @get_Z.setter
    def set_Z(self, new_Z):
        self._Z = new_Z
        
    @property
    def get_color(self):
        return self._color
    
    @property
    def get_circumference(self):
        return self._circumference