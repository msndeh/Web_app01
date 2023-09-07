from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_url', methods=['POST'])
def process_url():
    url = request.form['url']
    
    # Parse the URL
    from urllib.parse import urlparse
    parsed_url = urlparse(url)
    
    protocol = parsed_url.scheme
    queries = parsed_url.query
    
    return render_template('result.html', protocol=protocol, queries=queries)

if __name__ == '__main__':
    app.run(debug=True)
