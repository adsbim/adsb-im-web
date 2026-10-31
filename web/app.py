import os
from flask import Flask, redirect, render_template, request, send_from_directory
app = Flask(__name__)

data = {
    "feeder_status": """We haven't seen an ADS-B image from your IP address connect to our server. If you have booted your single board computer with the ADSB.im image and still get this message, please take a look at the troubleshooting section in our <a href="/faq">FAQ</a>."""
}

@app.context_processor
def site_context():
    # every template reads these two, so without them a local run renders the
    # wrong site: 'adsb.im' in undefined is false rather than an error, so each
    # page quietly falls through to the sdre.im branding
    host = request.headers.get('X-Forwarded-Host') or request.host
    if host.split(':')[0] in ('127.0.0.1', 'localhost', '[::1]'):
        # nothing is proxying in front of us, so let the developer say which
        # of the two sites they are looking at
        host = os.environ.get('SITE_HOST', 'adsb.im')
    return {
        'x_forwarded_host': host,
        'version': os.environ.get('FEEDER_VERSION', ''),
    }

@app.route('/')
def index():
    return redirect('/home', code=301)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/<path:page>')
def page(page):
    return render_template(f'{page}.html', data=data)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=8000)
