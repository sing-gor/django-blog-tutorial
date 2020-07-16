from flask import Flask
from flask import render_template

from services.site_data import SiteData

app = Flask(__name__)

site_data = SiteData('http://127.0.0.1:5000')

def home():
    return render_template('home.html',site_data=site_data)

def index():
    return render_template('index.html',site_data=site_data)

def show_1():
    return render_template('show_1.html',site_data=site_data)

def show_2():
    return render_template('show_2.html',site_data=site_data)

def show_3():
    return render_template('show_3.html',site_data=site_data)

def show_4():
    return render_template('show_4.html',site_data=site_data)



app.add_url_rule("/", view_func=home)
app.add_url_rule("/articles/", view_func=index)
app.add_url_rule("/articles/1", view_func=show_1)
app.add_url_rule("//articles/2", view_func=show_2)
app.add_url_rule("//articles/3", view_func=show_3)
app.add_url_rule("//articles/4", view_func=show_4)
