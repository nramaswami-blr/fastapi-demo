from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Hello nCorium APIs"}

@app.get("/sensors")
def list_sensors():
    return [
        {"id" : "001", "name" : "Main Entrance"},
        {"id" : "002", "name" : "Basement 2 Parking"},
        {"id" : "003", "name" : "Rear Entrance"}
    ]
