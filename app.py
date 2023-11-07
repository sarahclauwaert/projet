import fiche_appel
from flask import Flask, request, render_template
app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/traiter', methods=['POST'])
def traiter():
    message = '<h1>Le bouton a été cliqué ! </h1>'
    return message

if __name__ == '__main__':
    app.run(debug=True)