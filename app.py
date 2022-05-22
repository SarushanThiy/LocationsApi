from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions

from controllers import locations

app=Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return jsonify({'message': 'Hello from the api'}), 200

# Route to get all locations
@app.route('/locations', methods = ['GET'])
def users_handlers():
    fns = {
        'GET': locations.index, 
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

# Find all names
@app.route('/locations/names', methods=['GET'])
def locations_handlers_names():
    fns = {
        'GET': locations.show_names,
    }
    resp, code = fns[request.method](request)
    return jsonify (resp), code

# Find all countries
@app.route('/locations/countries', methods=['GET'])
def locations_handlers_countries():
    fns = {
        'GET': locations.show_countries,
    }
    resp, code = fns[request.method](request)
    return jsonify (resp), code

# Find all continents
@app.route('/locations/continents', methods=['GET'])
def locations_handlers_continents():
    fns = {
        'GET': locations.show_continents,
    }
    resp, code = fns[request.method](request)
    return jsonify (resp), code

# Find route by id
@app.route('/locations/<int:location_id>', methods=['GET'])
def locations_handlers(location_id):
    fns = {
        'GET': locations.show_by_id,
    }
    resp, code = fns[request.method](request, location_id)
    return jsonify(resp), code

# Find route by specific name
@app.route('/locations/<name>', methods=['GET'])
def locations_handlers_name(name):
    fns = {
        'GET': locations.show_by_name,
    }
    resp, code = fns[request.method](request, name)
    return jsonify(resp), code

# Find route by specific country
@app.route('/locations/<country>', methods=['GET'])
def locations_handlers_country(Country):
    fns = {
        'GET': locations.show_by_country,
    }
    resp, code = fns[request.method](request, Country)
    return jsonify(resp), code



# Handling Errors
@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops {err}'}, 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f'Oops cannot find the page {err}'}, 500

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f' Oops, {err}'}, 400
