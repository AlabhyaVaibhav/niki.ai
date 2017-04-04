def cipher(m,n):
	alpha_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	if m<n:
		if m<=26 and n <=26:
			for x in range(m,n):
				print(alpha_list[x])
		elif m <=26 and n >=26:
			while m<=26:
				print(alpha_list[m])
				m=m+1
			for x in range(m,n):
				fa=x/26
				sa=x-(26*fa)
				print(alpha_list[fa],alpha_list[sa])
		elif m>26 and n>26:
			for x in range(m,n):
				fa=x/26
				sa=x-(26*fa)
				print(alpha_list[fa],alpha_list[sa])