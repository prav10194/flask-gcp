import os
from flask import Flask, jsonify, Response, render_template, request

productDictionary = {
      "Python": {
            "developedIn": "2012",
            "securityThreat": "Medium"
      },
      "JavaScript": {
            "developedIn": "1998",
            "securityThreat": "Low"
      }
}

def create_app():
  app = Flask(__name__)
  
  @app.route("/")
  def hello_world():
     return render_template('index.html')
  
  @app.route("/productInfo", methods = ['POST']) 
  def productInfo():
    if request.json["action"] == "search" and request.json["product"] in productDictionary:
        return {"code": "success", "message": productDictionary[request.json["product"]]}
    else:
        return {"code": "not found", "message": "Try Python or JavaScript as input"}

  return app
  
app = create_app()

if __name__ == "__main__":
  #    app = create_app()
  print(" Starting app...")
  app.run(host="0.0.0.0", port=5000)