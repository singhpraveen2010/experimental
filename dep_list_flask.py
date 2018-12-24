import sys
import json
import flask
from flask import Flask, request
from flask_cors import CORS


if sys.version_info.major == 2:
    reload(sys)
    sys.setdefaultencoding('UTF8')


app = Flask(__name__)
CORS(app)


@app.route('/')
def heart_beat():
    return flask.jsonify({"status": "ok"})


@app.route('/api/v1/get_dep', methods=['GET'])
def get_path():
    with open("dev-stack-analysis-clean-data/maven/github/data_kronos_dependency/kronos_dependency_maven.json", "r") as f:
        data = json.load(f)
    return flask.jsonify(data['kronos_edge_list'])


if __name__ == "__main__":
    app.run(port=8080)
