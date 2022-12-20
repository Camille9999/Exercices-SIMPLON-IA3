from typing import Union
from fastapi import FastAPI
from pandas import DataFrame
from numpy import log
import pickle

app = FastAPI()

class CustomUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        if name == 'ModeleLineaire':
            from LinearModel import ModeleLineaire
            return ModeleLineaire
        return super().find_class(module, name)

pickled_model = CustomUnpickler(open('life_expectancy_model.pkl', 'rb')).load()


@app.get("/")
def read_root(drink: Union[float, None] = None,
              income: Union[float, None] = None,
              hiv: Union[float, None] = None):

    X = DataFrame({'People using at least basic drinking water services' : [drink],
                   'Income composition of resources' : [income],
                   'HIV/AIDS' : [log(hiv)]})

    pred = pickled_model.prediction(X)[0]

    return {'prediction' : round(pred)}
