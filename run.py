from flask import Flask, request, render_template
app = Flask(__name__)

import os
import mimetypes
import slumber

@app.route('/search')
def search():
    # TODO: make this a field for different localwikis
    SITE = "http://detroitwiki.org/"
    query = request.args['query']

    api = slumber.API(SITE + "api/")

    results = api.file.get(slug__icontains=query)
    # TODO: figure out pagination
    images = []
    for f in results['objects']:
        is_image = mimetypes.guess_type(f['file'])[0].startswith('image/')
        if is_image:
            images.append({
                'url': SITE + f['file'],
                'title': f['slug']
                })

    return render_template('gallery.html', query=query, images=images)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    #app.run(host='0.0.0.0', port=port) # Heroku likes this
    app.run(debug=True)

