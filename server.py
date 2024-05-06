from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# In-memory storage for high scores
high_scores = {}

@app.route('/highscore', methods=['GET', 'POST'])
def handle_highscore():
    chat_id = request.args.get('chat_id')
    if request.method == 'POST':
        # Store the high score
        high_scores[chat_id] = request.json['score']
        return jsonify(success=True)
    else:
        # Retrieve the high score
        return jsonify(score=high_scores.get(chat_id, 0))

if __name__ == '__main__':
    app.run(port=5000)
