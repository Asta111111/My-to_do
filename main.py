from flask import Flask, request, render_template, redirect

app = Flask(__name__)





#routers 
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            return redirect("/add", code=302)
        elif  request.form.get('action2') == 'VALUE2':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")




@app.route("/add",  methods=['GET', 'POST'])
def add():
    savetext = [] 
    if request.method == "POST":
        text = request.form.get('text')
        print(text)
        savetext.append(text)
    return render_template("add.html")



if __name__ == "__main__": 
    app.run(debug=True) 