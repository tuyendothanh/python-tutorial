def priority_sort(items, group):
	def sortHelper(x):
		if x in group:
			return 0, x
		return 1, x
	items.sort(key = sortHelper)

items = [8, 1, 2, 7, 3,5, 4, 6]
group = {5, 7, 2}
priority_sort(items, group)
print items