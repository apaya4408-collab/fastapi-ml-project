from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# 1. Load model RandomForest
model = joblib.load("HU_model_randomforest.pkl")

# 2. Buat FastAPI app
app = FastAPI(title="Prediksi HU dengan RandomForest")

# 3. Definisikan input data
class SensorData(BaseModel):
    Berat: float
    Cahaya: float
    R: float
    G: float
    B: float
    Hue: float
    Saturation: float
    Value: float
@app.get("/")
def read_root():
    return {"message": "API RandomForest HU sudah jalan!"}
# 4. Endpoint prediksi
@app.post("/predict")
def predict(data: SensorData):
    # Ubah input ke array sesuai urutan fitur
    input_data = np.array([[
        data.Berat,
        data.Cahaya,
        data.R,
        data.G,
        data.B,
        data.Hue,
        data.Saturation,
        data.Value
    ]])

    # Prediksi HU
    prediction = model.predict(input_data)[0]

    return {"predicted_HU": float(prediction)}
