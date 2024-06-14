from id0 import *
from math import *
import numpy as np

def dvxg(Fxg):
    return Fxg/m

def dvyg(Fyg):
    return Fyg/m-g

def dvzg(Fzg):
    return Fzg/m

def dxg(vxg):
    return vxg

def dyg(vyg):
    return vyg

def dzg(vzg):
    return vzg

def dwx(Mx,wy,wz):
    return Mx/Ix - (Iz - Iy)*wy*wz/Ix

def dwy(My,wx,wz):
    return My/Iy - (Ix - Iz)*wx*wz/Iy

def dwz(Mz,wx,wy):
    return Mz/Iz - (Iy - Ix)*wx*wy/Iz

def drhoRG(rorg,larg,murg,nurg,wx,wy,wz):
    return -(wx*larg + wy*murg + wz*nurg)/2

def dlyRG(rorg,larg,murg,nurg,wx,wy,wz):
    return (wx*rorg - wy*nurg + wz*murg)/2

def dmuRG(rorg,larg,murg,nurg,wx,wy,wz):
    return (wx*nurg + wy*rorg - wz*larg)/2

def dnuRG(rorg,larg,murg,nurg,wx,wy,wz):
    return (-wx*murg + wy*larg + wz*rorg)/2

def thetf(rho, ly, mu, nu):
    return asin(2 * (rho * nu + ly * mu))

def psif(rho, ly, mu, nu):
    return atan2(2*(rho * mu - ly * nu), rho**2 + ly**2 - mu**2 - nu**2)

def gammaf(rho, ly, mu, nu):
    return atan2(2*(rho * ly - mu * nu), rho**2 - ly**2 + mu**2 - nu**2)

def alphaf(vy,vx):
    return -atan2(vy,vx)

def bettaf(vz,V):
    return asin(vz/V)

def deltavf(thet,thet_prev,dt,Kv):
    dthet = (thet - thet_prev)/dt
    return -Kv*dthet

def deltanf(psi,psi_prev,dt,Kn):
    dpsi = (psi-psi_prev)/dt
    return -Kn*dpsi

def deltaef(gama,gama_prev,dt,Ke1,Ke2):
    dgama = (gama-gama_prev)/dt
    return -Ke1*dgama -Ke2*gama

def rg(psi, thet, gamma):
    rorg = cos(psi/2)*cos(thet/2)*cos(gamma/2)-sin(psi/2)*sin(thet/2)*sin(gamma/2)
    larg = sin(psi/2)*sin(thet/2)*cos(gamma/2)+cos(psi/2)*cos(thet/2)*sin(gamma/2)
    murg = sin(psi/2)*cos(thet/2)*cos(gamma/2)+cos(psi/2)*sin(thet/2)*sin(gamma/2)
    nurg = cos(psi/2)*sin(thet/2)*cos(gamma/2)-sin(psi/2)*cos(thet/2)*sin(gamma/2)
    return (rorg, larg, murg, nurg)

def nzsk_ssk(rho, ly, mu, nu):
    A = np.array([
        [rho**2 + ly**2 - mu**2 - nu**2, 2 * (rho * nu + ly * mu), 2 * (-rho * mu + ly * nu)],
        [2 * (-rho * nu + ly * mu), rho**2 - ly**2 + mu**2 - nu**2, 2 * (rho * ly + nu * mu)],
        [2 * (rho * mu + ly * nu), 2 * (-rho * ly + mu * nu), rho**2 - ly**2 - mu**2 + nu**2]
    ])
    return A
    
def euiler(vec,Fxg,Fyg,Fzg,Mx,My,Mz,vxg,vyg,vzg,xg,yg,zg,wx,wy,wz,rhoRG,lyRG,muRG,nuRG,t,dt):
    vec[9] += dvxg(Fxg)*dt
    vec[10] += dvyg(Fyg)*dt
    vec[11] += dvzg(Fzg)*dt
    vec[1] += dxg(vxg)*dt
    vec[2] += dyg(vyg)*dt
    vec[3] += dzg(vzg)*dt
    vec[15] += dwx(Mx,wy,wz)*dt
    vec[16] += dwy(My,wx,wz)*dt
    vec[17] += dwz(Mz,wx,wy)*dt
    vec[18] += drhoRG(rhoRG,lyRG,muRG,nuRG,wx,wy,wz)*dt
    vec[19] += dlyRG(rhoRG,lyRG,muRG,nuRG,wx,wy,wz)*dt
    vec[20] += dmuRG(rhoRG,lyRG,muRG,nuRG,wx,wy,wz)*dt
    vec[21] += dnuRG(rhoRG,lyRG,muRG,nuRG,wx,wy,wz)*dt