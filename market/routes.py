
from flask import render_template,Blueprint

main_pages=Blueprint("main_pages",__name__)
@main_pages.route('/')
@main_pages.route('/home')
def home_page():
    return render_template('home.html')










