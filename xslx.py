import xlwt
from math import *

def xlsxwritter(data,data1,ops,wind,Kv0,Kn0,Ke0):
    a = len(data[0])
    i = 0
    n = 1
    wb = xlwt.Workbook()
    wsheet = wb.add_sheet('Параметры', cell_overwrite_ok = True)
    wsheet_dop = wb.add_sheet('Параметры другие', cell_overwrite_ok = True)

    wsheet.write(0,0,'t, с')
    wsheet.write(0,1,'xg, м')
    wsheet.write(0,2,'yg, м')
    wsheet.write(0,3,'zg, м')
    wsheet.write(0,4,'ϑ, град')
    wsheet.write(0,5,'ψ, град')
    wsheet.write(0,6,'γ, град')
    wsheet.write(0,7,'α, град')
    wsheet.write(0,8,'β, град')
    wsheet.write(0,9,'vxg, м/c')
    wsheet.write(0,10,'vyg, м/c')
    wsheet.write(0,11,'vzg, м/c')
    wsheet.write(0,12,'dv, град')
    wsheet.write(0,13,'dn, град')
    wsheet.write(0,14,'de, град')
    wsheet.write(0,15,'wx, рад/c')
    wsheet.write(0,16,'wy, рад/c')
    wsheet.write(0,17,'wz, рад/c')
    
    wsheet_dop.write(0,0,'t, с')
    wsheet_dop.write(0,1,'X, Н')
    wsheet_dop.write(0,2,'Y, Н')
    wsheet_dop.write(0,3,'Z, Н')
    wsheet_dop.write(0,4,'Mx, Н*м')
    wsheet_dop.write(0,5,'My, Н*м')
    wsheet_dop.write(0,6,'Mz, Н*м')
    wsheet_dop.write(0,7,'Fxg, Н')
    wsheet_dop.write(0,8,'Fyg, Н')
    wsheet_dop.write(0,9,'Fzg, Н')
    wsheet_dop.write(0,10,'rho, -')
    wsheet_dop.write(0,11,'ly, -')
    wsheet_dop.write(0,12,'mu, -')
    wsheet_dop.write(0,13,'nu, -')

    while n<=a:
        wsheet.write(n,0,data[0][i])
        wsheet.write(n,1,data[1][i])
        wsheet.write(n,2,data[2][i])
        wsheet.write(n,3,data[3][i])
        wsheet.write(n,4,degrees(data[4][i]))
        wsheet.write(n,5,degrees(data[5][i]))
        wsheet.write(n,6,degrees(data[6][i]))
        wsheet.write(n,7,degrees(data[7][i]))
        wsheet.write(n,8,degrees(data[8][i]))
        wsheet.write(n,9,data[9][i])
        wsheet.write(n,10,data[10][i])
        wsheet.write(n,11,data[11][i])
        wsheet.write(n,12,degrees(data[12][i]))
        wsheet.write(n,13,degrees(data[13][i]))
        wsheet.write(n,14,degrees(data[14][i]))
        wsheet.write(n,15,data[15][i])
        wsheet.write(n,16,data[16][i])
        wsheet.write(n,17,data[17][i])
        
        wsheet_dop.write(n,0,data1[0][i])
        wsheet_dop.write(n,1,data1[1][i])
        wsheet_dop.write(n,2,data1[2][i])
        wsheet_dop.write(n,3,data1[3][i])
        wsheet_dop.write(n,4,data1[4][i])
        wsheet_dop.write(n,5,data1[5][i])
        wsheet_dop.write(n,6,data1[6][i])
        wsheet_dop.write(n,7,data1[7][i])
        wsheet_dop.write(n,8,data1[8][i])
        wsheet_dop.write(n,9,data1[9][i])
        wsheet_dop.write(n,10,data1[10][i])
        wsheet_dop.write(n,11,data1[11][i])
        wsheet_dop.write(n,12,data1[12][i])
        wsheet_dop.write(n,13,data1[13][i])
    
        i += 1
        n += 1
    path = 'C:/Users/artem/Desktop/uts/vladik/'
    file = 'OTR '
    xls = '.xls'
    wind_txt = ''
    if ops == 1:
        wind_txt = 'wind_x='
    elif ops == 2:
        wind_txt = 'wind_z='
    elif ops == 3:
        wind_txt = 'wind_xz='
    else:
        wind_txt = 'without wind'
        wind = ''
    ss = ' kv='+str(Kv0)+' kn='+str(Kn0)+' ke='+str(Ke0)
    wb.save(path+file+wind_txt+str(wind)+ss+xls)