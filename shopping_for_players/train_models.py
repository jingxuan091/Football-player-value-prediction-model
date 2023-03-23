import pickle
from preprocessing import preprocess_data
from models import train_model

mydata="../rawdata/appearances.csv"

# Load and preprocess the data
data = preprocess_data(mydata)

# Train the model
model = train_model(data)

# Load the trained model from the file
with open('trained_model.pkl', 'wb') as f:
    trained_model = pickle.dump(model,f)
