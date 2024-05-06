from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace 'high_scores.txt' with your desired file for storing scores
HIGH_SCORES_FILE = 'high_scores.txt'

def get_high_score():
  try:
    with open(HIGH_SCORES_FILE, 'r') as f:
      return int(f.read().strip())
  except FileNotFoundError:
    return 0

def set_high_score(score):
  with open(HIGH_SCORES_FILE, 'w') as f:
    f.write(str(score))

@app.route('/get_high_score', methods=['GET'])
def get_high_score_route():
  high_score = get_high_score()
  return jsonify({'highScore': high_score})

@app.route('/set_high_score', methods=['POST'])
def set_high_score_route():
  data = request.get_json()
  if data and 'score' in data:
    new_score = data['score']
    if new_score > get_high_score():
      set_high_score(new_score)
  return jsonify({'message': 'High score updated!'})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)  # You can change the port if needed
