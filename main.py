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



save_text = {}
id = random.randint(0, 1000000000)

@app.route("/add",  methods=['GET', 'POST'])
def add():
    id = random.randint(0, 1000000000)
    save_text
    if request.method == "POST":
        text = request.form.get('text')
        save_text.update({text: [id, False]})
        print(save_text)
    return render_template("add.html")


@app.route("/mylist",  methods=['GET', 'POST'])
def mylist():
    if request.method == "POST":
        if request.form.get('save') == 'SAVE':
            for key in save_text:
                save_text[key][1] = True



    return render_template("list.html", save_text=save_text)




if __name__ == "__main__": 
    app.run(debug=True) 