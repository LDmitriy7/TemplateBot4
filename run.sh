source .env

if [ $APP_ENV = "development" ]; then
  nodemon src/app.py
elif [ $APP_ENV = "production" ]; then
  docker compose build && docker compose up -d
else
  echo "\$APP_ENV must be development/production"
fi
