from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

@app.route('/')
def index():
    resp = requests.get(
        url='http://127.0.0.1:9080/crawl.json?start_requests=true&spider_name=steam'
    ).json()

    items = resp.get('items')
    
    return render_template('index.html', games=items)

# @app.route('/show')
# def show_template():
#     users = [
#         'User 1',
#         'John Doe',
#         'Franz'
#     ]
#     return render_template('index.html', users=users)


if __name__ == "__main__":
    app.run(debug=True)