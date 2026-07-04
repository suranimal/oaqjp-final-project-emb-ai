"""
Server module for the Emotion Detection application.
Provides routes to render the user interface and analyze input text
using the EmotionDetection package wrapper around the Watson NLP API.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():
    """
    Route to analyze the text received from the user interface
    and return a formatted string response with error handling.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector function
    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion from the response
    dominant_emotion = response['dominant_emotion']

    # Error handling when the dominant_emotion is None (blank entry scenario)
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Extract the emotion scores if valid data exists
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    # Format the exact string response requested by the customer
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Route to render the main HTML webpage interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Deploy the application on localhost:5000
    app.run(host="0.0.0.0", port=5000)
    