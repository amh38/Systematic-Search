from sbb import SBB
from algorithms import *
sbb = SBB()
sbb.importData('linie-mit-betriebspunkten.json')


# The object sbb contains know all the hubs and trainlines. We can visualize the hubs with matplotlib:

# In[11]:


# import matplotlib.pyplot as plt
#
# def plot_hubs(hubs, labelNames = False):
#     fig = plt.figure(figsize=(10,10))
#     x =[]; y = []; names = [];
#     for h in hubs:
#         new_x = hubs[h].x
#         new_y = hubs[h].y
#         x.append(new_x)
#         y.append(new_y)
#         if labelNames:
#             plt.text(new_x+0.01, new_y+0.01, h, fontsize=9)
#     plt.scatter(x,y, marker='.', color='black')
#     plt.axis('equal')
#
# plot_hubs(sbb.hubs)


# With a little imagination and geographic knowledge you can recognize the different regions of Switzerland.
#
# We want to implement a search algorithm that finds the shortest way between 'Rotkreuz' and 'Thalwil'. In this exercise, we are not restricted to the official train lines. We can use the railway system with our own search agent and decide at each hub in which direction we want to go. If you have successfully implemented the classes above, the following code should execute and provide the directions between Rotkreuz and Zermatt.

# In[13]:


start = 'Rotkreuz'
goal = 'Thalwil'
sbb_map = UndirectedGraph(sbb.createMap())
problem = GraphProblem(start, goal, sbb_map)
node = deapth_first_graph_search(problem)
print_info_about_search(node)
