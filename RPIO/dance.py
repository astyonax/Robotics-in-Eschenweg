import PIBOT as PB

try:
	PB.forw(1)
	PB.left(1)
	PB.back(1)
	PB.right(1)
	PB.right_fast(4)
except KeyboardInterrupt:
	PB.reset()

