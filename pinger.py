from flask import Flask
import threading
import time
import requests

# ------------------------------
# CONFIGURATION
# ------------------------------
TARGET_URL = "https://254kenyasafaris.africa/health"  # replace with your main site's /health
PING_INTERVAL = 8 * 60  # 8 minutes in seconds

# ------------------------------
# FLASK APP
# ------------------------------
app = Flask(__name__)

@app.route("/health")
def health():
    """Health check for the pinger site itself."""
    return "Pinger site is running!", 200

# ------------------------------
# PING LOGIC
# ------------------------------
def ping_target():
    """Continuously ping the target website every 8 minutes."""
    while True:
        try:
            response = requests.get(TARGET_URL)
            print(f"Pinged {TARGET_URL} - Status code: {response.status_code}")
        except Exception as e:
            print(f"Error pinging {TARGET_URL}: {e}")
        time.sleep(PING_INTERVAL)

def start_pinger():
    """Start pinging in a background thread."""
    thread = threading.Thread(target=ping_target, daemon=True)
    thread.start()

# ------------------------------
# START FLASK AND PINGER
# ------------------------------
if __name__ == "__main__":
    start_pinger()       # start the ping thread
    app.run(debug=True)  # start the Flask app
