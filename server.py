
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt',mode='a') as db:
        file = db.write(f'\n{data["email"]},{data["subject"]}, {data["message"]}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as db:
        email = data["email"]
        subj = data["subject"]
        msg = data["message"]
        csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subj, msg])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save the data'
    else:
        return 'Try Again !!!'



'''
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/works.html')
def work():
    return render_template('works.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')
'''



#@app.route('/<username>')
#def hello_world(username=None):
#    return render_template('index_test.html', name=username, post_id=1)


#@app.route('/<username>/<int:post_id>')
#def html_user_id(username=None, post_id=None):
#   return render_template('index_test.html', name=username, post_id=post_id)


#@app.route('/blg')
#def blog():
#     return 'Building Blog page in Progress'


#@app.route('/blog/2020/dogs')
#def blog_dogs():
#    return 'This is my dogs post'
