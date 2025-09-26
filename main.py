from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# 1. Load model KNN
model = joblib.load("KNN_model_prediksi_HU.pkl")

# 2. Buat FastAPI app
app = FastAPI(title="Prediksi HU dengan KNN")

# 3. Definisikan input data dari ESP32
class SensorData(BaseModel):
    Berat: float
    Cahaya: float
    R: float
    G: float
    B: float
    Hue: float
    Saturation: float
    Value: float

# 4. Endpoint untuk prediksi
@app.post("/predict")
def predict(data: SensorData):
    # ubah input ke numpy array sesuai urutan fitur
    input_data = np.array([[
        data.Berat, data.Cahaya, data.R, data.G,
        data.B, data.Hue, data.Saturation, data.Value
    ]])
    
    # prediksi HU
    prediction = model.predict(input_data)
    
    return {"predicted_HU": float(prediction[0])}
