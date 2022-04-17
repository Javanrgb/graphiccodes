import matplotlib.pyplot as plt
print(" Input for Coordinates and Radius")
rx = int(input("Enter the value of radius X:"))
ry = int(input("Enter the value of radius Y:"))
x = int(input("Enter the value of X:"))
y = int(input("Enter the value of Y:"))

x1=x
y1=ry
P1= ((ry * ry)-(rx * rx * ry) +(0.25 * rx * rx))
dx = 2 * ry *ry * x1
dy = 2 * rx * rx * y1
x1_ = []
y1_ = []
x2_ = []
y2_ = []
print( P1, dx, dy)
while dx < dy:

    if P1 < 0:  # If Decision Parameter(p1) < 0

        print("\nDecision Parameter:\t", P1)
        print("Coordinates:\t({},{})".format((x1+1), (y1)))
        x1 = x1 + 1
        y1 = y1
        x1_.append(x1)
        y1_.append(y1)
        dx = dx + (2 * ry * ry)
        P1 = P1 + dx + (ry * ry)



        # If Decision Parameter(P) > 0

    else:
        print("\nDecision Parameter:\t", P1)
        print("Coordinates:\t({},{})".format((x1 + 1), (y1 - 1)))
        x1 = x1 + 1
        y1 = y1 - 1
        x1_.append(x1)
        y1_.append(y1)

        dx = dx + (2 * ry * ry)
        dy = dy - (2 * rx* rx)
        P1 = P1 + dx -dy + (ry * ry)

        print(x1_,y1_)
        x2_ = []
        y2_ = []
        x2_ = [-x for x in x1_]
        y2_ = [-y for y in y1_]
        print(x2_, y2_)

plt.plot(x1_, y1_, color='blue', marker='o', linestyle='-', linewidth=1, markersize=4)
plt.plot(x2_, y1_, color='blue', marker='o', linestyle='-', linewidth=1, markersize=4)
plt.plot(x1_, y2_, color='blue', marker='o', linestyle='-', linewidth=1, markersize=4)
plt.plot(x2_,y2_, color='blue', marker='o', linestyle='-', linewidth=1, markersize=4)
#plt.plot(y1_, x1_, color='blue', marker='o', linestyle='-', linewidth=1, markersize=4)
#plt.plot(y2_, x1_, color='blue', marker='o', linestyle='-', linewidth=1, markersize=4)
#plt.plot(y2_, x2_, color='blue', marker='o', linestyle='-', linewidth=1, markersize=4)
#plt.plot(y1_, x2_, color='blue', marker='o', linestyle='-', linewidth=1, markersize=4)
plt.grid(True)
plt.show()
