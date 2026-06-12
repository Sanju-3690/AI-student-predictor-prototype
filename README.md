# Student Marks Predictor

An AI-powered student marks prediction web app built using FastAPI, Streamlit, and Machine Learning.

---

## Features

- Predict student marks based on study hours
- Machine Learning model using Linear Regression
- FastAPI backend API
- Streamlit frontend UI
- Interactive prediction interface
- Data visualization using charts

---

## Technologies Used

- Python
- FastAPI
- Streamlit
- Scikit-learn
- Pandas
- Matplotlib
- Joblib

---

## Project Structure

```text
fastapi-ml-student-predictor/
│
├── main.py
├── app.py
├── train_model.py
├── student_model.pkl
├── requirements.txt
└── README.md
```

---

## Machine Learning Model

This project uses:
- Linear Regression

The model predicts student marks based on:
- study hours

---

## API Endpoint

### POST `/predict`

Example Input:

```json
{
  "hours": 5
}
```

Example Response:

```json
{
  "predicted_marks": 82.5
}
```

---

## Run Backend

```bash
uvicorn main:app --reload
```

Swagger Docs:

http://127.0.0.1:8000/docs

---

## Run Frontend

```bash
streamlit run app.py
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Application Architecture

```text
Streamlit Frontend
        ↓
FastAPI Backend
        ↓
Machine Learning Model
```

---

## Frontend Features

- Slider input
- Predict button
- Result display
- Bar chart visualization

---

## Author

"End-to-end ML web app demonstrating model deployment with FastAPI and Streamlit."
