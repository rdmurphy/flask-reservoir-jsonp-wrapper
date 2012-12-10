import os
import requests
from flask import Flask, request

app = Flask(__name__)
RESERVOIR_JSON = 'http://waterdatafortexas.org/reservoirs/recent-conditions.json'


@app.route('/reservoirs.json')
def get_reservoir_json():
    r = requests.get(RESERVOIR_JSON)
    return '{0}({1})'.format(request.args.get('callback'), r.text)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
