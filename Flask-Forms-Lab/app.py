from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


accounts={
	"llo2ay" : "123",
	"bob" : "456"


}
username = "llo2ay"
password1 = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/' ,methods=['GET','POST'])  # '/' for the default page
def login():
	facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]
	if request.method=='GET':
		return render_template('login.html')
	else:
		name = request.form['username']
		password = request.form['password']
		for x in (accounts):
			if name==x and password==accounts[x]:
				return render_template('home.html',name=name,password=password,facebook_friends=facebook_friends)
		
		return render_template('login.html')

@app.route('/home' ,methods=['GET','POST'])  # '/' for the default page
def home():

  return render_template('home.html',facebook_friends=facebook_friends)
@app.route('/friends_exist/<string:name>' ,methods=['GET','POST'])  # '/' for the default page
def friends_exist(name):
	y=0
	exists= False
	for x in (facebook_friends):
		if name==x:
			y+=1
	if y>=1:
		exists=True
	return render_template('friend_exists.html',facebook_friends=facebook_friends,exists=exists,name1=name)
		



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)