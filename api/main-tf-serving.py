from fastapi import FastAPI, UploadFile, File
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import requests
import tensorflow as tf

app = FastAPI()

endpoint = "http://localhost:8501/v1/modelspotatoes_model:predict"
CLASS_NAMES = ["Early Blight","Late Blight","Healthy"]

@app.get("/ping")
async def ping():
    return "Hello i am alive"

def read_file_as_image(data)->np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(
        file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image,0)

    json_data = {
        "instances" : img_batch.tolist()
    }

    response = requests.post(endpoint, json=json_data)
    prediction = response.json()["predictions"][0]
    index = np.argmax(prediction)

    class_name = CLASS_NAMES[index]

    return {
        "class" : class_name
    }

if __name__ == "__main__":
    uvicorn.run(app,host='localhost',port=8000)
