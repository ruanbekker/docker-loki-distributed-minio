from flask import Flask, request
from flask.logging import default_handler
import logging

app = Flask(__name__)

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)
app.logger.setLevel(logging.INFO)
default_handler.setFormatter(
    logging.Formatter(
        'time="%(asctime)s" service=%(name)s level=%(levelname)s %(message)s'
    )
)

@app.route("/")
def home():
    return "ok"

@app.after_request
def after_request(response):
    app.logger.info(
        'addr="%s" method=%s scheme=%s path="%s" status=%s',
        request.remote_addr,
        request.method,
        request.scheme,
        request.full_path,
        response.status_code,
    )
    return response

if __name__ == '__main__':
    app.run()
