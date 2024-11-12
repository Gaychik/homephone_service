from flask import Flask,jsonify,request
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  


@app.get("/users")
def users():
    return "Load Data..."

@app.post("/users")
def create_user():
    pass 

@app.delete("/users")
def remove_user():
    pass


if __name__=="__main__":
    app.run(port=5001,debug=True)
