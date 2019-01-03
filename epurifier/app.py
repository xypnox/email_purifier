from flask import Flask, request, redirect, url_for, render_template, send_from_directory, flash,session
from werkzeug.utils import secure_filename
import os
import config 
import string
import subprocess
import pexpect
import threading
import pandas as pd
from . import email_checker as ec
import sys





app = Flask('__main__')
app.config.from_object('config.Config')
#sys.path.append()

@app.route('/',methods=['GET','POST'])

def home():


	if request.method=='POST':
		if 'inf' not in request.files:
			#No file in request
			flash('Error : No file found in request')
			return redirect(request.url)

		inf = request.files['inf']
		outf = request.form['outf']
		column = request.form['column']
		if inf.filename == '':
			#No file
			flash('Error : No file found in request')
			return redirect(request.url)

		broken = inf.filename.split('.')
#		print(broken)
#		print(str(broken[1]))		
#		print(str(broken[1]) is not 'csv')
		if len(broken)!=2 or str(broken[1]) != 'csv':
			#Wrong file extension
			flash('Wrong file extension')
#			print('See here')
			return redirect(request.url)

		if not outf:
			flash('Output file name is mandatory')
			#All columns mandatory
			return redirect(request.url)



		broken = outf.split('.')
		if len(broken)!=2 or str(broken[1]) != 'csv':
			#Wrong file extension
			flash('Wrong file extension')
#			print('See here')
			return redirect(request.url)

		inf.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(inf.filename)))
		session['infile'] = secure_filename(inf.filename)
		session['outfile'] = outf
		session['column'] = column	
		return redirect('/uploaded')



	if request.method=='GET':
		return render_template('index.html')




@app.route('/uploaded',methods=['GET','POST'])

def arrive():

	if request.method == 'GET' and session.get('infile')!=None:
		data_df = pd.read_csv(session.get('infile'))
		colName = None

		for column in data_df.columns:
			if column.lower() == column_header:
				colName = column

		if colName == None:
			flash('The specified column name ' + column_header+ ' was not found in the input file '+inputfile+'!\nExiting...\n')
			return render_template('status.html')

		emails = data_df[colName]
		emil = ec.EmailPurifier(list(emails))
		emil.CheckEmails(checkTypo=True)
		emil.CorrectWrongEmails()
		data_df[colName] = emil.emails


		flash('Do you want to remove duplicate entries? Enter 1 for yes, 2 for no :')
		return render_template('status2.html')

	elif request.method=='POST':
		session['removeduplicates'] = request.form['input']
		return redirect('/next')

	else:
		return redirect('/')

@app.route('/next')

def nextprocess():
	if session.get('removeduplicates')==None:
		return redirect('/')

	

	

if __name__ == '__main__':
	app.run()




"""	if request.method=='GET':
		output = driver.communicate()
		output = output[0]
		output = output.decode("utf-8")
		print('out is : ',output)
		flash(output)
		return render_template('status.html')

	if request.method=='POST':
		inputgiven = request.form['input']
		output = driver.communicate(inputgiven)
		output = output[0]
		output = output.decode("utf-8")
		print('out is : ',output)
		flash(output)
		return render_template('status.html')
"""




