import joblib
from tkinter import *

# Load trained model
model = joblib.load("cancer_model.pkl")

# Prediction function
def predict():
    try:
        values = [float(e.get()) for e in entries]
        result = model.predict([values])[0]

        if result == 0:
            output.set("CANCER")
        else:
            output.set("NO CANCER")

    except:
        output.set("Invalid Input")

# GUI setup
root = Tk()
root.title("Breast Cancer Prediction")

labels = [
    "radius_mean", "texture_mean", "perimeter_mean", "area_mean",
    "smoothness_mean", "compactness_mean", "concavity_mean",
    "concave points_mean", "symmetry_mean", "fractal_dimension_mean",
    "radius_se", "texture_se", "perimeter_se", "area_se",
    "smoothness_se", "compactness_se", "concavity_se",
    "concave points_se", "symmetry_se", "fractal_dimension_se",
    "radius_worst", "texture_worst", "perimeter_worst", "area_worst",
    "smoothness_worst", "compactness_worst", "concavity_worst",
    "concave points_worst", "symmetry_worst", "fractal_dimension_worst"
]

entries = []

for i, label in enumerate(labels):
    Label(root, text=label).grid(row=i, column=0)
    e = Entry(root)
    e.grid(row=i, column=1)
    entries.append(e)

Button(root, text="PREDICT", command=predict).grid(row=31, column=1)

output = StringVar()
Label(root, text="Result:").grid(row=32, column=0)
Entry(root, textvariable=output).grid(row=32, column=1)

root.mainloop()
