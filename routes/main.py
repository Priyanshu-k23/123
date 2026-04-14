from flask import Blueprint, render_template, send_from_directory, current_app
from models.models import Delivery

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/track/<int:delivery_id>')
def track_delivery(delivery_id):
    delivery = Delivery.query.get_or_404(delivery_id)
    # The template will use Socket.IO and Maps API for realtime tracking.
    return render_template('track_delivery.html', delivery=delivery)

@main_bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)
