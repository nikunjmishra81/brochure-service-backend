import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    BASE_URL=(str, ""),
)

# reading .env file
environ.Env.read_env()

ENV = env("ENV")
DEBUG = env.bool("DEBUG", False)
PORT = env.int("PORT")
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS")
BACKEND_HOST = env.str("BACKEND_HOST")
DUMMY_RESPONSE_FILE_PATH = env.path("DUMMY_RESPONSE_FILE_PATH")
DUMMY_RESPONSE_FILE_NAME = env.str("DUMMY_RESPONSE_FILE_NAME")
