# -*- coding: utf-8 -*-


from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return "hello world!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80
            #      , debug=True
            )
