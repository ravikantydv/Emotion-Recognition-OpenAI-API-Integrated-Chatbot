from flask import Flask, request, render_template
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = Flask(__name__)

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(r"C:\Users\hp\Documents\DataScientist\PaidAssignments\urdoer\Inprogress\Emotion recognition\tokenizer")
model = AutoModelForSequenceClassification.from_pretrained(r"C:\Users\hp\Documents\DataScientist\PaidAssignments\urdoer\Inprogress\Emotion recognition\trained_model")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        print("Received text:", text)

        # Set pad token if not already defined
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        # Tokenize and predict
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)

        # Print the raw logits for debugging
        print("Raw logits:", outputs.logits)

        # Calculate probabilities
        probs = torch.sigmoid(outputs.logits)
        print("Probabilities:", probs)

        # Determine predicted labels based on threshold
        predictions = (probs > 0.5).int().tolist()[0]  # Change threshold to 0.5
        print("Predicted binary labels:", predictions)

        # Map binary predictions to labels
        actual_labels = ['negative', 'positive']  # Change order to map correctly
        predicted_labels = [actual_labels[i] for i in range(len(predictions)) if predictions[i] == 1]
        
        if not predicted_labels:
            predicted_labels = ["Negative (Not Happy)"]  # Default to negative if no positive predictions

        print("Predicted labels:", predicted_labels)

        return render_template('index.html', predictions=predicted_labels)



if __name__ == "__main__":
    app.run(debug=True)
