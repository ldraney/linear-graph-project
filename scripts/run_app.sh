# scripts/run_app.sh
gunicorn -b :8050 app:server

