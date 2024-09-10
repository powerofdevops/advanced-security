# Sample Python code to demonstrate an explicit and typical SQL injection vulnerability in a web application context

import sqlite3
from flask import Flask, request

app = Flask(__name__)

def execute_query(query):
    # Dummy database connection
    db_path = "example.db"
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return []

@app.route('/search', methods=['GET'])
def search():
    username = request.args.get('username')
    query = f"SELECT * FROM users WHERE username = '{username}';"  # High risk of SQL injection
    results = execute_query(query)
    return {"results": results}

if __name__ == '__main__':
    app.run(debug=True)
