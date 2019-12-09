from flask import Flask, request, abort, make_response, jsonify
import json
from urllib.parse import urlparse

base =[{"name": "datacenter-1", "metadata": {"monitoring": {"enabled": "true"},"limits": {"cpu": {"enabled": "false","value": "300m"}}}}, {"name": "datacenter-2","metadata": {"monitoring": {"enabled": "true"},"limits": {"cpu": {"enabled": "true","value": "250m"}}}}]




app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1> Api Heart Beat</h1?"
#read all
@app.route('/configs', methods=['GET'])
def config():
    #result = json.dumps(base)
    return jsonify({'base': base})
    #return "<p>{}</p>",result

#read one
@app.route('/configs/<name>',methods=['GET'])
def read_one(name):
    task = [task for task in base if task['name'] == name]
    if len(task) == 0:
           abort(404)
    return jsonify({name: task[0]})

@app.route('/configs', methods=['POST'])
#create one
def create(name):
        if not request.json or not 'name' in request.json:
            abort(400)
        task = {
            'name': request.json['name'],
            'metadata': request.json.get('metadata', ""),

        }
        base.append(task)
        return jsonify({name: task}), 201

#update
@app.route('/configs',methods = ['PUT','PATCH'])
def update(name):
    task = [task for task in base if task['name'] == name]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'metadata' in request.json:
        abort(400)

    task[0]['name'] = request.json.get('name', task[0]['name'])
    task[0]['metadata'] = request.json.get('metadata', task[0]['metadata'])
    return jsonify({name: task[0]})

#delete
@app.route('/configs',methods = ['DELETE'])
def delete(name):
    task = [task for task in base if task['name'] == name]
    if len(task) == 0:
        abort(404)
    base.remove(task[0])
    return jsonify({'result': True})

@app.route('/search',methods = ['GET'])
def search():
    url = request.url
    u = urlparse(url)
    query = u.query
    ss = query.split("=")
    key = ss[0]
    print(key)
    value = ss[1]
    print(value)
    for i in range(len(base)):
        if key == value in base[i]:
            print(base[i])
            return base[i]


if __name__ == "__main__":
Port = int(os.environ['PORT'])
app.run(host='0.0.0.0', port=Port)
