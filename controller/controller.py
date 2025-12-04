from flask import Blueprint, render_template

controller = Blueprint('controller', __name__, static_folder='static', template_folder='templates')
app = controller
app.secret_key = 'SOFTWARE'

@app.route('/')
def root_page():
    return render_template('index.html')