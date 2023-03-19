# main.py

#this is a super simple main file to be improved

from preprocessing import preprocess_data
from model import train_model, make_predictions

# Load and preprocess the data
data = preprocess_data("data.csv")

# Train the model
model = train_model(data)

# Make predictions
predictions = make_predictions(model, data)

# Print the predictions
print(predictions)
