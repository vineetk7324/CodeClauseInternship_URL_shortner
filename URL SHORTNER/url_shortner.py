

from flask import Flask, render_template, request, redirect, url_for
import shortuuid

app = Flask(__name__)

# Dictionary to store short URLs and their corresponding full URLs
url_mapping = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    full_url = request.form.get('full_url')
    if full_url:
        short_url = shortuuid.uuid()[:8]  # Generate a short URL
        url_mapping[short_url] = full_url
        return render_template('index.html', short_url=short_url)
    return redirect(url_for('index'))

@app.route('/<short_url>')
def redirect_to_full_url(short_url):
    if short_url in url_mapping:
        full_url = url_mapping[short_url]
        return redirect(full_url)
    return "Short URL not found."

if __name__ == '__main__':
    app.run(debug=True, port=8080)  # Change port to 8080 or any other available port
