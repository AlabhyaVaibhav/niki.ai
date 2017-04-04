def cipher(m,n):
	alpha_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	if m<n:
		if m<=26 and n <=26:
			for x in range(m-1,n):
				print(alpha_list[x])
		elif m <=26 and n >=26:
			while m<=26:
				print (alpha_list[m-1])
				m=m+1
			m=m-1
			for x in range(m,n+1):
			  fa=int(x/26)
			  sa=int(x-(26*fa))
			  print(alpha_list[int(fa-1)] + alpha_list[int(sa)])
		elif m>26 and n>26:
			for x in range(m-1,n):
				fa=int(x/26)
				sa=int(x-(26*fa))
				print(alpha_list[int(fa-1)] + alpha_list[int(sa)])

