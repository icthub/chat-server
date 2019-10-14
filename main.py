import app


if __name__ == "__main__":
    app.util.log_info("Application launched")
    instance = app.Endpoint()
    instance.start()
