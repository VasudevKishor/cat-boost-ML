import numpy as np
import matplotlib.pyplot as plt
from catboost import CatBoostRegressor

# Define the observed time series
observed_series = [1.0, 1.2, 1.5, 1.7, 1.6, 1.4, 1.3]

# Prepare the data for supervised learning
def prepare_data(series, window_size):
    X, y = [], []
    for i in range(len(series) - window_size):
        X.append(series[i:i + window_size])
        y.append(series[i + window_size])
    return np.array(X), np.array(y)

# Parameters
window_size = 3  # Number of past observations to use as features

# Prepare the training data
X, y = prepare_data(observed_series, window_size)

# Train a CatBoost model
model = CatBoostRegressor(iterations=100, depth=3, learning_rate=0.1, verbose=0)
model.fit(X, y)

# Predict the next value
last_window = observed_series[-window_size:]  # Use the last 'window_size' values as input
predicted_next_value = model.predict([last_window])[0]

# Append the predicted value to the observed series for visualization
extended_series = observed_series + [predicted_next_value]

# Plot the observed series and predicted value
plt.figure(figsize=(10, 6))
plt.plot(range(len(observed_series)), observed_series, marker='o', label="Observed Series", color='blue')
plt.plot(len(observed_series), predicted_next_value, marker='x', markersize=10, color='red', label="Predicted Next Value")
plt.axvline(x=len(observed_series) - 1, color='gray', linestyle='--', alpha=0.7, label="Prediction Point")
plt.title("Time Series Prediction with CatBoost")
plt.xlabel("Time Step")
plt.ylabel("Value")
plt.legend()
plt.grid()
plt.show()
