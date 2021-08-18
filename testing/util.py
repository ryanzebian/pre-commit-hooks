import os.path


TESTING_DIR = os.path.abspath(os.path.dirname(__file__))


def get_resource_path(path: str) -> str:
    return os.path.join(TESTING_DIR, 'resources', path)
