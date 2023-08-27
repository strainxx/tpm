#---Aruus TG plugin parser---
#~~~Aruus beta v.0.1~~~

import os

def readPlugin(path):
	#info indexes: 0 - name; 1 - description;
	#2 - author
	#3 - version; 4 - contains sussy modules?
	info = []
	count = 0
	f = open(path+"/plugin.aruus", "r")
	count = sum(1 for _ in f)
	f.seek(0)
	lines = f.readlines()
	for i in range(count):
		data = lines[i]
		info.append(lines[i].split('"', 2)[1])
		
	return info


def parse():
	modules = {}
	fu = [f.path for f in os.scandir("./") if f.is_dir()]
	
	#print(fu)
	
		
		#print(plugin)
	
	return fu
	
	
def info(fu):
	print(f"Founded {len(fu)} plugins \n")
	count = 0
	for i in fu:
		count+=1
		try:
			plugin = readPlugin(i)
			name = plugin[0]
			desc = plugin[1]
			author = plugin[2]
			ver = plugin[3]
			print(f"Plugin № {count}: {name} by {author} v. {ver} | {desc}\n")
		except:
			damged = True
			print(f"Plugin № {count}: Damaged plugin :( \nTry to reinstall plugin | Plugin path: {i}\n")
#parse()