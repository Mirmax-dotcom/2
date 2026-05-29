# Информационная система «Управление безналичным питанием и предзаказами»

## Описание
ИС для автоматизации процессов питания в столовой колледжа, включая безналичный расчет, учет лицевых счетов, предзаказ комплексных обедов и формирование аналитической отчетности.

## Структура проекта

```
├── backend/                 # Django REST API
├── frontend/               # React приложение
├── database/               # Миграции и схема БД
├── docs/                   # Документация
├── docker-compose.yml      # Docker конфигурация
├── .env.example            # Пример переменных окружения
└���─ README.md
```

## Технологический стек

- **Backend:** Python 3.10+, Django REST Framework
- **Frontend:** React, Redux Toolkit
- **База данных:** PostgreSQL 14+
- **Веб-сервер:** Nginx
- **Контейнеризация:** Docker, Docker Compose

## Быстрый старт

### Требования
- Docker и Docker Compose
- Git

### Установка

```bash
# Клонировать репозиторий
git clone https://github.com/Mirmax-dotcom/2.git
cd 2

# Скопировать пример переменных окружения
cp .env.example .env

# Поднять контейнеры
docker-compose up -d

# Применить миграции БД
docker-compose exec backend python manage.py migrate

# Создать суперпользователя
docker-compose exec backend python manage.py createsuperuser
```

### Доступ
- Frontend: http://localhost:3000
- Backend Admin: http://localhost:8000/admin
- API: http://localhost:8000/api

## Функциональность

- ✅ Управление лицевыми счетами
- ✅ Проведение транзакций
- ✅ Ведение меню
- ✅ Оформление предзаказов
- ✅ Интеграция с кассой
- ✅ Отчетность
- ✅ Ролевая модель доступа

## Документация

Полная документация находится в папке `/docs`:
- [Архитектура системы](docs/01_architecture.md)
- [Руководство оператора](docs/02_operator_guide.md)
- [Пользовательское руководство](docs/03_user_guide.md)
- [API документация](docs/04_api_documentation.md)
- [План тестирования](docs/05_testing_plan.md)
- [Инструкция по развертыванию](docs/06_deployment.md)

## Лицензия
Внутренняя разработка
