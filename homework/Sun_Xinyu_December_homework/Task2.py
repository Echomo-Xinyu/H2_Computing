# by Sun Xinyu
# the file is a terminal based prompter to receive instruction from user
# input: 

title = input()
N = int(input())
command = []
for i in range(N):
    newline = input()
    command.append(newline)

def create_navbar():
	try:
		tabname = []
		tablink = []
		for line in command:
			x = line.split(',')
			for i in x:
				i = i.strip()
			tabname.append(x[0])
			tablink.append(x[1])
		print("passed1")
		t = open("{0}.html".format(title), 'w')
		c = open("navbar_template.txt", 'r')
		cnt = 0
		for line in c:
			# line = line.decode('utf-8')
			if cnt == 5:
				t.write("	<title>{0}</title>\n".format(title))
			elif cnt > 60:
				t.write("		<a class = \"item\" href=\"/\" style=\"margin-right: 2em; border-right: 1px solid gray;\"><p>{0}</p></a>\n".format(title))
				for i in range(N):
					t.write("		<a class = \"item\" href=\"{0}\"><p>{1}</p></a>\n".format(tablink[i], tabname[i]))
				t.write('	</div>\n')
				t.write('</body>\n')
				t.write('</html>\n')
				break
			else:
				t.write(line)
			cnt += 1
		t.close()
		c.close()
		print("success")
	except:
		print("Error detected. Please check your input format")
	print("end of the function")

create_navbar()