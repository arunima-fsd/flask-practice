#The views are the handlers that respond to requests from
# web browsers or other clients. In Flask handlers are written
# as Python functions. Each view function is mapped to one or more request URLs


#the render_template function invokes the Jinja2
# templating engine that is part of the Flask framework

from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname' : 'mickey'}
    posts = [  {
                'author': {'nickname': 'John'},
                'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title = 'Home',
                           user = user,
                           posts = posts)
