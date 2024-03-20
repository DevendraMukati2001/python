import numpy as np
import matplotlib.pyplot as pl
ar2=[1,7,21,35,35,21,7,1]
s1=np.sin(ar2)
s2=np.cos(ar2)
s3=np.tan(ar2)
pl.plot(ar2,s1,"c")
pl.plot(ar2,s2,"r")
pl.plot(ar2,s3,"k",linestyle="dashed")
pl.show()