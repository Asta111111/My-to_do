from flask import Flask, request, render_template, redirect, url_for
import sqlite3 
from datetime import datetime


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
        my_db(text)
    return render_template("add.html")


@app.route("/mylist",  methods=['GET', 'POST'])
def mylist():
    data = my_db_data()
    time_list = data
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
        
        return redirect(url_for("mylist")) 
                        
                        
    data_update_req = my_db_update_data()   
    return render_template("list.html", data=data, data_update_req=data_update_req, time_list=time_list)



def my_db(text):
    db = sqlite3.connect('database.db') #create file and database
    list_time = datetime.now().date()

    cursore = db.cursor() #create cursor

    #create something, control databse
    cursore.execute(f"""CREATE TABLE IF NOT EXISTS question (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        mytext TEXT NOT NULL,
        value INTEGER NOT NULL DEFAULT 0 CHECK(value IN (0,1)),
        date DATE 

    )""") 


    cursore.execute("INSERT INTO question (mytext, value, date) VALUES (?, ?, ?)", (text, 0, list_time,))


    cursore.execute("SELECT mytext FROM question")
    db.commit()


    db.close() 



def my_db_update(first_int):
    db = sqlite3.connect('database.db') 


    cursore = db.cursor() 


    cursore.execute(f"UPDATE question SET value = ((value | 1) - (value & 1)) WHERE id = {first_int}")


    db.commit() 


    db.close()


def my_db_data():
    db = sqlite3.connect('database.db') 


    cursore = db.cursor() 

    cursore.execute("SELECT * FROM question")
    data = cursore.fetchall()

    db.close() 
    return data


def my_db_update_data():
    db = sqlite3.connect('database.db') 


    cursore = db.cursor() 

    cursore.execute("SELECT * FROM question WHERE value = 1")
    data_update = cursore.fetchall()
    db.close() 
    
    return data_update



if __name__ == "__main__": 
    app.run(debug=True) 