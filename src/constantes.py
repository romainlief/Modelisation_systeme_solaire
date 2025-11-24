G = 6.67430e-11  # constante gravitationnelle (m^3 kg^-1 s^-2)
# Pas de temps: 1 heure (3600 s) et ~8760 pas pour ~1 an
dt = 10 *3600.0      # delta t en secondes (1 heure)
steps = 10 * 8760     # nombre de pas (~1 an en heures)

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

# Mars
mars_radius = 3389500
M_mars = 6.4185e23
x_mars = 2.279e11
y_mars = 0.0
z_mars = 0.0
vx_mars = 0.0
vy_mars = 24080.0
vz_mars = 0.0

# Mercure
mercury_radius = 2439700
M_mercury = 3.3011e23
x_mercury = 5.791e10
y_mercury = 0.0
z_mercury = 0.0
vx_mercury = 0.0
vy_mercury = 47362.0
vz_mercury = 0.0

# Vénus

venus_radius = 6051800
M_venus = 4.8675e24
x_venus = 1.082e11
y_venus = 0.0
z_venus = 0.0
vx_venus = 0.0
vy_venus = 35020.0
vz_venus = 0.0

# Jupiter

jupiter_radius = 69911000
M_jupiter = 1.8982e27
x_jupiter = 7.785e11
y_jupiter = 0.0
z_jupiter = 0.0
vx_jupiter = 0.0
vy_jupiter = 13070.0
vz_jupiter = 0.0

# Bille
x, y = 2.0, 0.0 # position initiale de la bille
vx, vy = 0.0, 1.0 # vitesse initiale de la bille
