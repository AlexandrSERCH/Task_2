# Stellar Burgers — API Test Automation

Автотесты для REST API сервиса [Stellar Burgers](https://stellarburgers.education-services.ru).

**Стек:** Python · pytest · requests · allure-pytest · pydantic · faker · pytest-xdist

---

## Структура проекта

```
Task_2/
├── clients/                    # HTTP-клиенты (обёртки над requests)
│   ├── base_client.py          # Базовый клиент: сессия, логирование в Allure
│   ├── user_client.py          # Методы для /api/auth/...
│   └── order_client.py         # Методы для /api/orders
├── data/
│   ├── users_data/
│   │   ├── builder_users.py    # Builder для тестовых пользователей (Faker)
│   │   └── constans_users.py   # Константы пользователей
│   └── orders_data/
│       └── constants_orders.py # Тестовые наборы заказов
├── helpers/
│   ├── build_curl.py           # Генератор cURL-команды для Allure
│   └── validate_html_in_response_body.py
├── models/
│   ├── responses/              # Pydantic-модели тел ответов
│   └── users/                  # Pydantic-модель пользователя
├── tests/
│   ├── users/
│   │   ├── test_create_user.py
│   │   ├── test_login_user.py
│   │   └── test_update_user.py
│   └── orders/
│       ├── test_create_order.py
│       └── test_get_order.py
├── config.py                   # BASE_URL
├── conftest.py                 # Фикстуры (клиенты, создание/удаление пользователей)
├── pytest.ini                  # Настройки pytest (-n auto по умолчанию)
└── requirements.txt
```

---

## Требования

- Python 3.10+

---

## Установка

```bash
# 1. Клонировать репозиторий
git clone <url-репозитория>
cd Task_2

# 2. Создать виртуальное окружение
python -m venv .venv

# 3. Активировать
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

# 4. Установить зависимости
pip install -r requirements.txt
```

---

## Запуск тестов

### Все тесты (параллельно, без Allure)

По умолчанию `pytest.ini` содержит `addopts = -n auto` — тесты запускаются в параллельных воркерах автоматически.

```bash
pytest
```

### Все тесты с формированием Allure-отчёта

```bash
pytest --alluredir=allure-result
```

### Конкретный модуль или директория

```bash
# Только тесты пользователей
pytest tests/users/

# Только тесты заказов
pytest tests/orders/

# Один файл
pytest tests/users/test_create_user.py
```

### Запуск с указанием числа потоков вручную

```bash
# 4 потока
pytest -n 4 --alluredir=allure-result

# Без параллелизма (отладка)
pytest -n 0 --alluredir=allure-result
```

---

## Просмотр Allure-отчёта


```bash
allure serve allure-result
```


---

## Пример отчёта

![Allure Report](allure-result/img.png)

В отчёте для каждого теста доступны:

| Вкладка              | Содержимое                              |
|----------------------|-----------------------------------------|
| `url`                | Полный URL запроса                      |
| `cURL` | Готовая команда для воспроизведения запроса |
| `request_headers` | Заголовки запроса (JSON) |
| `request_body` | Тело запроса (JSON) |
| `response_status_code` | HTTP-код ответа |
| `response_headers` | Заголовки ответа (JSON) |
| `response_body` | Тело ответа (JSON) |
| `response_time_in_sec` | Время выполнения запроса |

---

## Покрытие тестами

| Группа                    | Тест-кейс                                          |
|---------------------------|----------------------------------------------------|
| Создание пользователя     | Успешное создание                                  |
| | Дубликат пользователя → 403 |
| | Отсутствие email / password / name → 403 |
| Авторизация пользователя | Успешный логин |
| | Неверный email → 401 |
| | Неверный пароль → 401 |
| | Неверные email и пароль → 401 |
| Обновление пользователя | Успешное обновление авторизованным пользователем |
| | Обновление без авторизации → 401 |
| Создание заказа | Успешное создание (авторизован / не авторизован) |
| | Заказ без ингредиентов → 400 |
| | Заказ с невалидным ингредиентом → 500 |
| Получение заказов | Получение заказов авторизованным пользователем |
| | Получение заказов без авторизации → 401 |

---

## Конфигурация

`config.py` — единственная точка для изменения окружения:

```python
BASE_URL = "https://stellarburgers.education-services.ru"
```

Для смены стенда достаточно заменить значение `BASE_URL`.