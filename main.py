from flask import Flask, request, render_template

app = Flask(__name__)



#routers 
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            pass # do something
        elif  request.form.get('action2') == 'VALUE2':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")


if __name__ == "__main__": 
    app.run(debug=True) 