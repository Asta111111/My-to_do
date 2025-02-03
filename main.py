from flask import Flask, request, render_template, redirect
import random

app = Flask(__name__)





#routers 
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            return redirect("/add", code=302)
        elif  request.form.get('action2') == 'VALUE2':
            pass 
        else:
            pass 
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")



savetext = {}

@app.route("/add",  methods=['GET', 'POST'])
def add():
    id = random.randint(0, 1000000000)
    savetext
    if request.method == "POST":
        text = request.form.get('text')
        savetext.update({text: id})
        print(savetext)
    return render_template("add.html")



@app.route("/mylist")
def mylist():
    return render_template("list.html")




if __name__ == "__main__": 
    app.run(debug=True) 