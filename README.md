# House Price Prediction Application

This is a Flask-based web application that predicts house prices in Chennai based on various features. The model used for prediction is a Ridge Regression model that has been pre-trained and saved as a pickle file.

## Features

- Predict house prices based on area, number of bedrooms, number of bathrooms, and square footage.
- User-friendly web interface to input features and get predictions.

## How to Run

### Prerequisites

- Python 3.x
- Flask
- pandas
- numpy
- pickle5

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/house-price-prediction.git
   cd house-price-prediction
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Ensure the following files are present in the project directory:**

   - `Final_Chennai_House_Data.csv`
   - `RidgeModel.pkl`
   - `templates/index.html`

### Running the Application

1. **Run the Flask application:**

   ```sh
   python3 main.py
   ```

2. **Access the application:**

   Open a web browser and navigate to `http://127.0.0.1:5001/` to access the application.

## Demo

## Notes

- Ensure that your CSV file and pickle model are correctly placed in the project directory.
