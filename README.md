# AIIntern1
# Manufacturing Predictive API

## Overview
This is a FastAPI-based API designed to predict downtime in manufacturing systems using machine learning models. The model is trained on a dataset containing two main features:
- **Temperature**
- **Run Time**

The model is trained using the Decision tree algorithm for predicting the **Downtime_Flag** based on the features provided.

## Requirements
Before you can run this API, ensure you have the following:
- Python 3.7+
- `pip` (Python's package installer)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://your-repository-url.git
    cd your-repository-directory
    ```

2. **Install dependencies**:
    Use the following command to install the required packages:
    ```bash
    pip install -r requirements.txt
    ```


   The `requirements.txt` file should include dependencies like `fastapi`, `scikit-learn`, `joblib`, and others required for this project.

## Setting up and Running the API

1. **Start the API server**:
   Run the FastAPI server with the following command:
   ```bash
   uvicorn app.main:app --reload

2. **Upload the dataset file**:
   Type command "curl -X POST "http://127.0.0.1:8000/upload" -F "file=@data/dataset_500_balanced.csv""
   This is only the name of the dataset: dataset_500_balanced.csv

   Here is the sample 
   $  curl -X POST "http://127.0.0.1:8000/upload" -F "file=@data/dataset_500_balanced.csv"
   {"message":"File uploaded successfully","file_path":"data/dataset_500_balanced.csv"}

3. **Train the model**:
   Type command "curl -X POST "http://127.0.0.1:8000/train""

   Here is the sample 
   $ curl -X POST "http://127.0.0.1:8000/train"
   {"message":"Model trained successfully","metrics":{"accuracy":0.52,"f1_score":0.5}}

4. **Predict the data**:
   Type command "curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"Temperature": 75.0, "Run_Time": 150}'
"
   Here is the sample 
   $ curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"Temperature": 75.0, "Run_Time": 150}'
   {"Downtime":"Yes","Confidence":1.0}
