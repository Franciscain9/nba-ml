from flask import Flask
from flask_restful import Resource, Api
import sys
import os


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/api/evaluate', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if operation == 'add':
            sum = float(num1) + float(num2)
            return render_template('index.html', sum=sum)

        elif operation == 'subtract':
            sum = float(num1) - float(num2)
            return render_template('index.html', sum=sum)

        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            return render_template('index.html', sum=sum)

        elif operation == 'divide':
            sum = float(num1) / float(num2)
            return render_template('index.html', sum=sum)
        else:
            return render_template('index.html')


if __name__ == ' __main__':
    app.run(host="0.0.0.0", port=port)
