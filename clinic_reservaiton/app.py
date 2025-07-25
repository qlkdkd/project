from flask import Flask, render_template, request, redirect, jsonify
from models import db, Reservation
from collections import Counter
from datetime import datetime

# Flask 세팅
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chart-data')
def chart_data():
    reservations = Reservation.query.all()
    
    time_slots = [r.time for r in reservations]
    room_usage = [r.room for r in reservations]
    
    time_counter = Counter(time_slots)
    room_counter = Counter(room_usage)
    
    return jsonify({
        'time_labels': list(time_counter.keys()),
        'time_values': list(time_counter.values()),
        'room_labels': list(room_counter.keys()),
        'room_values': list(room_counter.values()),
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
