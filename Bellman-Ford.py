# Suppose the graph has vertices v_0, v_1,...,v_n. W[i][j] is the weight of the directed edge from v_i to v_j, 
# defined to be 0 when i=j and infinity if there is no such edge.

import math

def bf(W):
	n=len(W)-1
	lst=[0]
	for i in range(n):
		lst.append(math.inf)
	counter=0
	while counter<n:
		for i in range(n+1):
			for j in range(n+1):
				if lst[i]+W[i][j]<lst[j]:
					lst[j]=lst[i]+W[i][j]
		counter+=1
	return lst

# Testing using the example from https://www.youtube.com/watch?v=obWXjtg0L64

W=[[0,10,math.inf,math.inf,math.inf,8],
   [math.inf,0,math.inf,2,math.inf,math.inf],
   [math.inf,1,0,math.inf,math.inf,math.inf],
   [math.inf,math.inf,-2,0,math.inf,math.inf],
   [math.inf,-4,math.inf,-1,0,math.inf],
   [math.inf,math.inf,math.inf,math.inf,1,0]]

print(bf(W))

print("gf")

