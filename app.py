"""
Tuition Fee Tracking System - Flask Backend
"""
import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_folder='frontend', static_url_path='')
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default-secret-key')

# Enable CORS
CORS(app, supports_credentials=True)

# Initialize Supabase client
from db import supabase

if not supabase:
    print("\nWARNING: Supabase could not be initialized. Please check your .env file.\n")

# Register Blueprints
from routes.auth import auth_bp
from routes.students import students_bp
from routes.courses import courses_bp
from routes.fees import fees_bp
from routes.payments import payments_bp
from routes.dashboard import dashboard_bp
from routes.downloads import downloads_bp

app.register_blueprint(auth_bp)
app.register_blueprint(students_bp)
app.register_blueprint(courses_bp)
app.register_blueprint(fees_bp)
app.register_blueprint(payments_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(downloads_bp)


# Serve frontend pages
@app.route('/')
def serve_index():
    return send_from_directory('frontend', 'login.html')


@app.route('/<path:filename>')
def serve_frontend(filename):
    return send_from_directory('frontend', filename)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
