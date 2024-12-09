Time Series Prediction with CatBoost (GUI)

This repository demonstrates a simple time series prediction application using the CatBoost library. The application includes a graphical user interface (GUI) built with Tkinter to make it easy for users to interact with the model.

Features

Input a time series manually.

Train a CatBoost regression model using the provided data.

Predict the next value in the time series.

Visualize the observed series and the predicted value in a plot.

Prerequisites

Before running the code, ensure you have the following installed:

Python 3.7+

Required libraries:

numpy

matplotlib

catboost

tkinter (comes pre-installed with Python)

Install the necessary libraries using pip:

pip install numpy matplotlib catboost

How to Run the Application

Clone this repository:

git clone https://github.com/yourusername/TimeSeriesPredictionGUI.git

Navigate to the project directory:

cd TimeSeriesPredictionGUI

Run the application:

python main.py

The GUI window will open. Enter your time series values, click the "Train and Predict" button, and view the results.

File Structure

main.py: The main Python script containing the GUI and time series prediction logic.

Usage

Enter Time Series Data:

Input a comma-separated list of numeric values in the text box (e.g., 1.0, 1.2, 1.5, 1.7).

Train and Predict:

Click the "Train and Predict" button to train the model and generate a prediction for the next time step.

Visualization:

The observed time series and the predicted next value will be displayed in a plot.

Example

Input:

Time Series: 1.0, 1.2, 1.5, 1.7, 1.6, 1.4, 1.3

Output:

Predicted Next Value: 1.28 (example output; varies depending on data)

A plot showing the observed series and the predicted value.

Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any feature additions or bug fixes.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

CatBoost Documentation

Python Community for Tkinter and data visualization tools.
