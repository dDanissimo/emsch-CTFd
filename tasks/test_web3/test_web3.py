import pytest
import sqlite3
import os
from app import app as flask_app, create_database, DATABASE

@pytest.fixture
def app():
    """
    Передача в pytest стартовых данных о приложении
    """
    test_db_path = "test_database.db"
    # создание тестовой БД 
    os.environ["DATABASE"] = "test_database.db"
    create_database()
    yield flask_app
    # сворачивание тестовой БД
    if os.path.exists(test_db_path):
        os.remove(test_db_path)

@pytest.fixture
def client(app):
    """
    Передача в pytest данных о тестовом клиенте приложения
    """
    return app.test_client()

def test_login_page(client):
    """
    Проверка на валидность отображения страницы логина
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Login" in response.data

def test_successful_login(client):
    """
    Проверка успешной авторизации пользователя при корректно введённых запрашиваемых данных
    """
    response = client.post('/login', data={'username': 'admin', 'password': 'admin_password'})
    assert b"Flag" in response.data

def test_failed_login(client):
    """
    Обработка ошибок в механизме авторизации
    """
    response = client.post('/login', data={'username': 'wrong', 'password': 'wrong'})
    assert b"Login failed" in response.data

def test_database_creation():
    """
    Проверка наличия подключения к базе данных sqlite3
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    number_of_users = cursor.fetchone()[0]
    conn.close()
    assert number_of_users >= 2
