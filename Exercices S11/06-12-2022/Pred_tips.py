from typing import Union
from fastapi import FastAPI
from pandas import DataFrame
import pickle

app = FastAPI()


@app.get("/")
def read_root(
    size: Union[int, None] = None,
    total_bill: Union[int, None] = None,
    sex: Union[str, None] = None,
    smoker: Union[str, None] = None,
    day: Union[str, None] = None,
    time: Union[str, None] = None
    ):

    pickled_model = pickle.load(open('pipeline.pkl', 'rb'))
    X = DataFrame({"size" : [size], "total_bill" : [total_bill], "sex" : [sex], "smoker" : [smoker], "day" : [day], "time" : [time]})
    pred = pickled_model.predict(X)[0]

    return {'prediction' : round(pred, 2)}
