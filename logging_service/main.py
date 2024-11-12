from flask import Flask,jsonify,request
app = Flask(__name__)

@app.post("/log/user")
def set_log_user():
    return "Logging User..."

@app.post("/log/call")
def set_log_call():
    return "Logging Call..."


#В теле запроса будет передаваться период времени за который нужно получить логи 
@app.get("/log/calls")
def calls():
     pass

@app.get("/log/users")
def users():
     pass

if __name__=="__main__":
    app.run(port=5004,debug=True)
