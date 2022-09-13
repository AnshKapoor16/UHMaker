import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import openpyxl
from openpyxl.chart import ScatterChart, Reference, Series
from math import *

x10 = []

def calc(L,A,S,Lc,subzone):
    if(subzone == "1(a)"):
        tr = 1
        tp = round(0.257*(A**0.409)*(S**0.432),4) 
        tp_used = 0.5 + int(tp)
        qp = round(2.165*(tp_used**(-0.893)),4)
        W50 = round(2.654*(qp**(-0.921)),4)
        W75 = round(1.672*(qp**(-0.816)),4)
        WR50 = round(1.245*(qp**(-0.571)),4)
        WR75 = round(0.816*(qp**(-0.559)),4)
        TB = round(6.299*(tp_used**0.612),4)
        Tm = tp_used+(tr/2) 
        Qp = round(qp*A,4) 
    elif(subzone == "1(b)"):
        tr = 1
        tp = round(0.339*((L/(sqrt(S)))**0.826),4)
        tp_used = 0.5 + int(tp)
        qp = round(1.251*(tp_used**(-0.610)),4)
        W50 = round(2.215*(qp**(-1.034)),4)
        W75 = round(1.190*(qp**(-1.057)),4)
        WR50 = round(0.834*(qp**(-1.077)),4)
        WR75 = round(0.502*(qp**(-1.065)),4)
        TB = round(6.662*(tp_used**0.613),4)
        Tm = tp_used+(tr/2)
        Qp = round(qp*A,4) 
    elif(subzone == "1(c)"):
        tr = 1
        qp = round(1.331*((L/S)**(-0.492)),4)
        tp = round(2.195*(qp**(-0.944)),4)
        tp_used = 0.5 + int(tp)
        W50 = round(2.040*(qp**(-1.0265)),4)
        W75 = round(1.250*(qp**(-0.864)),4)
        WR50 = round(0.739*(qp**(-0.968)),4)
        WR75 = round(0.500*(qp**(-0.813)),4)
        TB = round(3.917*(tp_used**(0.990)),4)
        Tm = tp_used+(tr/2)
        Qp = round(qp*A,4)
    elif(subzone == "1(d)"):
        tr = 1
        tp = round(0.314*((L/sqrt(S))**1.012),4)
        tp_used = 0.5 + int(tp)
        qp = round(1.664/(tp_used**0.965),4)
        W50 = round(2.534/(qp**0.976),4)
        W75 = round(1.478/(qp**0.860),4)
        WR50 = round(1.091/(qp**0.750),4)
        WR75 = round(0.672/(qp**0.719),4)
        TB = round(5.526*(tp_used**0.866),4)
        Tm = tp_used+(tr/2)
        Qp = round(qp*A,4)
    elif(subzone == "1(e)"):
        tr = 2
        qp = round(2.030/((L/sqrt(S))**0.649),4)
        tp = round(1.858/( qp**1.038),4)
        tp_used = round(tp,0)
        W50 = round(2.217/(qp**0.990),4)
        W75 = round(1.477/(qp**0.876),4)
        WR50 = round(0.812/(qp**0.907),4)
        WR75 = round(0.606/(qp**0.791),4)
        TB = round(7.744 * (tp_used**0.779),4)
        Tm = tp_used+(tr/2)
        Qp = round(qp*A,4) 
    elif(subzone == "1(f)"):
        tr = 6
        qp = round(0.409/((L/sqrt(S))**0.456),4)
        tp = round(1.217/( qp**1.034),4)
        tp_used = round(tp,0)
        W50 = round(1.743/(qp**1.104),4)
        W75 = round(0.902/(qp**1.108),4)
        WR50 = round(0.736/(qp**0.928),4)
        WR75 = round(0.478 /(qp**0.902),4)
        TB = round(16.432*(tp**0.646),4)
        Tm = tp_used+(tr/2) 
        Qp = round(qp*A,4) 
    elif(subzone == "1(g) Hilly"):
        tr = 1
        tp = round(1.1808 *(((L*Lc)/sqrt(S))**0.285),4)
        tp_used = 0.5 + int(tp)
        qp = round(2.0972*(tp_used**(-0.927)),4)
        W50 = round(1.2622*(tp_used**0.828),4)
        W75 = round(0.7896*(tp_used**0.711),4)
        WR50 = round(0.5357*(tp_used**0.745),4)
        WR75 = round(0.3825*(tp_used**0.647),4)
        TB = round(5.5830*(tp_used**0.824),4)
        Tm = tp_used+(tr/2)
        Qp = round(qp*A,4) 
    elif(subzone == "1(g) Plain"):
        tr = 1
        qp = round(0.6617*((L/sqrt(S))**(-0.515)),4)
        tp = round(1.8833*(qp**(-0.940)),4)
        tp_used = 0.5 + int(tp)
        W50 = round(1.7897*(qp**(-1.006)),4)
        W75 = round(0.8955*(qp**(-1.061)),4)
        WR50 = round(0.5524*(qp**(-1.012)),4)
        WR75 = round(0.2984*(qp**(-1.012)),4)
        TB = round(12.4755*(tp_used**0.721),4)
        Tm = tp_used+(tr/2)
        Qp = round(qp*A,4) 
    elif(subzone == "2(a)"):
        tr = 1
        qp = round(2.272*((L*Lc/S)**(-0.409)),4)
        tp = round(2.164*(qp**(-0.940)),4)
        tp_used = 0.5 + int(tp)
        W50 = round(2.084*(qp**(-1.065)),4)
        W75 = round(1.028*(qp**(-1.071)),4)
        WR50 = round(0.856*(qp**(-0.865)),4)
        WR75 = round(0.440*(qp**(-0.918)),4)
        TB = round(5.428*(tp_used**0.852),4)
        Tm = tp_used+(tr/2)
        Qp = round(qp*A,4) 
    elif(subzone == "2(b)"):
        tr = 1
        qp = round((0.905*(A**(0.758))/A),4)
        tp = round(2.87*(qp**(-0.839)),4)
        tp_used = 0.5 + int(tp)
        W50 = round(2.304*(qp**-1.035),4)
        W75 = round(1.339*(qp**(-0.978)),4)
        WR50 = round(0.814*(qp**(-1.018)),4)
        WR75 = round(0.494*(qp**(-0.966)),4)
        TB = round(2.447*(tp_used**1.157),4) 
        Tm = tp_used+(tr/2)
        Qp = round(qp*A,4)
    elif(subzone == "3(a)"):
        tr = 1
        tp = round(0.433*((L/sqrt(S))**0.704),4)
        tp_used = 0.5 + int(tp)
        qp = round(1.161/(tp_used**0.635),4)
        W50 = round(2.284/(qp**1),4)
        W75 = round(1.331/(qp**0.991),4)
        WR50 = round(0.827/(qp**1.023),4)
        WR75 = round(0.561/(qp**1.037),4)
        TB = round(8.375*(tp_used**0.512),4)
        Tm = tp_used+(tr/2)
        Qp = round(qp*A,4)
    elif(subzone == "3(b)"):
        tr = 1
        tp = round(0.583*(((L*Lc)/sqrt(S))**0.302),4)
        tp_used = 0.5 + int(tp)
        qp = round(1.914*(tp_used**(-0.763)),4)
        W50 = round(1.849*(qp**(-0.976)),4)
        W75 = round(0.955*(qp**(-0.792)),4)
        WR50 = round(0.738*(qp**(-0.781)),4)
        WR75 = round(0.438*(qp**(-0.641)),4)
        TB = round(7.042*(tp_used**0.559),4)
        Tm = tp_used+(tr/2)
        Qp = round(qp*A,4)
    elif(subzone == "3(c)"):
        tr = 1
        tp = round(0.995*(((L*Lc)/sqrt(S))**0.2654),4)
        tp_used = 0.5 + int(tp)
        qp = round(1.665*(tp_used**-0.71678),4)
        W50 = round(1.9145*(qp**(-1.2582)),4)
        W75 = round(1.1102 *(qp**(-1.2088)),4)
        WR50 = round(0.7060*(qp**(-1.3859)),4)
        WR75 = round(0.45314*(qp**(-1.3916)),4)
        TB = round(5.04537*(tp_used**0.71637),4)
        Tm = tp_used+(tr/2)
        Qp = round(qp*A,4)
    elif(subzone == "3(d)"):
        tr = 1
        tp = round(1.757*(((L*Lc)/sqrt(S))**0.261),4)
        tp_used = 0.5 + int(tp)
        qp = round(1.260*(tp_used**(-0.725)),4)
        W50 = round(1.974*(qp**(-1.104)),4)
        W75 = round(0.961*(qp**(-1.125)),4) 
        WR50 = round(1.150*(qp**(-0.829)),4)
        WR75 = round(0.527*(qp**(-0.932 )),4)
        TB = round(5.411*(tp_used**0.826),4)
        Tm = tp_used+(tr/2)
        Qp = round(qp*A,4)
    elif(subzone == "3(e)"):
        tr = 1
        tp = round(0.727 *((L/sqrt(S))**0.59),4)
        tp_used = 0.5 + int(tp)
        qp = round(2.020/(tp_used**0.88),4)
        W50 = round(2.228/(qp**1.04),4)
        W75 = round(1.301/(qp**0.96),4)
        WR50 = round(0.880/(qp**1.01),4)
        WR75 = round(0.540/(qp**0.96),4)
        TB = round(5.485*(tp_used**0.73),4)
        Tm = tp_used + (tr/2)
        Qp = round(qp * A,4)  
    elif(subzone == "3(f)"):
        tr = 1
        tp = round(0.348*((L*Lc/sqrt(S))**0.454),4)
        tp_used = 0.5 + int(tp)
        qp = round(1.842*(tp_used**(-0.804)),4)
        W50 = round(2.353*(qp**(-1.005)),4)
        W75 = round(1.351*(qp**(-0.992)),4)
        WR50 = round(0.936*(qp**(-1.047)),4)
        WR75 = round(0.579*(qp**(-1.004)),4)
        TB = round(4.589*(tp_used**(0.894)),4)
        Tm = tp_used + (tr/2)
        Qp = round(qp * A,4)
    elif(subzone == "3(g)"):
        tr = 1
        tp = round(0.353*((L*Lc/sqrt(S))**0.45),4)
        tp_used = 0.5 + int(tp)
        qp = round(1.968*(tp_used**(-0.842)),4)
        W50 = round(2.30*(qp**(-1.018)),4)
        W75 = round(1.356*(qp**(-1.007)),4)
        WR50 = round(0.95*(qp**(-1.078)),4)
        WR75 = round(0.58*(qp**(-1.035)),4)
        TB = round(4.572*(tp_used**0.90),4)
        Tm = tp_used + (0.5*tr)
        Qp = round(qp * A,4)        
    elif(subzone == "3(h)"):
        tr = 1
        tp = round(0.325*((L*Lc/sqrt(S))**0.447),4)
        tp_used = 0.5 + int(tp)
        qp = round(0.996*(tp_used**(-0.497)),4)
        W50 = round(2.389*(qp**(-1.065)),4)
        W75 = round(1.415*(qp**(-1.067)),4)
        WR50 = round(0.753*(qp**(-1.229)),4)
        WR75 = round(0.558*(qp**(-1.088)),4)
        TB = round(7.392*(tp_used**0.524),4)
        Tm = tp_used + (tr/2)
        Qp = round(qp*A,4)
    elif(subzone == "3(i)"):
        tr = 1
        tp = round(0.553*((L*Lc/sqrt(S))**0.405),4)
        tp_used = 0.5 + int(tp)
        qp = round(2.043/(tp_used**0.0872),4)
        W50= round(2.197/(qp**1.067),4)
        W75= round(1.325/(qp**1.088),4)
        WR50= round(0.799/(qp**1.138),4)
        WR75= round(0.536/(qp**1.109),4)
        TB= round(5.083/(tp_used**0.733),4)
        Tm= tp_used + (tr/2)
        Qp = round(qp*A,4)
    elif(subzone == "4(a), (b) & (c)"):
        tr = 1
        tp = round(0.376*((L*Lc/sqrt(S))**0.434),4)
        tp_used = 0.5 + int(tp)
        qp = round(1.215 /(tp_used**0.691),4)
        W50 = round(2.211 / (qp**1.07),4)
        W75 = round(1.312 / (qp**1.003),4)
        WR50 = round(0.808 /(qp**1.053),4)
        WR75 = round(0.542/(qp**0.965),4)
        TB = round(7.621*(tp_used**0.623),4)
        Tm = tp_used + (tr/2)
        Qp = round(qp * A,4)
    elif(subzone == "5(a) & 5(b)"):
        tr = 1
        qp = round(0.9178*((L/S)**(-0.4313)),4)
        tp = round(1.5607*(qp**(-1.0814)),4)
        tp_used = 0.5 + int(tp)
        W50 = round(1.925*(qp**(-1.0896)),4)
        W75 = round(1.0189*(qp**(-1.0443)),4)
        WR50 = round(0.5788*(qp**(-1.1072)),4)
        WR75 = round(0.3469*(qp**(-1.0538)),4)
        TB = round(7.380*(tp_used**0.7343),4)
        Tm = tp_used+(tr/2)
        Qp = round(qp*A,4)
    elif(subzone == "7"):
        tr = 1
        tp = round(2.498 * (((L*Lc)/S)**0.156),4)
        tp_used = 0.5 + int(tp)
        qp = round(1.048 * (tp_used**(-0.178)),4)
        W50 = round(1.954 * (((L*Lc)/S)**0.099),4)
        W75 = round(0.972 * (((L*Lc)/S)**0.124),4)
        WR50 = round((0.189 * (W50**1.769)),4)
        WR75 = round(0.419 * (W75**1.246),4)
        TB = round(7.845 * (tp_used**0.453),4)
        Tm = tp_used + (tr/2)
        Qp = round(qp * A,4) 

    set_values(L,A,S,Lc, subzone, tr, tp, tp_used, qp, W50, W75, WR50, WR75, TB, Tm, Qp)

def set_values(L, A, S, Lc, subzone, tr, tp, tp_used, qp, W50, W75, WR50, WR75, TB, Tm, Qp):
    global x10
    x = [-1, 0, round(Tm-WR50,2), round(Tm-WR75,2), round(Tm,2), round(Tm-WR75+W75,2), round(Tm-WR50+W50,2), int(TB)+1,int(TB)+2]
    y = [-1, 0, round(Qp/2,2), round(Qp*0.75,2), round(Qp,2), round(Qp*0.75,2), round(Qp/2,2), 0,-1]
    x10 = [ (f"{tr} hr UNIT HYDROGRAPH as per SUBZONE {subzone}",""),
            (),
            ("S.No","Description", "Symbol", "Value", "Unit", "Rounded-off Value"),
            (1,"Length of Main stream","L",L, "Km"),
            (2,"Catchment Area","A",A, "Sq. Km"),
            (3,"Slope of River","S",S, "m/Km"),
            (4,"Length between Centroid of area & Gauge Site","Lc",Lc, "Km"),
            (5,"Duration of Unit hydrograph"," ",tr, "hrs"),			
            (6,"Enhancement in Peak discharge"," "," ", " "),			
            (7,"Time of Peak","tp",tp, "hrs",tp_used,"","","","Time(hr)","Discharge(Cumecs)"),
            (8,"Peak discharge of Unit Hydrograph","qp",qp, "Cumec/Sq. Km","","","","",x[1],y[1]),
            (9,"Width of UG measure at 50% peak discharge","W50",W50, "hrs","","","","",x[2],y[2]),
            (10,"Width of UG measure at 75% peak discharge","W75",W75, "hrs","","","","",x[3],y[3]),
            (11,"Width of the rising side of UG measured at 50% of peak discharge","WR50",WR50, "hrs","","","","",x[4],y[4]),
            (12,"Width of the rising side of UG measured at 75% of peak discharge","WR75",WR75, "hrs","","","","",x[5],y[5]),
            (13,"Base width of Unit Hydrograph","TB",TB, "hrs", int(TB)+1,"","","",x[6],y[6]),
            (14,"Time from the start of rise to the peak of UG","Tm",Tm, "hrs","","","","",x[7],y[7]),
            (15,"Peak Discharge of Unit Hydrograph (cumecs)","Qp",Qp, "Cumec"),
            (),
            ("","CHECK =",round(A/0.36,4),"Round-off =",round(A/0.36)),
            (),
            (" ", " ", "Time (in hrs)", "Discharge (in cumec)")]
    check = round(A/0.36)
    draw_graph(x,y,check)
    


def draw_graph(x,y,check):
    def valuecorrection(m):
        m[0]=0
        m[(len(m)-1)]=0
        j=max(m)
        u=j
        m[int(x[4])] = max(y)
        for i in range(1,len(m)):
            if(m[i]<0):
                m[i]=0
        
        for i in range(m.index(max(m))-1,int(round(x[2],0)),-1):
            avgdiff = ((j- m[i])/m[i])*100
            j=m[i]
            if(avgdiff<0):
                m[i] = m[i+1]/((avgdiff/100)+1)
        
            elif(avgdiff==0):
                break
            
            else:
                m[i] = m[i+1]/((avgdiff/100)+1)

        j=u
        for i in range(m.index(max(m))+1,int(round(x[-2],0))):

            avgdiff = ((j- m[i])/m[i])*100
            j=m[i]
            
            if(avgdiff<0):
                m[i] = m[i-1]/((avgdiff/100)+1)

            elif(avgdiff==0):
                break
            
            else:
                m[i] = m[i-1]/((avgdiff/100)+1)

        diff = np.sum(m) - check
        valtsub = diff/(len(m)-2)
        while(round(valtsub,2)!=0):
            for i in range(1,len(m)-1):
                if(i in x):
                    pass
                elif(m[i]==0):
                    m[i] += valtsub
                else:
                    m[i] -= valtsub
                    if(m[i]<=0):
                        m[i] += valtsub
            diff = np.sum(m) - check
            valtsub = diff/(len(m)-2)

    s=interpolate.PchipInterpolator(x,y)

    xnew=np.linspace(0,int(x[-2]),1000)
    ynew=s(xnew)

    xp=np.linspace(-1,int(x[-1]),int(x[-1])+2)
    yp=[]
    for i in xp:
        yp.append(np.round_(s.__call__(i),decimals=2))
    l=interpolate.UnivariateSpline(xp,yp,k=3)
    y2=l(xnew)

    i=0

    if round(l.integral(0,x[-2]),2) > check:
        while round(l.integral(0,x[-2]),2) > check and i<50000:
            l.set_smoothing_factor(i)
            y2=l(xnew)
            np.round_(y2,decimals=2)
            i=i+10
            
    else:
        while round(l.integral(0,x[-2]),2) < check and i<50000:
            l.set_smoothing_factor(i)
            y2=l(xnew)
            np.round_(y2,decimals=2)
            i=i+10

    for i in range(1,len(x)-1):
        if((abs(l.__call__(x[i])-y[i])/y[i])*100 > (y[i]*0.2)):
            l.set_smoothing_factor(0)


    x7=np.linspace(0,int(x[-2]),int(x[-2])+1)
    y7=[]
    for i in x7:
        y7.append(l.__call__(i))

    valuecorrection(y7)

    n=interpolate.InterpolatedUnivariateSpline(x7,y7,k=3)
    y10=n(xnew)
    plt.plot(xnew,y10)

    for i in range(0,len(y7)):
        global x10
        x10.append((" ", " ", x7[i],np.round_(y7[i],decimals=2)))


def export_to_excel(rows, name):
    wb = openpyxl.Workbook()
    
    sheet = wb.active

    sheet.column_dimensions['B'].width = 61
    sheet.column_dimensions['E'].width = 12
    sheet.column_dimensions['F'].width = 16

    for row in rows:
        sheet.append(row)
    
    chart = ScatterChart()
    
    xvalues = Reference(sheet, min_col = 3,
                        min_row = 23, max_row = len(rows))
                        
    yvalues = Reference(sheet, min_col = 4,
                        min_row = 23, max_row = len(rows))

    series = Series(values = yvalues, xvalues = xvalues, title = "Smoothened")
    
    chart.series.append(series)
    
    chart.title = " UNIT HYDROGRAPH "
    
    chart.x_axis.title = " Time(in hrs) "
    
    chart.y_axis.title = " Discharge(in cumec) "

    sheet.add_chart(chart, "G23")
    
    wb.save(f"{name}.xlsx")



