import subprocess
x = 0
while x < 5:
	x = x + 1
	
	subprocess.call(["say", str(x)])
	if x % 3 == 0:
		subprocess.call(["say",  "Fizz"])
	if x % 5 == 0:
		subprocess.call(["say", "Buzz"])
