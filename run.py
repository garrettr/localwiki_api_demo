from flask import Flask, request, render_template
app = Flask(__name__)

import os

@app.route('/search/<query>')
def search():
    pass

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    #app.run(host='0.0.0.0', port=port) # Heroku likes this
    app.run(debug=True)

