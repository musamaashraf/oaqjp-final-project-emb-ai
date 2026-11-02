"""
Emotion Detection Server
This script initiates a Flask server to detect emotions in text provided by users.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Analyzes the text passed via GET parameter 'textToAnalyze'
    and returns a formatted string of emotions and dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Analyze the emotion of the input text
    response = emotion_detector(text_to_analyze)

    # Extract dominant emotion
    dominant_emotion = response['dominant_emotion']

    # Check if the dominant emotion is None
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Extract individual emotions
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    # Return formatted response string
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is <b>{dominant_emotion}.</b>"
    )

@app.route("/")
def render_index_page():
    """
    Renders the main application index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
