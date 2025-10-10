import matplotlib.pyplot as plt
import pandas as pd
data={
    "years":[1978,1980,1982,1984,1986,1988,1990,1992,1994,1996,1998,2000,2002,2004,2006,2008,2010,2012,2014,2016,2018],
    "performance":[1, 2, 3.5, 7, 14, 30, 60, 120, 250, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000, 1000000]
}
df=pd.DataFrame(data)
plt.figure(figsize=(9,5))
plt.plot(df["years"],df["performance"],marker='o',color='purple',linewidth=2,label="Processor performance (vs. Vax-11/780)")
plt.yscale("log")
plt.title("Moore's Law - Processor Performance Growth",fontsize=14,fontweight='bold')
plt.xlabel("Year")
plt.ylabel("Relative Performance (log scale)")
plt.grid(True,which="both",linestyle="--",linewidth=0.6,alpha=0.7)
plt.legend()
for x,y in zip(df["years"][::3],df["performance"][::3]):
    plt.text(x,y*1.2,f"{y:,}",ha='center',fontsize=8,color='gray')

plt.tight_layout()
plt.show()