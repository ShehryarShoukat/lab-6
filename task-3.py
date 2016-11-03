import random
n_STATION = 100000
def carAssembly(a, t, x , e):
    T1=[]
    T2=[]
    T3=[]
    for x1 in xrange(0,n_STATION):
        T1.append(0)
        T2.append(0)
        T3.append(0)
    
    i=0
    T1[0] = e[0] + a[0][0] #e[0] is starting time of line 1
    T2[0] = e[1] + a[0][1] #e[1] is starting time of line 2
    T3[0] = e[2] + a[0][2] #e[2] is starting time of line 3
    
    for i in range(1,n_STATION):
        T1[i] = min(T1[i-1] + a[i][0], T2[i-1] + t[i][1] + a[i][0], T3[i-1] + t[i][2] + a[i][0])
        T2[i] = min(T2[i-1] + a[i][1], T1[i-1] + t[i][0] + a[i][1], T3[i-1] + t[i][2] + a[i][1])
        T3[i] = min(T3[i-1] + a[i][2], T1[i-1] + t[i][0] + a[i][2], T2[i-1] + t[i][1] + a[i][2])
    time1 = T1[n_STATION-1] + x[0] #x[0] is leaving time of line 1
    time2 = T2[n_STATION-1] + x[1] #x[1] is leaving time of line 2
    time3 = T3[n_STATION-1] + x[2] #x[2] is leaving time of line 3
    
    
    return min( time1 , time2 ,time3)
	
a =  [[random.randint(1,10) for i in range(0,3)] for j in range(0,n_STATION)] # station costs

t =  [[random.randint(1,10) for i in range(0,3)] for j in range(0,n_STATION)] # station time

e=[]
e.append(random.randint(1,15)) 
e.append(random.randint(1,15)) 
e.append(random.randint(1,15)) 
x=[]
x.append(random.randint(1,15)) 
x.append(random.randint(1,15)) 
x.append(random.randint(1,15)) 

print carAssembly(a, t, x , e)
 
  