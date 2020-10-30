from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
import json

templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)
with open('data.json') as file_json:
    FileJson = json.load(file_json)

def mensaje():
  mensaje = 'Bienvenido'
  return "alert('" + mensaje + "')"

@app.route('/')
def index():
  temp = environment.get_template('index.html')
  return temp.render(my_data = FileJson['data'], headers = FileJson['headers'])

@app.route('/crear', methods = ['GET', 'POST'])
def crear():
  if request.method == 'POST':
    _id = request.form['id']
    _type = request.form['type']
    _name = request.form['name']
    _image = request.form['image']
    _thumbnail = request.form['thumbnail']
    print (f'{_id} {_type} {_name} {_image} {_thumbnail}')

    FileJson['data'].append({"id":_id, "type":_type, "name":_name, "image":{"url":_image}, "thumbnail":{"url":_thumbnail}})
    return redirect(url_for('index'))
  template = environment.get_template('form.html')
  return template.render()


@app.route('/Nombre')
def nombre():
  return 'Jose Reyes'

@app.route('/Edad')
def edad():
  return '19'

@app.route('/Carnet')
def carnet():
  return '20200201'

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)