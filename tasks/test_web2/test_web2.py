import pytest
from app import app as flask_app

@pytest.fixture
def app():
    """
    Предоставление начальных данных о настройках веб-приложения.
    """
    yield flask_app

@pytest.fixture
def client(app):
    """
    Предоставление начальных данных о тестовом клиенте веб-приложения.
    """
    return app.test_client()

def test_home_page(client):
    """
    Проверка на доступность домашней страницы.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Vulnerable App" in response.data

def test_ping_route_valid_ip(client):
    """
    Проверка на валидность ответа при введённом корректном IP
    """

    # TODO: проверять ip по regex

    response = client.get('/ping?ip=127.0.0.1')
    assert response.status_code == 200
    assert b"PING 127.0.0.1 (127.0.0.1)" in response.data

def test_ping_route_invalid_ip(client):
    """
    Проверка штатной отработки программы при неправильном введённом айпи; статус - 200 OK; вывод - отсутствует
    """
    response = client.get('/ping?ip=invalid_ip')
    assert response.status_code == 200
    assert b"" in response.data

def test_404_error_handler(client):
    """
    Проверка ображщения к несуществующему ресурсу
    """
    response = client.get('/nonexistentpage')
    assert response.status_code == 404
    assert b"404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again." in response.data
