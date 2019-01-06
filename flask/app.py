from flask import Flask, request, redirect, url_for, render_template, send_from_directory, flash,session
from werkzeug.utils import secure_filename
import os
import config 
import string
import subprocess
import pexpect
import threading
import pandas as pd
import sys
import email_checker as ec



app = Flask('__main__')
app.config.from_object('config.Config')
#sys.path.append()

@app.route('/',methods=['GET','POST'])

def home():

#	print('I am here')

	if request.method=='POST':

#		print('Got here')
		if 'inf' not in request.files:
			#No file in request
			flash('Error : No file found in request')
			return redirect(request.url)

		inf = request.files['inf']
		outf = request.form['outf']
		column = request.form['column']
		duplicate = request.form.get('duplicate')
#		print(duplicate)
#		print(type(duplicate))
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
		session['duplicate'] = duplicate

		return redirect('/uploaded')



	if request.method=='GET':
		return render_template('index.html')




@app.route('/uploaded',methods=['GET','POST'])

def arrive():


	column_header = session.get('column')
#	print('see : ',column_header)
#	print('here',type(column_header))
	if len(column_header) == 0:
#		print('i reach')
		column_header = 'email'
#		print(column_header)

	column_header = column_header.lower()
#	print('column header is : ',column_header)

	if session.get('infile')!=None:		#valid session

		inputfile = session.get('infile')
#		print(inputfile)
		data_df = pd.read_csv(session.get('infile'))
		colName = None

		for column in data_df.columns:
#			print(column)
			if column.lower() == column_header:
				colName = column

#		print(colName)
		if colName == None:
			flash('The column name ' + column_header + ' was not found in the input file '+inputfile+'!\nExiting...\n')
			return redirect('/')

		emails = data_df[colName]
		emailobj = ec.EmailPurifier(list(emails))
		emailobj.CheckEmails(checkTypo=True)
		wrongemaillist = emailobj.wrong_emails
		emailobj.SuggestEmails()
		suggestedlist = emailobj.suggestedmails
		if len(wrongemaillist)==0:
			flash('Good csv file, no error found!','info')

		else:
			for wrongemails in wrongemaillist:
				flash(wrongemails,'error')

		#making pairs
		diction = {}
		for i in range(len(suggestedlist)):
			diction[wrongemaillist[i]] = suggestedlist[i]

		return render_template('status.html',diction = diction)

	else:
		flash('Invalid Session')
		return redirect('/')







		


		


	

	

if __name__ == '__main__':
	app.run()




