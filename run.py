#!/usr/bin/python3

# based on https://github.com/dpgaspar/Flask-AppBuilder/tree/master/examples/mongoimages

from app import app

app.run(host='0.0.0.0', port=8086, debug=True)

