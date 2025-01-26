# crime-prediction-
This project is a Flask-based web application that predicts the probability of a specific crime occurring in a given city. It uses a dataset containing crime statistics from various cities in India to calculate probabilities.

Features
Interactive User Interface: Users can select a city and crime from dropdown menus.
Crime Probability Prediction: Displays the predicted probability of a crime based on the dataset.
Responsive Design: Built using Bootstrap for a clean and responsive layout.
Data Normalization: Handles case-sensitivity issues in city and crime descriptions.
Project Structure
bash
Copy
Edit
![image](https://github.com/user-attachments/assets/de47b28d-6440-4500-b2e7-4c095c75cf42)


Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/crime-prediction.git
cd crime-prediction
Install required Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask application:

bash
Copy
Edit
python app.py
Open your browser and navigate to:

arduino
Copy
Edit
http://127.0.0.1:5000
Dataset
The dataset crime_dataset_india24.csv contains the following key columns:

City: Name of the city where the crime occurred.
Crime Description: Description of the type of crime.
Other relevant fields.
Ensure that the dataset is located in the same directory as app.py.

How It Works
The user selects a city and a crime type from the dropdowns.
The app calculates the probability of the selected crime in the chosen city using frequency analysis from the dataset.
The prediction is displayed as a percentage on the web page.
Screenshots

Example of the homepage with city and crime dropdowns.
![image](https://github.com/user-attachments/assets/5d872b55-6171-4f3a-a350-04a1f73e4d11)


Technologies Used
Backend: Flask, Python
Frontend: HTML, CSS, Bootstrap
Data Handling: Pandas
Dataset: Crime statistics (India)
Contributing
Contributions are welcome! If you'd like to improve this project:

Fork the repository.
Create a feature branch: git checkout -b feature-name.
Commit your changes: git commit -m "Add feature".
Push the branch: git push origin feature-name.
Open a pull request.
License
