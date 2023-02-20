from flask import Flask, request,render_template
from bug_tracker.bug_app.user import User
from bug_tracker.bug_app.bug import Bug

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)



@app.route('/create_bug',methods=['GET','POST'])
def create_bug():
    try:
        return render_template('create_bug.html')
    except Exception as e:
        return str(e)


    
@app.route('/view_bug',methods=['GET','POST'])
def view_bug():
    try:
        bug = Bug()
        bugs = bug.get_bug()
        return render_template('view_bug.html',context={"bugs":bugs})
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run()