from math import *
import numpy as np
N = 12
xg,yg,zg = 0,40000 - 100 * N,0
t = 0

# Габариты ОТР
m = 1200
dm = 1.4
l = 3.7
s = pi * dm**2 / 4

# Углы
thet = -radians(39)
gama = psi = betta = alpha = 0.0
deltav = deltan = deltae = 0
thets = thet - alpha

# Скорость
v = 4790 - 10 * N
vxg,vyg,vzg = v * cos(thets), v * sin(thets), 0

# Угловая скорость, момент инерции, G
wx,wy,wz = 0.4, 0, 0
Ix, Iy, Iz = 180, 700, 700
g = 9.80665