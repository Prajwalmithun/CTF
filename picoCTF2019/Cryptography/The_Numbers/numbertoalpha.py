#! /bin/python3

alphabets = "0,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"

ar_alphabetsalphabets = alphabets.split(',')

inp = input("Enter the numbers with spaces in between \n")

res = []

for x in inp.split(' '):
	res.append(ar_alphabetsalphabets[int(x)])

print("".join(res).upper())
