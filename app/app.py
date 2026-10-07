from flask import Flask, jsonify, request
import logging
import os
from datetime import datetime, timezone

app = Flask(__name__)

APP_NAME = "infrastructure-automation"
APP_VERSION = "1.1.0"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


@app.get('/')
def index():
    return jsonify({
        "service": APP_NAME,
        "version": APP_VERSION,
        "status": "running",
        "message": "Infrastructure automation platform is operational",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })


@app.get('/healthz')
def healthz():
    return jsonify({
        "status": "ok",
        "service": APP_NAME,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }), 200


@app.get('/readyz')
def readyz():
    return jsonify({
        "status": "ready",
        "service": APP_NAME,
        "version": APP_VERSION,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }), 200


@app.get('/api/status')
def status():
    return jsonify({
        "service": APP_NAME,
        "version": APP_VERSION,
        "status": "healthy",
        "environment": os.getenv("FLASK_ENV", "development"),
        "features": [
            "terraform",
            "ansible",
            "docker",
            "kubernetes",
            "ci_cd"
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }), 200


@app.get('/api/metrics')
def metrics():
    return jsonify({
        "service": APP_NAME,
        "requests_total": 0,
        "uptime_seconds": 0,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }), 200


@app.errorhandler(404)
def not_found(error):
    logger.warning("Missing route requested: %s", request.path)
    return jsonify({
        "error": "not_found",
        "path": request.path,
        "message": "This endpoint does not exist",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }), 404


@app.errorhandler(500)
def server_error(error):
    logger.exception("Unhandled server error")
    return jsonify({
        "error": "internal_server_error",
        "message": "An unexpected error occurred",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }), 500


if __name__ == '__main__':
    logger.info("Starting %s %s", APP_NAME, APP_VERSION)
    app.run(host="0.0.0.0", port=8000, debug=False)
