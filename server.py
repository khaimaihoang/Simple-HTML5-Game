from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle_update():
  update = request.get_json()
  chat_id = update.get("message").get("chat").get("id")

  # Optional: Store the chat_id for future use

  # Respond to the user with a message requesting chat ID
  telegram_bot_token = "7077622229:AAEFrSSmt_xcE3b5b0rYAqNtz_zwGNPrRGQ"
  message = "Please send me a message to get your chat ID."
  url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={chat_id}&text={message}"
  # Send the message using your preferred library (requests, urllib etc.)

  return "OK"

if __name__ == "__main__":
  app.run(debug=True)
