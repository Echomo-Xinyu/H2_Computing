from flask import *
import sqlite3
app = Flask("__name__")

@app.route('/')
def root():
	return render_template("Email_generated.html")
@app.route('/submit', methods=["POST"])
def submit():
	table_name = "generatedTable"
	con = sqlite3.connect('generated.db')
	fielddata = [None for i in range(5)]
	try:
		command = 'CREATE TABLE IF NOT EXISTS {0}(refID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT)'.format(table_name)
		con.execute(command)
		command = "ALTER TABLE '{0}' ADD '{1}' '{2}'".format(table_name, "First Name","TEXT")
		con.execute(command)
		command = "ALTER TABLE '{0}' ADD '{1}' '{2}'".format(table_name, "Last Name","TEXT")
		con.execute(command)
		command = "ALTER TABLE '{0}' ADD '{1}' '{2}'".format(table_name, "Domain","TEXT")
		con.execute(command)
		command = "ALTER TABLE '{0}' ADD '{1}' '{2}'".format(table_name, "Number","INTEGER")
		con.execute(command)
		command = "ALTER TABLE '{0}' ADD '{1}' '{2}'".format(table_name, "Photo","TEXT")
		con.execute(command)
	except:
		pass
	fielddata = [None for i in range(5)]
	try:
		if 'Photo' in request.files:
			filename = 'Photo'
			fielddata[4] = 'Photo.in'
			inputfile = request.files[filename]
			import os
			try:
				os.remove('static/Photo.in')
			except:
				pass
			inputfile.save('static/Photo.in')
	except:
		return 'Invalid Input'
	try:
		if fielddata[0] == None:
			fielddata[0] = request.form["First Name"]
		if fielddata[1] == None:
			fielddata[1] = request.form["Last Name"]
		if fielddata[2] == None:
			fielddata[2] = request.form["Domain"]
		if fielddata[3] == None:
			fielddata[3] = request.form["Number"]
		if fielddata[4] == None:
			fielddata[4] = request.form["Photo"]
		for i in range(len(fielddata)):
			if fielddata[i] == None or fielddata[i] == '' or len(fielddata[i]) == 0: return "Invalid Input"
		con.execute("INSERT INTO generatedTable('First Name', 'Last Name', 'Domain', 'Number', 'Photo') VALUES(?, ?, ?, ?, ?)", (fielddata[0], fielddata[1], fielddata[2], fielddata[3], fielddata[4]))
		import os
		con.row_factory = sqlite3.Row
		refID = None
		cursor = con.execute('SELECT refID FROM generatedTable WHERE "Photo"="Photo.in"')
		r = cursor.fetchone()
		refID = r['refID']
		con.execute("UPDATE generatedTable SET 'Photo'=? WHERE refID=?", (str(refID) + str('Photo'), int(refID)))
		newname = str('static/') + str(refID) + str('Photo')
		os.rename('static/Photo.in', newname)
	except:
		return "Invalid Input"
	con.commit()
	con.close()
	return "Input Submitted Successfully."
if __name__ == "__main__":
	app.run()