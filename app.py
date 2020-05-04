from flask import Flask, request, render_template, url_for, redirect
from Main import img_gen , pdf_gen , delete , url_check
from apscheduler.schedulers.background  import BackgroundScheduler

app = Flask(__name__, static_url_path='/static')
# app.debug = True

time_diff = 3 #minutes

def sensor():
    delete(val='img',time_diff = time_diff)
    delete(val='pdf',time_diff = time_diff)

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',minutes=time_diff)
sched.start()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def get_link():
    link = request.form['link']
    msg = url_check(link)
    if(msg!='Web'):
        error_link=True
        return render_template("index.html", error_link=error_link, msg=msg)
    # msg code 
    # Invalid -> Invalid url , https://www.google.com
    # Down -> Website is currently not responding, try again after sometime
    # NExist -> Couldn't reach this website , check url 
    # Nfound -> Website not found 

    # Web -> All fine , call img_gen 

    img_name = img_gen(link)
    pdf_name = pdf_gen(img_name)
    save=1
    notice="The screenshot will be delete after 30 mins"
    return render_template("index.html", img_name=img_name,save=save, pdf_name=pdf_name, notice=notice)

if __name__ == '__main__':
    app.run()