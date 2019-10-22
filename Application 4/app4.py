#!/usr/bin/env python

'''
Application 4: Intro to Personal Website Using Flask.
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    '''
    Website HomePage
    '''
    return render_template("home.html")

@app.route('/about/')
def about():
    '''
    Website About Page
    '''
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
