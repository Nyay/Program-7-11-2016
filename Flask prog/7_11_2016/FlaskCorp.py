from flask import Flask
from flask import url_for, render_template, request, redirect
import re

app = Flask(__name__)

def opening():
    file = open('text.txt', 'r', encoding='UTF-8')
    arr = file.readlines()
    global arr
    file.close()
    return file

opening()

@app.route('/')
def main_page():
    urls = {'Ссылка на поиск': url_for('search'),
            }
    return render_template('main_page.html', urls=urls)

@app.route('/search')
def search():
    d = {}
    if request.args:
        submit = request.args['wordform']
        for str in arr:
            if submit in str:
                if submit in d:
                    d[submit].append(str)
                else:
                    d[submit]=[]
                    d[submit].append(str)
    return render_template('search.html', d=d)

if __name__ == '__main__':
    app.run(debug=True)