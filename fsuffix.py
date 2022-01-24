arr=['xyzp','lmzp','pqzp']
s=''
for i in range(len(arr)):
	x=arr[i]
	for j in range(i+1,len(arr)):
		y=arr[j]
		for k in range(len(x)):
			if x[k]==y[k]:
				if x[k] not in s:
					s=s+x[k]
		break
					
print(s)