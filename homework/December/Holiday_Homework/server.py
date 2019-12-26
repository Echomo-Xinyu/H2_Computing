# inspired by Irfan's idea

from flask import Flask, render_template, redirect, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def root():
	return render_template("home.html")

@app.route('/task1')
def task1():
	return render_template("task1.html")

@app.route('/createform')
def createform():
	return render_template("createform.html")

# TASK1 - create html form
@app.route('/createform2', methods=['POST'])
def createform2():
	try:
		#collecting data from file
		temp = request.files
		fileHandle = temp["createform_command"]
		command = []
		if fileHandle.filename == '':
			raise Exception
		for line in fileHandle:
			line = line.strip()
			line = line.decode('utf-8')
			print(line)
			command.append(line)

		fname = command[0] + '_generated.html'
		f = open(fname, 'w')
		t = open("form_template.txt", 'r')

		cnt = 1
		# copy based on template
		for line in t:
			if cnt > 48:
				break
			cnt += 1
			f.write(line)

		# submit to url
		temp = command[len(command) - 1]
		temp = temp.split(',')
		submitname = temp[0]
		submitto = temp[1]
		s = '	<form action="{0}" enctype="multipart/form-data" method="POST">\n'.format(submitto)
		f.write(s)
		for i in range(1, len(command) - 1):
			temp = command[i].split(',')
			field_name = temp[0]
			field_type = temp[1]
			fieldmax = 1000
			if(len(temp) > 2):
				fieldmax = temp[2]
			print(field_type)
			if(field_type == 'text' or field_type == 'file' or field_type == 'number' or field_type == 'password'):
				f.write('		<div>\n')
				f.write('			<label for={0}>{1}</label>\n'.format(field_name, field_name))
				f.write('			<input name=\'{0}\' type=\'{1}\' maxlength={2}>\n'.format(field_name, field_type, fieldmax))
				f.write('		</div>\n')
			elif(field_type =='textarea'):
				f.write('		<div>\n')
				f.write('			<label for={0}>{1}</label>\n'.format(field_name, field_name))
				f.write('			<textarea name="{0}" maxlength={1}></textarea>\n'.format(field_name, fieldmax))
				f.write('		</div>\n')
			elif(field_type == 'button'):
				f.write('		<div>\n')
				f.write('			<button type="{1}">{0}</button>\n'.format(field_name, field_type))
				f.write('		</div>\n')
			else:
				print("exception - ", command[i])
				raise Exception
		print('name: ', submitname)
		f.write('		<div>\n')
		f.write('			<button type="{1}">{0}</button>\n'.format(submitname, 'submit'))
		f.write('		</div>\n')
		f.write('	</form>\n')
		f.write('</body>\n')
		f.write('</html>\n')
		t.close()
		f.close()
	except:
		return render_template('invalid.html')
	return render_template('valid.html')

@app.route('/createsql')
def createsql():
	return render_template("createsql.html")

@app.route('/createsql2', methods=["POST"])
def createsql2():
	try:
		f = request.files["createsql_command"]
		field_name = []
		field_type = []
		original_field_type = []
		table_name = ''
		cachelast = None
		# print('passed')
		for line in f:
			line = line.strip()
			line = line.decode('utf-8')
			temp = line.split(',')
			if(len(temp) == 1):
				table_name = temp[0]
			else:
				cachelast = temp[1]
				if(temp[1] == 'file' or temp[1] == 'text' or temp[1] == 'textarea'):
					field_name.append(temp[0])
					field_type.append('TEXT')
					original_field_type.append(temp[1])
				elif(temp[1] == 'number' or temp[1] == 'password'):
					field_name.append(temp[0])
					field_type.append('INTEGER')
					original_field_type.append(temp[1])
				else:
					continue
		f.close()
		# print('passed')

		#dynamically creating table - if it doesnt exist
		t = open(table_name + '.py', 'w')
		t.write('from flask import *\n')
		t.write('import sqlite3\n')
		t.write('app = Flask("__name__")\n\n')
		t.write("@app.route('/')\n")
		t.write("def root():\n")
		t.write('	return render_template("{0}_generated.html")\n'.format(table_name))

		t.write("@app.route('{0}', methods=[\"POST\"])\n".format(cachelast))
		t.write("def submit():\n")
		t.write('	table_name = "generatedTable"\n')
		t.write("	con = sqlite3.connect('generated.db')\n")
		t.write("	fielddata = [None for i in range({0})]\n".format(len(field_name)))
		t.write("	try:\n")
		t.write("		command = 'CREATE TABLE IF NOT EXISTS {0}(refID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT)'.format(table_name)\n")
		t.write("		con.execute(command)\n")
		for i in range(0, len(field_name)):
			t.write("		command = \"ALTER TABLE '{0}' ADD '{1}' '{2}'\".format(table_name, " + '"' + str(field_name[i]) + '"' + ',' + '"' + str(field_type[i]) + '")\n')
			t.write("		con.execute(command)\n")
		t.write("	except:\n")
		t.write("		pass\n")
		# print('passed')

		# code to retrieve input to form for files
		t.write("	fielddata = [None for i in range({0})]\n".format(len(field_name)))
		if 'file' in original_field_type:
			for i in range(len(original_field_type)):
				if original_field_type[i] == 'file':
					t.write("	try:\n")
					t.write("		if '{0}' in request.files:\n".format(field_name[i]))
					t.write("			filename = '{0}'\n".format(field_name[i]))
					t.write("			fielddata[{0}] = '{1}.in'\n".format(i, field_name[i]))
					t.write("			inputfile = request.files[filename]\n")
					t.write("			import os\n")
					t.write("			try:\n")
					t.write("				os.remove('static/{0}.in')\n".format(field_name[i]))
					t.write("			except:\n")
					t.write("				pass\n")
					t.write("			inputfile.save('static/{0}.in')\n".format(field_name[i])) #generic format for file, can be accessed as per normal
					t.write("	except:\n")
					t.write("		return 'Invalid Input'\n")
		# print('passed')

		# retrieve data for normal input
		t.write('	try:\n')
		for i in range(len(field_name)):
			t.write('		if fielddata[{0}] == None:\n'.format(i))
			t.write('			fielddata[{0}] = request.form["{1}"]\n'.format(i, field_name[i]))
		t.write('		for i in range(len(fielddata)):\n')
		t.write('			if fielddata[i] == None or fielddata[i] == \'\' or len(fielddata[i]) == 0: return "Invalid Input"\n')
		# print('passed')

		# INSERT Code - Special formatting
		t.write('		con.execute("INSERT INTO generatedTable(')
		first = True
		for i in field_name:
			if first:
				t.write('\'{0}\''.format(i))
				first = 0
			else:
				t.write(', \'{0}\''.format(i))
		t.write(') VALUES(')
		
		# print('passed')
		first = True
		for i in field_name:
			if first:
				t.write('?')
				first = 0
			else:
				t.write(', ?')
		t.write(')", (')

		# print('passed')
		first = True
		for i in range(len(field_name)):
			if first: 
				t.write('fielddata[{0}]'.format(i))
				first = False
			else:
				t.write(', fielddata[{0}]'.format(i))
		t.write('))\n')
		t.write('		import os\n')
		t.write('		con.row_factory = sqlite3.Row\n')
		for j in range(len(original_field_type)):
			if original_field_type[j] != 'file': continue
			t.write("		refID = None\n")
			t.write("		cursor = con.execute('SELECT refID FROM generatedTable WHERE \"{0}\"=\"{1}.in\"')\n".format(field_name[j], field_name[j]))
			t.write("		r = cursor.fetchone()\n")
			t.write("		refID = r['refID']\n")
			t.write("		con.execute(\"UPDATE generatedTable SET '{0}'=? WHERE refID=?\", (str(refID) + str('{1}'), int(refID)))\n".format(field_name[j], field_name[j]))
			t.write("		newname = str('static/') + str(refID) + str('{0}')\n".format(field_name[j]))
			t.write("		os.rename('static/{0}', newname)\n".format(str(field_name[j] + ".in")))
		t.write('	except:\n')
		t.write('		return "Invalid Input"\n')
		t.write('	con.commit()\n')
		t.write('	con.close()\n')
		t.write('	return "Input Submitted Successfully."\n')
		t.write('if __name__ == "__main__":\n')
		t.write('	app.run()')
		t.close()
	except:
		return render_template("invalid.html")
	return render_template("valid.html")

@app.route('/task2')
def task2():
	return render_template("task2.html")

@app.route('/navbar')
def navbar():
	return	render_template("navbar.html")

@app.route('/navbar2', methods=["POST"])
def navbar2():
	try:
		title = None
		N = None
		tabname = []
		tablink = []
		f = request.files["command"]
		cnt = 0
		for line in f:
			line = line.decode('utf-8')
			line = line.strip()
			if cnt == 0: title = str(line)
			elif cnt == 1: N = int(line)
			else:
				line = str(line)
				x = line.split(',')
				for i in x: i = i.strip()
				tabname.append(x[0])
				tablink.append(x[1])
			cnt += 1

		t = open("{0}.html".format(title), 'w')
		c = open("navbar_template.txt", 'r')
		cnt = 0
		for line in c:
			# line = line.decode('utf-8')
			if cnt == 3:
				t.write("	<title>{0}</title>\n".format(title))
			elif cnt > 41:
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
	except:
		return render_template("invalid.html")
	return render_template("valid.html")

app.run()
