from fastapi import FastAPI, UploadFile, File, HTTPException
from app.models.model import train_model, make_prediction
from app.schemas.data_schema import PredictionInput
from app.utils.file_utils import save_file

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Manufacturing Predictive API"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = save_file(file)
        return {"message": "File uploaded successfully", "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/train")
async def train():
    try:
        metrics = train_model()
        return {"message": "Model trained successfully", "metrics": metrics}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict")
async def predict(data: PredictionInput):
    try:
        result = make_prediction(data.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
