import os
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def main():
    db_connect_result = False
    err_message = ""
    try:
        conn = mysql.connector.connect(
            host=os.environ.get('DB_Host'),
            database=os.environ.get('DB_Database'),
            user=os.environ.get('DB_User'),
            password=os.environ.get('DB_Password')
        )
        color = '#39b54b'
        db_connect_result = True
    except mysql.connector.Error as e:
        color = '#ff3f3f'
        err_message = str(e)

    return render_template('hello.html', debug=err_message, db_connect_result=db_connect_result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
