import os
try:
	x = open("path.txt" ,'r').read()
except:
	x = raw_input("Input path to addonlist\n>")
	x = str(x)
	open("path.txt", 'w').write(x)
filen = os.path.join(x, "addonlist.txt")
x = open(filen, 'r').read()
if "1" in x:
	x = open(filen, 'r').read().split("1")
	open(filen, 'w').write(x[0] +"0"+x[1])
	os.rename(__file__, "enable_weaponmod.py")
elif "0" in x:
	x = open(filen, "r").read().split("0")
	open(filen, 'w').write(x[0]+"1"+x[1])
	os.rename(__file__, "disable_weaponmod.py")