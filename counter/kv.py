# Simple persistent key-value store
#
# Inspired by <https://docs.repl.it/misc/database>
#
#     $ FLASK_APP=kv APP_CONFIG=kv.cfg flask run
#     $ export DB_URL=localhost:5000
#

import shelve

from flask import Flask, g, request, jsonify

app = Flask(__name__)
app.config.from_envvar('APP_CONFIG')

DB = {}


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        backing_store = app.config.get('DBM', ':memory:')
        if backing_store == ':memory:':
            db = DB
        else:
            db = shelve.open(backing_store)
        g._database = db
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        if not isinstance(db, dict):
            db.close()

# Set
# http $DB_URL foo=bar
@app.route('/', methods=['POST'])
def set_key():
    req = request.get_json()
    if not req:
        req = request.form
    for key in req.keys():
        get_db()[key] = req[key]
    return jsonify(req)

# Get
# http $DB_URL/foo
@app.route('/<key>')
def get_key(key):
    return jsonify({key: get_db().get(key)})
    
# Get
# http $DB_URL/allkeysandvalues

# Use requests to write a Python dump.py to connect to
# the kv.py service and display all of its keys and values.
@app.route('/')
def all_keys_values():

	all_keys_values_list = []
	
	for key, value in get_db().items():
		all_keys_values_list.append({key : value})
	return jsonify(all_keys_values_list)

# Delete
# http DELETE $DB_URL/foo
@app.route('/<key>', methods=['DELETE'])
def delete_key(key):
    return jsonify({key: get_db().pop(key, None)})


# List
# http $DB_URL
# http $DB_URL?prefix=f
@app.route('/')
def match():
    keys = get_db().keys()
    prefix = request.args.get('prefix')
    if prefix:
        matches = [k for k in keys if k.startswith(prefix)]
    else:
        matches = list(keys)
    return jsonify({'keys': matches})
