#!C:\Program Files\Python310\python.exe
print("content-type: text/html\n\n" )


import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append(r'''C:\Users\tyree\AppData\Roaming\Python\Python310\site-packages''')

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot