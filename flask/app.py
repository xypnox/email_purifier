from flask import Flask, render_template, request,json

app= Flask('__main__')

@app.route('/')

def main():
	return render_template('index.html')



if __name__ == '__main__':
	app.run('0.0.0.0',8080)
