#!/usr/bin/env python
# coding: utf-8

# In[1]:


#get_ipython().run_line_magic('matplotlib', 'widget')
#get_ipython().run_line_magic('matplotlib', 'widget')


# In[2]:


"""Set custom lights to a 3D scene"""
from vedo import *
import matplotlib.pyplot as plt

import matplotlib

matplotlib.use('module://ipympl.backend_nbagg')


man = Mesh(dataurl+'man.vtk').c('white').lighting('glossy')

p1 = Point([1,0,1], c='y')
p2 = Point([0,0,2], c='r')
p3 = Point([-1,-0.5,-1], c='b')
p4 = Point([0,1,0], c='k')

# Add light sources at the given positions
l1 = Light(p1, c='y') # p1 can simply be [1,0,1]
l2 = Light(p2, c='r')
l3 = Light(p3, c='b')
l4 = Light(p4, c='w', intensity=0.5)

#show(man, l1, l2, l3, l4, p1, p2, p3, p4, __doc__, axes=1, viewup='z')



#####################################################
##### Equivalent code using a Plotter instance: #####
#####################################################

#fig, ax = plt.subplots()
#ax.plot([1,2,3], [4,3,2])
#fig.show()

plt.figure
plt = Plotter(axes=1)
plt += [man, p1, p2, p3, p4, l1, l2, l3, l4]
plt.show(viewup='z')
#####################################################


# In[ ]:





# In[ ]:




