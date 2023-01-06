from typing import Union
from fastapi import FastAPI
from pandas import DataFrame
from pickle import Unpickler
import numpy as np



app = FastAPI()

pickled_model = Unpickler(open('life_expectancy_model.pkl', 'rb')).load()


@app.get("/")
def read_root(drink: Union[float, None] = None,
              income: Union[float, None] = None,
              hiv: Union[float, None] = None):

    X = DataFrame({'People using at least basic drinking water services' : [drink],
                   'Income composition of resources' : [income],
                   'HIV/AIDS' : [np.log(hiv)]})

    pred = pickled_model.predict(X)[0]

    return {'prediction' : round(pred)}
