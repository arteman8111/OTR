from aerodynamic import *
from atmos import *
from id0 import *
from mm import *
from xslx import *
import numpy as np

def main(ops,wind,Kv0,Kn0,Ke0):
    # Параметры управления
    Kv = Kv0
    Kn = Kn0
    Ke1 = Ke2 = Ke0
    
    if ops == 1:
        Wx = wind
        Wz = 0
    elif ops == 2:
        Wx = 0
        Wz = wind
    elif ops == 3:
        Wx = wind
        Wz = wind
    else:
        Wx = 0
        Wz = 0
    
    rhoRG, lyRG, muRG, nuRG = rg(psi,thet,gama)
    Wssk = np.array([[-Wx],[0],[-Wz]])
    betta0 = asin(-Wz/v)
    VECTOR = [t,xg,yg,zg,thet,psi,gama,alpha,betta+betta0,vxg,vyg,vzg,deltav,deltan,deltae,wx,wy,wz,rhoRG,lyRG,muRG,nuRG]
    XLSX = [[t],[xg],[yg],[zg],[thet],[psi],[gama],[alpha],[betta+betta0],[vxg],[vyg],[vzg],[deltav],[deltan],[deltae],[wx],[wy],[wz],[rhoRG],[lyRG],[muRG],[nuRG]]
    XLSX_DOP = [[t],[0],[0],[0],[0],[0],[0],[0],[0],[0],[rhoRG],[lyRG],[muRG],[nuRG]]
    
    def get_fly(vec):
        dt = 1e-4
        while vec[2] >= 1e-4:
            vec_prev = vec.copy()
            V = (vec[9]**2 + vec[10]**2 + vec[11]**2)**0.5 
            # Определение АДХ
            rho,a= atm(vec[2])
            M = V / a  
            q = rho*V**2/2
            # Определение скоростей
            X,Y,Z,Mx,My,Mz = adh(M,s,l,V,q,vec[15],vec[16],vec[17],vec[7],vec[8],vec[12],vec[13],vec[14])

            Fssk = np.array([[-X],[Y],[Z]])
            Anzsk_ssk = nzsk_ssk(vec[18],vec[19],vec[20],vec[21])
            Fnzsk = np.matmul(np.linalg.inv(Anzsk_ssk),Fssk)
            Fxg, Fyg, Fzg = Fnzsk[0,0],Fnzsk[1,0],Fnzsk[2,0]

            # Пересчет параметров 
            euiler(vec,Fxg,Fyg,Fzg,Mx,My,Mz,vec[9],vec[10],vec[11],vec[1],vec[2],vec[3],vec[15],vec[16],vec[17],vec[18],vec[19],vec[20],vec[21],vec[0],dt)
            rg_norm = (vec[18]**2 + vec[19]**2 + vec[20]**2 + vec[21]**2)**0.5
            vec[18], vec[19], vec[20], vec[21] = vec[18] / rg_norm, vec[19] / rg_norm, vec[20] / rg_norm, vec[21] / rg_norm

            Vnzsk = np.array([[vec[9]],[vec[10]],[vec[11]]])
            Anzsk_ssk = nzsk_ssk(vec[18],vec[19],vec[20],vec[21])
            Vssk = np.matmul(Anzsk_ssk, Vnzsk)
            Vssk[0,0], Vssk[2,0] = Vssk[0,0] + Wssk[0,0], Vssk[2,0] + Wssk[2,0]

            vec[4] = thetf(vec[18],vec[19],vec[20],vec[21])
            vec[5] = psif(vec[18],vec[19],vec[20],vec[21])
            vec[6] = gammaf(vec[18],vec[19],vec[20],vec[21])
            vec[7] = alphaf(Vssk[1,0], Vssk[0,0])
            vec[8] = bettaf(Vssk[2,0],np.linalg.norm(Vssk))
            vec[12] = deltavf(vec[4],vec_prev[4],dt,Kv)
            vec[13] = deltanf(vec[5],vec_prev[5],dt,Kn)
            vec[14] = deltaef(vec[6],vec_prev[6],dt,Ke1,Ke2)

            # Прибавляем шаг
            vec[0] += dt

            # Точность 1e-4
            if vec[2] < 0:
                vec, vec_prev = vec_prev.copy(), vec.copy()
                dt = dt / 10
                continue
            
            if round(vec[0],5) * 100 % 25 == 0.00000 or (vec[2] <= 1e-4 and vec[2] > 0):
                print(vec[0])
                vec_dop = [vec[0],X,Y,Z,Mx,My,Mz,Fxg,Fyg,Fzg,vec[18],vec[19],vec[20],vec[21]]
                for c in range(18):
                    XLSX[c].append(vec[c])
                for k in range(len(vec_dop)):
                    XLSX_DOP[k].append(vec_dop[k])
    get_fly(VECTOR)
    xlsxwritter(XLSX,XLSX_DOP,ops,wind,Kv0,Kn0,Ke0)
    print('Конец расчета...')

ops = 0 # Параметры 0 - без ветра; 1 - встречный ветер; 2 - боковой ветер; 3 - В+Б 
W = 0 # Скорость ветра
# Параметры упраления
Kv = 0
Kn = 0
Ke = 0
main(ops,W,Kv,Kn,Ke)