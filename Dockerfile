# Используем образ Python
FROM python:3.10.5-slim-buster

# Устанавливаем переменную окружения PYTHONUNBUFFERED для вывода в логи без буферизации
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app/

# Установка зависимостей
RUN pip install -r requirements.txt


# Запуск Gunicorn
# CMD ["gunicorn", "config.wsgi:application", "-b", "0.0.0.0:8000"]
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "4", "--access-logfile", "-"]
