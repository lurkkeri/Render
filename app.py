import os
os.system('pip install scikit-learn')  # Temporary workaround for troubleshooting

from flask import Flask, request, jsonify
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re

app = Flask(__name__)

# Ensure the necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Define the preprocessing function
def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    
    # Remove non-alphabetic characters and lower the case
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    
    # Tokenize and remove stopwords
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    
    # Lemmatize tokens
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    return ' '.join(tokens)

# Load the pickled model
model = joblib.load('spam_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    input_data = request.json['sentence']
    
    # Perform preprocessing on the input data
    processed_data = preprocess_text(input_data)
    
    # Make predictions using the loaded model
    prediction = model.predict([processed_data])[0]
    
    # Convert the prediction result to human-readable format
    result = 'Spam' if prediction == 1 else 'Ham'
    
    # Return the prediction result as JSON
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
