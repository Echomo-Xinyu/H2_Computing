# by Sun Xinyu
# the file is a terminal based prompter to receive instruction from user
# input: elements for the web form
# output: html file and sql file for the web app

from flask import Flask, render_template, request, redirect
import sqlite3 as sql

# input format:
# first line: name of the form, number of elements included in the form
# following each line should follow this format <field_name>,<field_type>,<max_length(optional)>.
# (Note that the default max_length will always be 1000.)
# field type can only be: text, textarea, file, button, number (maxlength ignored), password
# if fielf type==button, since submit button is reserved for the last line, only "reset" button available
# The last line is a special line reserved for the 'submit' button. In this line write, <field_label>,<url_to_submit_to>
# So an example would be as below: (ignore the "# " part)

# Email Signup, 7
# First Name,text,30
# Last Name,text,30
# Domain,text,50
# Number,number
# Photo,file
# Cancel,button
# Signup,/submit

title, line_number = input().split(",")
command = [title]
for i in range(int(line_number)):
    newline = input()
    command.append(newline)

def create_html():
	try:
		fname = title + '_generated.html'
		f = open(fname, 'w')
		t = open("form_template.txt", 'r')

		cnt = 1
		# copy based on template
		for line in t:
			if cnt > 58:
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
			# print(field_type)
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
		# print('name: ', submitname)
		f.write('		<div>\n')
		f.write('			<button type="{1}">{0}</button>\n'.format(submitname, 'submit'))
		f.write('		</div>\n')
		f.write('	</form>\n')
		f.write('</body>\n')
		f.write('</html>\n')
		t.close()
		f.close()
		print("success with html")
	except:
		print("Error detected. Please check against the input format")
	

create_html()

# the sql part takes the same input as the part before
def create_sql():
	try:
		field_name = []
		field_type = []
		original_field_type = []
		table_name = ''
		cachelast = None
		# print('passed1')
		for i, line in enumerate(command):
			# print("passed2")
			line = line.strip()
			# print(i, line)
			# print("passed3")
			temp = line.split(',')
			# print("passed4")
			if(i == 0):
				table_name = temp[0]
				# print("passed5")
			else:
				cachelast = temp[1]
				if(temp[1] == 'file' or temp[1] == 'text' or temp[1] == 'textarea'):
					# print("passed6")
					field_name.append(temp[0])
					field_type.append('TEXT')
					original_field_type.append(temp[1])
					# print("passed7")
				elif(temp[1] == 'number' or temp[1] == 'password'):
					# print("passed8")
					field_name.append(temp[0])
					field_type.append('INTEGER')
					original_field_type.append(temp[1])
					# print("passed8")
				else:
					continue
		# print('passed10')

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
		print("success with sql")
	except:
		print("Error. Please check.")

create_sql()
