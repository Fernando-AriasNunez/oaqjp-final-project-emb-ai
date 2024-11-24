""" This module serves the server API """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# App innitiation
app = Flask('Emotion Detector')

@app.route('/')
def render_index_page():
    """ Function to render index page """
    return render_template('index.html')

@app.route('/emotionDetector')
def sent_detection():
    """ Function to handle emotionDetector route """
    # Extract text to analize
    text_to_analize = request.args.get('textToAnalyze')

    # Pass the request to the emotion_detector function
    response = emotion_detector(text_to_analize)

    # Client response construction
    # Error handling
    if response['dominant_emotion'] is None:
        client_response = "Invalid text! Please try again!"
    else:
        # Extract returned values and build client response
        client_response = (
            "For the given statement, the system response is" +
            " 'anger': " + str(response['anger']) +
            ", 'disgust': " + str(response['disgust']) +
            ", 'fear': " + str(response['fear']) +
            ", 'joy': " + str(response['joy']) +
            " and 'sadness': " + str(response['sadness']) +
            ". The dominant emotion is " + str(response['dominant_emotion'])
        )

    return client_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
