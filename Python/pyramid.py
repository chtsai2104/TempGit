import sys

if len(sys.argv) < 2:
	print 'no argument'
	sys.exit()

n = int(sys.argv[1]) + 1

print ord(sys.argv[2])

for i in range(n):
	print ' ' * (n - i), "{} ".format(sys.argv[2]) * (i - 1)
for i in range(n):
	print ' ' * (n - i), chr(ord(sys.argv[2])+(i-1)) * (2 * i - 1)