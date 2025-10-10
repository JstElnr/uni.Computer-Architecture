import matplotlib.pyplot as plt
labels=['SISD','SIMD','MISD','MIMD']
values=[1,4,1,4]
plt.bar(labels,values,color=['blue','green','orange','red'])
plt.title("Flynn's Taxonomy - Parallelism levels")
plt.ylabel("Relative Parallelism Power")
plt.grid(True,axis='y',linestyle='--',alpha=0.5)
plt.show()