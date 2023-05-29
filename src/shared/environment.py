import os


class Env:

    @staticmethod
    def get(key: str) -> str:
        return os.environ[key]
