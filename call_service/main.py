from flask import Flask,jsonify,request
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  


@app.post("/call")
def call():
    return "Call..."

@app.get("/call/history")
def history():
    pass 

@app.get("/call/history/last")
def get_call_last_some():
    pass


if __name__=="__main__":
    app.run(port=5002,debug=True)
