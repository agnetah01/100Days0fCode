# calculate area,sa and volume of a cuboid
print("length")
len=int(input())
print("width")
wid=int(input())
print("height")
hgt=int(input())

 #area
 #sa=2lw+2lh+2hw
area=2*(len*wid)+ 2*(len*hgt)+2*(wid*hgt)
print(area)
 
 #vol
vol=len*wid*hgt
print(vol)

#perimeter
per=4*(len+wid+hgt)
print(per)