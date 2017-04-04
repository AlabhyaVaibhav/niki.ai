import math
def factors(num):
	flag = 0
	if num < 100000:
		for x in range(2,int((math.sqrt(num)))+1):
			if num%x==0: 
			    if num/x == x:
				    print(x)
				    flag = flag + 1
			    else:
			        print(x) 
			        print (num/x)
			        flag = flag + 1
		if flag < 3:
		    print ("Prime Number")
