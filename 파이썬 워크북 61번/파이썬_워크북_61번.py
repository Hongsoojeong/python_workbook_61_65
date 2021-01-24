#연습 61번
n=0
total=0
while True:
   num=int(input("숫자를 입력해주세요: "))
   if num==0:
       break
   n=n+1
   total+=num
print("평균은 {}입니다".format(total//n))


#연습 62번
origianl_price=[4.95,9.95,14.95,19.95,24.95]
sale_price=list([i*(0.6) for i in origianl_price])
for j in range(len(sale_price)):
    print("원래 가격은 {:.2f}달러 이고, 할인된 가격은 {:.2f}달러입니다.".format(origianl_price[j],sale_price[j]))


#연습 63번
F=int(input("화씨 온도를 입력해주세요(F): "))
C=(F-32)//1.8
print("섭씨 온도는 {}ºC 입니다.".format(C))



#연습 64번
#(페니가 센트보다 단위가 더 작은거네) 가장 가까운 니켈로 반올림한대. 5로 나눴을 때 2.5이하면 반올림 ㄴㄴ

import math
total_price=0
while True:
    price=(input("총 금액을 입력해주세요(페니 단위): "))
    if price!="":
        total_price+=float(price)
    else:
        break
penny=total_price/5
if penny<2.5:
    penny=math.floor(penny)
else:
    penny=round(penny)
print("카드로 계산할 경우 지불해야할 금액은 {}센트 입니다.".format(total_price))
print("변환된 금액은 {}니켈이므로, 현금으로 계산할 경우 {}센트를 더 지불해야합니다.".format(penny,(total_price-(penny)*5)))






#연습 65번
#(좌표를 찍어야되네)

import math

coordinate_x=[]
coordinate_y=[]

first_x=int(input("Enter the x part of the coordinate: "))
first_y=int(input("Enter the y part of the coordinate: "))

coordinate_x.append(first_x)
coordinate_y.append(first_y)


while True:
      add_x=input("Enter the x part of the coordinate: (blank to quit): ")
      if add_x=="":
         break
      else:
          add_x=int(add_x)
          coordinate_x.append(add_x)
          add_y=int(input("Enter the y part of the coordinate: "))
          coordinate_y.append(add_y)


# x좌표의 리스트, y좌표의 리스트를 따로 만들어주었음. 이제 for문을 사용해서 하면 된다.



total_polygon=0

for i in range(0,len(coordinate_y)-1):
    dis=math.sqrt((coordinate_x[i+1]-coordinate_x[i])**2+(coordinate_y[i+1]-coordinate_y[i])**2)
    total_polygon+=dis
last=len(coordinate_x)-1
dis=math.sqrt((first_x-coordinate_x[last])**2+(first_y-coordinate_y[last])**2)
total_polygon+=dis
print("The perimeter of that polygon is %f"%total_polygon)