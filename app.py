from flask import Flask, render_template, g
import sqlite3

app = Flask("__name__")
DATABASE = 'static/images.db'

'''stuff to get the database connection and store it in the g dictionary and close it when done'''
def get_db():
    db=getattr(g,'_database',None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def home():
    cursor = get_db().cursor()
    sql = "SELECT filename FROM image"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("index.html", filenames=results)

@app.route('/upload/')
def upload():
    '''page to allow users to upload images to the database'''
    return "In Progress"


if __name__=="__main__":
    app.run(debug=True)
