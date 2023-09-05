print("input the fllowing")
print("enter pi measurements")
pi=float(input())
print("enter the radius")
rad=int(input())
print("enter the height")
height=int(input())

#sa of closed cylinder
# 2 pi r2 + 2pi dh
surf_area=2*(pi*rad*rad)+pi*(rad+rad)*height
print("the SA is ",surf_area)

#open cylinder
# pi r2 + pi dh
open=(pi*rad*rad)+pi+(rad *2)* height
print(" The surface area of the tank is ", open)

# Pipe
# pi d h
pipe = pi * (rad *2) * height
print(" The surface area of the pipe is ", pipe)