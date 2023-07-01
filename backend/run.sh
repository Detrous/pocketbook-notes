echo "Running migrations..."
alembic upgrade head
echo "Running server..."

uvicorn --host 0.0.0.0 main:app