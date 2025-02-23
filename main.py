from flask import Flask, request, render_template, redirect, url_for
import sqlite3

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




@app.route("/add",  methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        text = request.form.get('text')
        my_db(text, 0)
    return render_template("add.html")


@app.route("/mylist",  methods=['GET', 'POST'])
def mylist():
    data = my_db_data()
    if request.method == "POST":
        data_req = request.form
        first_key = next(iter(data_req)) 
        first_value = data_req[first_key]
        first_int = int(first_key)
        if first_value == 'SAVE':
            for item in data:
                list_item = list(item)
                if list_item[0] == first_int:
                    list_item[2] = 1
                    if list_item[2] == 1:
                        my_db_update(first_int)
                        
        
    return render_template("list.html", data=data)



def my_db(text, first_int):
    db = sqlite3.connect('database.db') #create file and database


    cursore = db.cursor() #create cursor

    #create something, control databse
    cursore.execute("""CREATE TABLE IF NOT EXISTS question (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        mytext TEXT NOT NULL,
        value INTEGER NOT NULL DEFAULT 0 CHECK(value IN (0,1))
        
    )""") 


    cursore.execute("INSERT INTO question (mytext) VALUES (?)", (text,))


    cursore.execute("SELECT mytext FROM question")
    db.commit()


    db.close() 


def my_db_update(first_int):
    db = sqlite3.connect('database.db') 


    cursore = db.cursor() 


    cursore.execute(f"UPDATE question SET value = ((value | 1) - (value & 1)) WHERE id = {first_int}")
    print(first_int)


    db.commit() 


    db.close()


def my_db_data():
    db = sqlite3.connect('database.db') 


    cursore = db.cursor() 

    cursore.execute("SELECT * FROM question")
    data = cursore.fetchall()

    db.close() 
    return data




if __name__ == "__main__": 
    app.run(debug=True) 