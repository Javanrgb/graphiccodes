# Brensenham's algorithm
#!/usr/bin/python3
import matplotlib.pyplot as plt

print("Enter values for endpoints below:")
x1 = int(input("Input value for x1:\n"))
y1 = int(input("Input value for y1:\n"))
x2 = int(input("Input value for x2:\n"))
y2 = int(input("Input value for y2:\n"))



x = x1
y = y1

dx = x2 - x1
dy = y2 - y1
grad = dy/dx

print("Display Change in x (dx):\n\t",dx)
print("Display Change in Y (dy):\n\t",dy)


# Decision parameter- obtaining starting value

print("Gradient is",grad)

# display list of points

x_point = []
y_point = []
x_ = []
y_ = []
p1 = []

if grad == 0:
    try:
        print("Gradient is",grad)
    except ZeroDivisionError:
        print("With a zero gradient,gradient is",grad)
        plt.plot(x_,y_,linewidth=0.8,color='g')
    
    

elif grad < 1:
    p0 = 2*dy - dx
    #p0 = 2*dy - dx

    print("Starting Value p0:", p0, "\n")
    for i in range(dx):
        x_point.append(x)
        y_point.append(y)

        if(p0 < 0):
            x = x + 1
            y = y
            p0 = p0 + 2*dy
            x_.append(x)
            y_.append(y)
            p1.append(p0)
        else:
          x = x + 1
          y = y + 1
          p0 = p0 + 2*dy - 2*dx
          x_.append(x)
          y_.append(y)
          p1.append(p0)
    print(p1)
    print(x_, y_)
    
    plt.plot( x_,y_, marker = 'o')
    #plt.plot([x1,y1],[x2,y2])
    plt.show()
elif grad > 1:
    p0 = 2*dx - dy
   # p0 = 2*dy - dx

    print("Starting Value p0:", p0, "\n")
    for i in range(dy):
        x_point.append(x)
        y_point.append(y)
    
        if(p0 == 0):
            x = x +1
            y = y +1
            p0 = p0 - (2*dy - 2*dx)
            x_.append(x)
            y_.append(y)
            p1.append(p0)
        elif(p0 < 0):
             x = x 
             y = y +1
             p0 = p0 + 2*dx
             x_.append(x)
             y_.append(y)
             p1.append(p0)
        elif(p0 > 0 ):
            x = x +1
            y = y + 1
            p0 = p0 + (2*dx -2*dy)
            x_.append(x)
            y_.append(y)
            p1.append(p0)
    print(p1)
    print(x_, y_)
        
    plt.plot( x_,y_, marker = 'o')
    plt.show()
    
if grad == (-grad):
    p0 = 2*dy + dx
    #p0 = 2*dy - dx

    print("Starting Value p0:", p0, "\n")
    for i in range(dx):
        x_point.append(x)
        y_point.append(y)

        if(p0 < 0):
            x = x + 1
            y = y - 1
            p0 = p0 + 2*dy
            x_.append(x)
            y_.append(y)
            p1.append(p0)
        elif(p0 == 0):
          x = x + 1
          y = y - 1
          p0 = p0 - 2*dy
          x_.append(x)
          y_.append(y-1)
          p1.append(p0)
          if(p0 > 0):
              x = x + 1
              y = y - 1 
              p0 = p0 - 2*dy
              x_.append(x)
              y_.append(y-1)
              p1.append(p0)
    print(p1)
    print(x_, y_)
    
    plt.plot( x_,y_, marker = 'o')
    plt.show()
