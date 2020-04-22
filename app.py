from flask import Flask, request, render_template, url_for
from Main import img_gen , pdf_gen

app = Flask(__name__, static_url_path='/static')
app.debug = True

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def get_link():
    link = request.form['link']
    img_name = img_gen(link)
    pdf_name = pdf_gen(img_name)
    save=1
    return render_template("index.html", img_name=img_name,save=save, pdf_name=pdf_name)

if __name__ == '__main__':
    app.run(debug = True )