G = 6.67430e-11  # constante gravitationnelle (m^3 kg^-1 s^-2)
# Pas de temps: 1 heure (3600 s) et ~8760 pas pour ~1 an
dt = 5 *3600.0      # delta t en secondes (1 heure)
steps = 5 * 8760     # nombre de pas (~1 an en heures)

# Soleil
sun_radius = 6.9634e8
M_sun = 1.989e30 

# Terre
earth_radius = 6371000
M_earth = 5.972e24   
x_earth = 1.496e11
y_earth = 0.0
z_earth = 0.0
vx_earth = 0.0
vy_earth = 29780.0               
vz_earth = 0.0

# rajouter les autres planètes

# Drap
k_depth = 0.1
k_sigma = 2.0
depth = k_depth * M_sun
sigma = k_sigma * sun_radius

# Bille
x, y = 2.0, 0.0 # position initiale de la bille
vx, vy = 0.0, 1.0 # vitesse initiale de la bille
