from flask import Flask,jsonify,request
from redis import Redis
app = Flask(__name__)
cache = Redis(port=6379,db=0)

@app.post("/cache/user")
def cache_user():
    return "Caching User ... "

@app.get("/cache/user")
def get_user_from_cache():
    pass 

@app.post("/cache/call")
def cache_call():
    return "Caching Call ... "

@app.get("/cache/call")
def get_call_result_from_cache():
    pass 


if __name__=="__main__":
    app.run(port=5003,debug=True)
