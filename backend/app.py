from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from devcycle_integration import get_feature_flags
from api.leaderboard import get_leaderboard

app = Flask(__name__)
socketio = SocketIO(app)

# Fetch feature flags
feature_flags = get_feature_flags()

@app.route('/api/leaderboard', methods=['GET'])
def leaderboard():
    # Get real-time leaderboard data
    return jsonify(get_leaderboard())

@app.route('/api/vote', methods=['POST'])
def vote():
    # Handle player voting for events
    data = request.get_json()
    event = data['event']
    socketio.emit('vote_event', {'event': event})
    return jsonify({"status": "success", "event": event})

# WebSocket event handling for live updates
@socketio.on('connect')
def handle_connect():
    print("Client connected")
    emit('event_data', {'feature_flags': feature_flags})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
