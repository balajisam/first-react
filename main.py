import flask

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    """ Welcome to automated CI/CD integrating github with Cloud Source, Cloud Build & deploying to App Engine. """
    return "Hello World!\n"


if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)
