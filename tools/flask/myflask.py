#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 2014/9/21

from flask import Flask,url_for,render_template,redirect,abort
app=Flask(__name__)
@app.route('/')
def hell_world():
    return 'hello world!'
@app.route('/user/<username>/',methods=['GET',])
def show_user(username):
    return 'user name:%s'%username
@app.route('/id/<int:post_id>/',methods=['POST',])
def show_id(post_id):
    return 'post id :%d'%post_id
@app.route('/test/')
def show_info():
    return render_template('base.html')
@app.route('/test/redirect/')
def test_redirect():
    return redirect(url_for('show_info'))

#with app.test_request_context:
    #print url_for('hell_world')
    #print url_for('show_user')
    #print url_for('show_id',post_id=5)
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)