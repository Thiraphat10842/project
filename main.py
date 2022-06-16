import uvicorn
from fastapi import FastAPI
from action import Action



app = FastAPI()

@app.get("/add_hw_name")
async def insertHW(name, hw_name):
    data = Action.insertHW(name, hw_name)
    return data

@app.get("/hw/update_status_hw")
async def hw_update_status_hw(ID, status):
    data = Action.updateStatusHW(ID, status)
    return data

@app.get("/hw/update_value_hw")
async def hw_update_status_hw(ID, value):
    data = Action.updateValueHW(ID, value)
    return data

@app.get("/delete_hw")
async def DeleteHW(ID):
    data = Action.DeleteHW(ID)
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="192.168.90.190", port=80)