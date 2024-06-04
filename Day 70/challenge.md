#### Day 70: Deploying Your Web Application with Heroku
**Challenge:** Deploy your Flask application to Heroku.

1. Install Heroku CLI and login.
2. Create a `Procfile` in your project directory.
3. Add a `requirements.txt` file.
4. Commit your changes and push to Heroku.

```bash
# Procfile
web: gunicorn app:app
```

```bash
# requirements.txt
Flask==2.0.1
gunicorn==20.1.0
Flask-SQLAlchemy==2.5.1
Flask-Login==0.5.0


```

```bash
# Terminal commands
$ heroku login
$ heroku create your-app-name
$ git add .
$ git commit -m "Deploy to Heroku"
$ git push heroku master
$ heroku open
```


