import pickle

# Load the trained model from the file
with open('trained_model.pkl', 'rb') as f:
    trained_model = pickle.load(f)

# Use the trained model to make predictions on new data
predictions = trained_model.predict(new_data)

# Print the predictions
print(predictions)
