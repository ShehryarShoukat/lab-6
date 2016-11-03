import random
#function that calls recursion
def recursioncall(info,e,switchtime,n): 
	return min(recursivefun(info,e,switchtime,n-1,0)+e[0],recursivefun(info,e,switchtime,n-1,1)+e[1],recursivefun(info,e,switchtime,n-1,2)+e[2])

#recursive function
def recursivefun(info,e,switchtime,n,i):
	if (n <=1):
		return (e[i]+info[i][1]) 
	else:	
		return min(recursivefun(info,e,switchtime,n-1,0)+e[0],recursivefun(info,e,switchtime,n-1,1)+e[1],recursivefun(info,e,switchtime,n-1,2)+e[2])
#calling the problem
def assemblyline(n):
	#random initialization of lane x staion array
	info = [[random.randint(1,10) for i in range(0,3)] for j in range(n)] 
	switchtime = 1
	#time to box
	boxtime = [random.randint(1,5) for i in range(0,3)]
	#return from the recursion
	return recursioncall(info,boxtime,switchtime,n)
	
print assemblyline(10)
