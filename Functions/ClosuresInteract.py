"""
def priority_sort(items, group):
	def sortHelper(x):
		if x in group:
			return 0, x
		return 1, x
	items.sort(key = sortHelper)
"""
def priority_sort(items, group):
	found = [False]
	def sortHelper(x):
		if x in group:
			found[0] = True
			return 0, x
		return 1, x
	items.sort(key = sortHelper)
	return found[0]

class sorter(object):
	def __init__(self, group):
		self.group = group
		self.found = False

	def __call__(self, x):
		if x in group:
			self.found = True
			return 0, x
		return 1, x


items = [8, 1, 2, 7, 3,5, 4, 6]
group = {5, 7, 2}
found = priority_sort(items, group)
print items
print found

sort = sorter(group)
items.sort(key = sort)
print items
print sort.found