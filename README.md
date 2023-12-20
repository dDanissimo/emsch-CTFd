![image](https://github.com/dDanissimo/emsch-CTFd/assets/56019205/db217886-746f-4da7-8ec9-56c74854ee67)

## Проектная работа по дисциплине "Алгоритмизация и Программирование"
### Название: "Платформа для размещения практических CTF-задач в рамках образовательного курса для школьников по основам ИБ."
### Выполнил: Иванькин Даниил, студент группы БИБ232 ОП "Информационная безопасность".

#### _В основу данного проекта лёг фреймворк CTFd, данный проект является форком исходного продукта. С информацией о фреймворке вы можете ознакомиться ниже:_

* Репозиторий: https://github.com/CTFd/CTFd
* Полный README CTFd: https://github.com/CTFd/CTFd/blob/master/README.md
* Документация (Gitbook): https://docs.ctfd.io/
* [Docs: Getting Started](https://docs.ctfd.io/tutorials/getting-started/)
* [Docs: Deployment options](https://docs.ctfd.io/docs/deployment/installation)

## Задача проекта
Обеспечить школьникам в рамках образовательного курса по информационной безопасности в Экономико-математической школе при ЭФ МГУ (ЭМШ) доступ к платформе, которая способна улучшить образовательный процесс за счёт учёта выполнения домашних/самостоятельных/контрольных работ с дополнительными функциями.
[Ссылка на подтверждающий документ](https://github.com/dDanissimo/emsch-CTFd/files/13722909/2.pdf)


## Функционал

1. Доменное имя с зарегистрированным SSL-сертификатом на этот домен (возможен доступ к ресурсу по HTTPS).

2. Возможность деплоя в публичную Сеть посредством размещения сервиса на выделенном приватном сервере на DIgitalOcean.

3. Фреймворк: Python + Flask + mariaDB/mySQL + redis + jinja2 + werkzeug.

4. Docker для сборки и автоматического деплоя по 80 порту инстанса веб-приложения с возможностью логирования активности на сервисе.

5. Веб-сервер NGINX (обёрнут под Docker) — работает в качестве reverse proxy, перенаправляя весь HTTP-трафик на HTTPS за счёт HTTP-редиректа на порт 443.

6. Система аутентификации и авторизации пользователей (login/register-форма).

7. Почтовый сервер на Mailgun для подтверждения регистрации пользователей с relay-узлом на сервере, где хостится приложение (прописан в конфигах фреймворка).

8. Возможность добавлять на сервис задания, их описание, исходные файлы, количество баллов, подсказки к решению (за штраф к баллам при их использовании).

9. Система уведомлений для всех пользователей.

10. Разграничение пользователей на пользователей и администраторов.

11. Учёт статистики по пользователям и решённым задачкам.

12. Рейтинговая таблица.

13. Возможность отсматривать успешные или неуспешные попытки сдать задание, а также их точное время.

14. Возможность автоматической санитизации HTML-страниц на сервере.

15. Возможность создавать резервные копии содержимого БД и пользовательского контента на сайте.

16. Возможность выбора режима - для соревнований (регистрация по командам) или индивидуального решения (в рамках проекта используется по умолчанию последнее).

17. Размещённые тестовые задания.

## Установка проекта
### Необходимые зависимости: Python 3.0+, Docker (опционально)

> (HTTPS) git clone --depth=1 https://github.com/dDanissimo/emsch-CTFd

> (SSH) git clone --depth=1 git@github.com:dDanissimo/emsch-CTFd.git

### Способ 1: Bare Python
1. Установите необходимые зависимости в Python:
```
python3 -m pip install -r requirements.txt
```
> или

```pip3 install -r requirements.txt```

> (если pip записан в переменной PATH)


2. Если вы запускаете проект нативным образом через Python, обновите https://github.com/ddanissimo/emsch-CTFd/blob/master/CTFd/config.ini под ваши нужды.
```
NB! Значение SECRET_KEY, согласно документации, должно быть пустой строкой.
В случае отсутствия заданного параметра SECRET_KEY, CTFd создаёт файл .ctfd_secret_key,
занесённый в .gitignore, который содержит значение SECRET_KEY. Из документации к фреймворку:

# The secret value used to create sessions and sign strings. This should be set to a random string. In the
# interest of ease, CTFd will automatically create a secret key file for you. If you wish to add this secret key
# to your instance you should hard code this value to a random static value.
```
### Способ 2: Docker
1. Сделать pull пре-собранного образа CTFd с Docker Hub:
```docker run -p 8000:8000 -it ctfd/ctfd```
2. Собрать Docker-image из склонированного репозитория (выполнить в корневой директории проекта):

```docker-compose up``` (для v1 branch docker/compose)

```docker compose up``` (для v2 branch docker/compose)

## Demo

https://emsch.ddanissimo.ru/

## Авторские права:

- Logo by [Laura Barbera](http://www.laurabb.com/)
- Theme by [Christopher Thompson](https://github.com/breadchris)
- Notification Sound by [Terrence Martin](https://soundcloud.com/tj-martin-composer)

## Скриншоты интерфейса
![image](https://github.com/dDanissimo/emsch-CTFd/assets/56019205/5043b06b-269d-49a2-a642-5cc60ce8a84f)
![image](https://github.com/dDanissimo/emsch-CTFd/assets/56019205/57e2849b-e9fe-4e1d-a610-fcf6b4395c3e)
![image](https://github.com/dDanissimo/emsch-CTFd/assets/56019205/21571447-462e-4487-8b4b-dddc8af45d20)
![image](https://github.com/dDanissimo/emsch-CTFd/assets/56019205/7f55f50c-dced-46f6-9d1c-e604cfecd97d)
![image](https://github.com/dDanissimo/emsch-CTFd/assets/56019205/65e76c95-e0b0-432e-9dc4-869ff959f9d7)
![image](https://github.com/dDanissimo/emsch-CTFd/assets/56019205/42e7ffa5-1158-4f4e-af04-f635d08bb2ad)
