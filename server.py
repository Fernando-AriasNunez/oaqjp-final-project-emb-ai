from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# App innitiation
app = Flask('Emotion Detector')

@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def sent_detection():
    # Extract text to analize
    text_to_analize = request.args.get('textToAnalyze')

    # Pass the request to the emotion_detector function
    response = emotion_detector(text_to_analize)

    # Extract returned values and build client response
    client_response = f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

    return client_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
