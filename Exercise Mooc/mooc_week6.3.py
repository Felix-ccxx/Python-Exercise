import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,1)
y=np.sin(4*np.pi*x)*np.exp(-5*x)
plt.plot(x,y,'r--')
plt.title('Matplotlib Graphic Attribute')
plt.xlabel('linespace')
plt.ylabel('SIN')
plt.show()
