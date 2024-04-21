FROM python:3.11.8-alpine3.19

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip

COPY ./Requirements.txt ./

RUN pip install -r Requirements.txt

COPY ./ ./

COPY wait-for-it.sh ./

# CMD ["wait-for-it.sh", "db:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
