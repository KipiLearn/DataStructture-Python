def TOH(n,a,b,c):
	if n>0:
		TOH(n-1,a,c,b)
		print("From",a,"To",c)
		TOH(n-1,b,a,c)
n=3 #no. of disk
TOH(n,'A','B','C') # A,B,C name of rods