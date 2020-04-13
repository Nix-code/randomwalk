from randomwalk import RandomWalk
import matplotlib.pyplot as plt
#storing class in an object
while True:
    r=RandomWalk(50000)#increases the points
    r.fill_walk()
    point_numbers=list(range(r.num_points))
    #list is made to store the walks in it in order to color it individually
    plt.scatter(r.x_values,r.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=1)

    """let's emphasize the first and last element in order to make it easy to understand"""
    plt.scatter(0,0,c='green',edgecolor='none',s=100)
    #0,0 means starting point of x and y (x,y)
    plt.scatter(r.x_values[-1],r.y_values[-1],c='red',edgecolor='none',s=100)
    #[-1] [-1]means last stored value of (x,y) as 0,0 has already used for starting point green
    #so [-1] is the ending red value,
    #deleting the label of axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
   # plt.figure(figsize=(10,6))
    plt.show()
    x=input("Continue:>>>> Y/N")
    if x=="N" or x=="n":
        break
