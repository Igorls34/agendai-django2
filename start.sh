#!/bin/bash
set -e

echo "🚀 Starting AgendAI Django Application..."

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Seed demo data
python manage.py seed_demo

echo "✅ Application ready!"
echo "🌐 Starting server..."

# Start the server
python manage.py runserver 0.0.0.0:$PORT --noreload
