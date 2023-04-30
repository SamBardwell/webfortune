from flask import (
    abort, Flask, jsonify, redirect, render_template, request,
    session, url_for
)
app = Flask(__name__)
import subprocess

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    process = subprocess.run(
                            ['fortune'],
                            stdout=subprocess.PIPE,
                            universal_newlines=True
                            )
    return '<pre>' + process.stdout + '</pre>'

@app.route('/cowsay/<message>/')
def cowsay(message):
    process = subprocess.run(
                            ['cowsay', message],
                            stdout=subprocess.PIPE,
                            universal_newlines=True
                            )
    return '<pre>' + process.stdout + '</pre>'

@app.route('/cowfortune/')
def cowfortune():
    process1 = subprocess.run(
                            ['fortune'],
                            stdout=subprocess.PIPE,
                            universal_newlines=True
                            )
    process = subprocess.run(
                            f'cowsay {process1.stdout}',
                            stdout=subprocess.PIPE,
                            shell=True,
                            universal_newlines=True
                            )
    
    return '<pre>' + process.stdout + '</pre>'
