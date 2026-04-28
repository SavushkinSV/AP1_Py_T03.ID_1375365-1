from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    # register_routes(app)

    @app.route("/")
    def index():
        return "Tic-Tac-Toe API is working!"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
