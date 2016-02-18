#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask, jsonify, redirect, render_template, request

class CustomFlask(Flask):
    jinja_options = dict(Flask.jinja_options)
    jinja_options.update(dict(
        variable_start_string='{$',
        variable_end_string='$}'
    ))

app = CustomFlask(__name__)


@app.route('/')
def index():
    return render_template('index.html', a=111)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9401)
