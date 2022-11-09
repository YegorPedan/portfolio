from os import environ


class Config:
    SECRET_KET = environ.get("SECRET_KEY") or "you-will-never-guess"