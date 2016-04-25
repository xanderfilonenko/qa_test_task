#!flask/bin/python
from flask import Flask, jsonify, make_response, abort, request, send_file
import os, logging

app = Flask(__name__)

candidates = []

@app.route('/candidates', methods=['GET'])
def get_candidates():
    return jsonify({'candidates': candidates})

@app.route('/candidates/<int:cand_id>', methods=['GET'])
def get_candidate(cand_id):
    candidate = filter(lambda t: t['id'] == cand_id, candidates)
    if len(candidate) == 0:
        abort(404)
    return jsonify({'candidate': candidates[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Incorrect URL'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': error.description}), 400)

@app.route('/candidates', methods=['POST'])
def create_candidate():
    if not request.json:
        abort(400, 'Incorrect header! Make sure your Content-Type header is application/json!')
    if not 'name' in request.json:
        abort(400, 'Name is absent in your request body!')
    if len(candidates)==0:
        candidate_id = 1
    else:
        candidate_id=candidates[len(candidates)-1]['id'] + 1
    candidate = {
        'id': candidate_id,
        'name': request.json['name'],
        'position': request.json.get('position', ""),
    }
    candidates.append(candidate)
    return jsonify({'candidate': candidate}), 201

@app.route('/candidates/<int:cand_id>', methods=['DELETE'])
def delete_candidate(cand_id):
    candidate = filter(lambda t: t['id'] == cand_id, candidates)
    if len(candidate) == 0:
        abort(404)
    candidates.remove(candidate[0])
    return jsonify({'result': True})

@app.route("/download/<file_name>")
def getFile(file_name):
    if os.path.isfile(file_name) is False:
        abort(400, 'No such file!')
    return send_file(file_name, as_attachment=True)

if __name__ == '__main__':
    logging.basicConfig(filename='flask.log',level=logging.DEBUG)
    app.run(debug=True, port=80, host='0.0.0.0')
