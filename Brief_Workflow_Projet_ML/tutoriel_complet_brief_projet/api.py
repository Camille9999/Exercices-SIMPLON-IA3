from typing import Union
from fastapi import FastAPI
import pandas as pd
import pickle
import numpy as np

app = FastAPI()

@app.get("/")
async def root(petal_width: Union[float, None] = 0, petal_length: Union[float, None] = 0, sepal_width: Union[float, None] = 0):  
  user_data = pd.DataFrame({"petal_width" : [float(petal_width)], "petal_length": [float(petal_length)], "sepal_width": [np.exp(float(sepal_width))]})  
  pickle_model = pickle.load(open('tutorial_pipeline.pkl', 'rb'))  
  pickle_predict = pickle_model.predict(user_data)
  return {'predict': f"{pickle_predict[0]}"}