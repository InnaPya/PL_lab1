import requests, re
b = []
old = []
c = 0
depth = 5
u = 'http://www.csd.tsu.ru'
def rec(j, c):
	c += 1
	r = requests.get(j)
	res = r.text
	a = re.findall('(?:mailto:)(\w+@[\w\.-]+)', res)
	for i in a:
		if i not in b: b.append(i)
	l = re.findall('<a\s+href="(/(?!:)[^"#]+)', res)
	for i in l:
		if i in old: l.remove(i)
		else: old.append(i)
	if c < depth:
		for i in l[0:min(10,len(l))]:
			rec(u+i, c)
rec(u, c)
print(b)
