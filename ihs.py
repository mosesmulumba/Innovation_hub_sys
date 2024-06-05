from flask import Flask , render_template , request , url_for , redirect
import mysql.connector 
from mysql.connector import errorcode

app = Flask(__name__)

# connect to the mysql database
def connect_db():
    try:
        mydb = mysql.connector.connect(
            user = "admin",
            password = "UMU@30_innovation",
            host = "localhost",
            database = "innovation_hub_db"
        )
        return mydb
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something went wrong with the username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)



# create the home route
@app.route("/")
def index():
    mydb = connect_db()
    cursor = mydb.cursor(dictionary=True)

    # List of tables to display
    tables = ['Members', 'Collaboration', 'Faculties','Projects']
    data = {}

    for table in tables:
        cursor.execute(f"SELECT * FROM {table}")
        data[table] = cursor.fetchall()

    mydb.close()
    return render_template('index.html', data=data)

# insert the data
@app.route("/insert" , methods=['POST'])
def insert_data():
    table = request.form['table']
    data = request.form['data'].split(',')
    mydb = connect_db()
    cursor = mydb.cursor()
    placeholders = ','.join(['%s'] * len(data))
    query = f"insert into {table} values (null, {placeholders})"
    cursor.execute(query , data)
    mydb.commit()
    mydb.close()
    return redirect(url_for('index'))


# update the tables
@app.route("/update" , methods=['POST'])
def update_data():
    table = request.form['table']
    column = request.form['column']
    new_value = request.form['new_value']
    condition = request.form['condition']
    mydb = connect_db()
    cursor = mydb.cursor()
    query = f"update {table} set {column} = %s where {condition}"
    cursor.execute(query , (new_value,))
    mydb.commit()
    mydb.close()
    return redirect(url_for('index'))


# delete the data
@app.route("/delete" , methods=['POST'])
def delete_data():
    table = request.form['table']
    condition = request.form['condition']
    mydb = connect_db()
    cursor = mydb.cursor()
    query = f"delete from {table} where {condition}"
    cursor.execute(query)
    mydb.commit()
    mydb.close()
    return redirect(url_for('index'))


# create the new table
@app.route("/create_table", methods=['POST'])
def create_new_table():
    table_name = request.form['table_name']
    columns = request.form['columns']
    mydb = connect_db()
    cursor = mydb.cursor()
    query = f"create table if not exists {table_name} ({columns})"
    cursor.execute(query)
    mydb.commit()
    mydb.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)