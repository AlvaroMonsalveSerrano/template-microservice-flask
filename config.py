import os


def get_api_url():
    """
    Create url.

    :return: Str, http://{host}:{port}
    """
    host = os.environ.get('API_HOST', 'localhost')
    port = 5000 if host == 'localhost' else 80
    return f"http://{host}:{port}"
