def hanoi(n,s,t,b):
	assert n > 0
	if n == 1:
		print 'move', s, 'to', t
	else:
		hanoi(n-1,s,b,t)
		hanoi(1,s,t,b)
		hanoi(n-1,b,t,s)

for i in range(1,5):
	print 'New Hanoi Example: hanoi(', i, ', source, target, buffer)'
	print '-----------------------------------------------------'
	hanoi(i, 'Left', 'Centre', 'Right')
	print '-----------------------------------------------------'