
from collections import defaultdict

class MissingHelper(object):
	def __init__(self):
		self.count = 0

	def __call__(self):
		self.count += 1
		return 0

current = {'red':1, 'blue':5, 'yellow':-1}
increment = [('green',5.5), 
			('brown',11),
			('red',-7)
]

count = MissingHelper()
result = defaultdict(count, current)
for key, value in increment:
	result[key] += value

print(dict(result))