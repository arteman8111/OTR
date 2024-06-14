from math import *

# AERODYNAMIC
def Cx(M, alfa_):
    return 1 / (73.211 / exp(M) - 47.483 / M + 16.878)

def Cy_alfa(M, alfa_):
    Ds = 11.554 / exp(M) - 2.5191e-3 * M * M - 5.024 / M + 52.836e-3 * M + 4.112
    if Ds >= 0:
        return sqrt(Ds)
    else:
        return 1.039

def Cy_deltav(M, alfa_):
    alfa_ = fabs(alfa_ * 180 / pi)
    p1 = 1 / (243.84e-3 / exp(alfa_) + 74.309e-3)
    p2 = log(1.9773 * alfa_ * alfa_ - 25.587 * alfa_ + 83.354)
    p3 = 18.985 * alfa_ * alfa_ - 375.76 * alfa_ + 1471
    p4 = -51.164e-3 * alfa_ * alfa_ + 805.52e-3 * alfa_ + 1.8929

    return (-p1 * 1e-6 * M * M + p2 * 1e-12 * exp(M) - p3 * 1e-6 * M - p4 * 1e-3) * 2

def Cz_beta(M, alfa_):
    return -Cy_alfa(M, alfa_)

def Cz_deltan(M, alfa_):
    return -Cy_deltav(M, alfa_)

def mx_wx(M, alfa_):
    return -0.005

def mz_wz(M, alfa_):
    return (146.79e-6*M*M - 158.98e-3/M - 7.6396e-3*M - 68.195e-3);

def mz_alfa(M, alfa_):
    return (-766.79e-3/exp(M) + 438.74e-3/M + 5.8822e-3*M - 158.34e-3);

def mz_deltav(M, alfa_):
    alfa_ = fabs(alfa_* 180 / pi);
    k1 = exp(-19.488e-3*alfa_*alfa_ - 378.62e-3*alfa_ + 6.7518);
    k2 = exp(-21.234e-3*alfa_*alfa_ - 635.84e-6*exp(alfa_) - 98.296e-3*alfa_ + 2.5938);
    return sqrt(k1*1e-9*M*M + k2*1e-6);

def my_wy(M, alfa_):
    return mz_wz(M, alfa_)

def my_beta(M, beta):
    return mz_alfa(M, beta)

def my_deltan(M, beta_):
    return mz_deltav(M, beta_)

def adh(M,s,l,v,q,wx,wy,wz,alpha,beta,deltav,deltan,deltae):
    # АД коэффициенты
    cx = Cx(M, alpha)
    cy = Cy_alfa(M, alpha) * alpha + Cy_deltav(M, alpha) * deltav
    cz = Cz_beta(M, alpha) * beta + Cz_deltan(M, alpha) * deltan

    # Силы
    X = cx*q*s
    Y = cy*q*s
    Z = cz*q*s
    
    mstx, msty, mstz = 100, 0, 0

    # АД коэффы моментов
    mx = mx_wx(M, alpha)*wx*l/v 
    my = my_wy(M, alpha)*wy*l/v + my_beta(M,alpha)*beta + my_deltan(M,beta)*deltan
    mz = mz_wz(M, alpha)*wz*l/v + mz_alfa(M, alpha)*alpha + mz_deltav(M, alpha)*deltav
    
    # Моменты
    Mx = mx*q*s*l + mstx * deltae
    My = my*q*s*l + msty
    Mz = mz*q*s*l + mstz
    
    return X,Y,Z,Mx,My,Mz