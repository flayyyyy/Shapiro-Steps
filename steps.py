import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['mathtext.fontset']='stix'
matplotlib.rcParams['font.family']='STIXGeneral'

f=18
plt.figure(figsize=(8,6))
for k in (0,2.5):
    Ic=2
    I1=k
    omega=1
    R=1
    if k==0:
        C=0.2
    else:
        C=0.6
    I0_values=np.linspace(-5, 5, 1000)

    def RCSJ(t, y, I0):
        phi, v=y
        dphi=v
        dv=(I0 + I1*np.sin(omega*t) - Ic*np.sin(phi) - v/R) / C
        return [dphi, dv]
    V_avg_list=[]
    for I0 in I0_values:
        sol=solve_ivp(lambda t, y: RCSJ(t, y, I0),
                        [0, 500], [0.0, 0.0],
                        t_eval=np.linspace(0, 500, 40000), method="RK45")
        phi=sol.y[0]
        v=sol.y[1]
        cut=int(0.7 * len(v))
        V_avg=np.mean(v[cut:])
        V_avg_list.append(V_avg)
    if k==0:
        plt.plot(V_avg_list, I0_values, lw=2,color='red',linestyle='--',label="witout RF")
    else:
        plt.plot(V_avg_list, I0_values, lw=2,color='black',label="with RF")
plt.ylabel("$I_{DC}$",fontsize=f)
plt.xlabel("$V_{DC}$",fontsize=f)
plt.xticks(np.arange(-5,6,1),fontsize=f)
plt.yticks(np.arange(-5,6,1),fontsize=f)
plt.xlim(-5.5,5.5)
plt.ylim(-5.5,5.5)
plt.legend(loc="best", fontsize=f, frameon=True)
plt.grid(True, linestyle='--', linewidth=0.4, alpha=0.6)
plt.tight_layout()
plt.show()
