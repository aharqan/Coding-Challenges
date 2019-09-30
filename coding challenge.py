x=input()
y=input()
x=x.split()
y=y.split()
finalList=[]
countX=0
countY=0
if int(x[0])>int(y[0]):
	countX+=1
if int(x[0])<int(y[0]):
	countY+=1
if int(x[0])==int(y[0]):
	countX+=0
	countY+=0
if int(x[1])>int(y[1]):
	countX+=1
if int(x[1])<int(y[1]):
	countY+=1
if int(x[1])==int(y[1]):
	countX+=0
	countY+=0
if int(x[2])>int(y[2]):
	countX+=1
if int(x[2])<int(y[2]):
	countY+=1
if int(x[2])==int(y[2]):
	countX+=0
	countY+=0
finalList.append(countX)
finalList.append(countY)
print(finalList[0],finalList[1])
