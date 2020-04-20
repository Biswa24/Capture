from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def get_link():
    link = request.form['link']
    return link

if __name__ == '__main__':
    app.run()