from . import app
from fastapi import UploadFile, File, HTTPException
import cv2
from cifar10 import Model
import numpy as np

model = Model()

ALLOW_EXTENSION = ['jpg', 'jpeg', 'png', ]

@app.get('/')
def index():
    return {'message': 'Hello, World!'}

@app.post('/analyze_image')
async def analyze_image(file: UploadFile = File(...)):
    '''
        Analyze image and return the result

        Args:
            file (UploadFile): image file

        Returns:
            dict: result
    '''
    extension = file.filename.split('.')[-1].lower()

    if extension not in ALLOW_EXTENSION:
        raise HTTPException(status_code=400, detail='File extension not allowed')
    
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    result = model.predict(img)

    return {'predict': result}