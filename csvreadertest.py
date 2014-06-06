import csv

with open('fw-policy.csv', 'rb') as csvfile:
	r = csv.reader(csvfile)
	p = [0,0]
	i = 0
	for row in r:		
		p[i] = row
		i = i + 1
	print p

