from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

@app.get("/prediction/{user_input}")
async def read_root(user_input: str):
    print(user_input)
    scaler_deploy = pickle.load(open('scaler_deploy.pkl', 'rb'))
    pickled_model = pickle.load(open('model_deploy.pkl', 'rb'))
    X_user = pd.DataFrame({"total_bill": [user_input]})
    X_user_scaled = scaler_deploy.transform(X_user)
    pred = pickled_model.predict(X_user_scaled)
    # import ipdb; ipdb.set_trace()
    return {"pred": round(pred[0])}
