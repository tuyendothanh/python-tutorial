
def div1(a, b):
	try:
		return a / b
	except ZeroDivisionError:
		return None

results1 = div1(5,0)
print results1

def div2(a, b):
	try:
		return a / b, True
	except ZeroDivisionError:
		return None, False

results1, condition = div2(5,0)
if condition == True:
	print results1
else:
	print "Error Message: " + "Divition Zero"

def div3(a, b):
	try:
		return a / b
	except ZeroDivisionError as e:
		raise ValueError(e)

result = div3(5,0)
try:
	print result
except ValueError:
	print("Message error: ZeroDivisionError")



