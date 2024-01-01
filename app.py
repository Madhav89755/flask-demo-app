from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/",methods=['GET'])
def hi():
  return jsonify({"message":"This is a demo flask app"}

if '__name__' == 'main':
  app.run()
