import numpy as np
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

# --- generate + save synthetic dataset ---
np.random.seed(42)
hours = np.random.uniform(1, 10, 300)
marks = 8 * hours + np.random.normal(0, 5, 300)
marks = np.clip(marks, 10, 100)

df = pd.DataFrame({"hours": hours, "marks": marks})
df.to_csv("student_data.csv", index=False)
print("Dataset saved → student_data.csv")
# --- train model ---
X = df[["hours"]]
y = df["marks"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# --- metrics ---
r2  = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"R² Score : {r2:.4f}")
print(f"MAE      : {mae:.2f} marks")
# --- save model ---
joblib.dump(model, "student_model.pkl")
print("Model saved → student_model.pkl")