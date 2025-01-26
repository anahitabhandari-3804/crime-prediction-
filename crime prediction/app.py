from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataset
df = pd.read_csv(r'C:\Users\DELL\Desktop\crime prediction\crime_dataset_india24.csv')

# Normalize the dataset to avoid case-sensitivity issues
df['City'] = df['City'].astype(str).str.strip().str.title()  # Normalize city names
df['Crime Description'] = df['Crime Description'].astype(str).str.strip().str.upper()  # Normalize crime descriptions


@app.route('/', methods=['GET', 'POST'])
def index():
    # Get the list of unique cities and crime descriptions
    cities = df['City'].dropna().unique()
    crimes = df['Crime Description'].dropna().unique()

    prediction = None  # Default prediction value

    if request.method == 'POST':
        # Get the selected city and crime from the form
        city = request.form['city'].strip().title()
        crime = request.form['crime'].strip().upper()

        # Calculate the probability
        probabilities = df.groupby(['City', 'Crime Description']).size() / len(df)
        prediction = probabilities.get((city, crime), 0)  # Get probability or 0 if not found

        # Prepare a message for the prediction
        prediction = f"Predicted crime probability for {crime} in {city}: {round(prediction * 100, 2)}"

    return render_template('index.html', cities=cities, crimes=crimes, prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
