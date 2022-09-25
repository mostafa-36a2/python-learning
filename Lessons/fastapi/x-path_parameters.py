from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}/{para1}/para2/{para3}/{para4}")
async def read_item(item_id, para1, para3, para4):
    return {"item_id": item_id, "params": [para1, para3, para4]}


# Example request: http://127.0.0.1:8000/items/hello/12/para2/14/15
# Example response: {"item_id":"hello","params":["12","14","15"]}
