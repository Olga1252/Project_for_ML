"Разработка и внедрение сервиса прогнозирования дефолта по кредитным картам с контейнеризацией и A/B-тестированием "

Датасет: Default of Credit Card Clients Dataset с UCI Machine Learning Repository.

Целевая переменная default.payment.next.month и принимает два значниея:
0 — дефолта нет
1 — дефолт есть

Содержание: 
1. Обучение модели бинарной классификации 
2. загрузка модели joblib
3. Flask API
4. эндпоинты /health /predict
5. контейнеризация 
6. документация 
7. A/B тестирование 

В проекте было использллвано две модели Логистической регресии (Logistic regression - model_v1) и случайный лес (Random forest classifier model_v2). После обучения модели сохраняются в папку models/. Во время обучения выводятся метрики качества. 

Установка зависимостей. 

виртуальное окружение:

python -m venv venv

виртуальное окружение на Windows:

venv\Scripts\activate

Установка зависимостей:

pip install -r requirements.txt

Flask API

Запустить API локально можно командой:

python -m app.api

После запуска сервис будет доступен по адресу:

http://127.0.0.1:5000

Пример запроса:

curl -X POST "http://127.0.0.1:5000/predict?v=v1" \
-H "Content-Type: application/json" \
-d '{
  "LIMIT_BAL": 20000,
  "SEX": 2,
  "EDUCATION": 2,
  "MARRIAGE": 1,
  "AGE": 24,
  "PAY_0": 2,
  "PAY_2": 2,
  "PAY_3": -1,
  "PAY_4": -1,
  "PAY_5": -2,
  "PAY_6": -2,
  "BILL_AMT1": 3913,
  "BILL_AMT2": 3102,
  "BILL_AMT3": 689,
  "BILL_AMT4": 0,
  "BILL_AMT5": 0,
  "BILL_AMT6": 0,
  "PAY_AMT1": 0,
  "PAY_AMT2": 689,
  "PAY_AMT3": 0,
  "PAY_AMT4": 0,
  "PAY_AMT5": 0,
  "PAY_AMT6": 0
}'

Пример ответа:

{
  "default_probability": 0.7754,
  "model_version": "v1",
  "prediction": 1
}


Эндпоинт:

POST /predict

API поддерживает две версии модели:

/predict?v=v1
/predict?v=v2

Описание полей ответа:

prediction = 0 — модель прогнозирует отсутствие дефолта
prediction = 1 — модель прогнозирует дефолт
default_probability — вероятность дефолта
model_version — версия используемой модели

Docker

Собрать Docker-образ:

docker build -t project_for_ml -f docker/Dockerfile .

Запустить контейнер:

docker run -p 5000:5000 project_for_ml

После запуска контейнера API будет доступен по адресу:

http://127.0.0.1:5000

Проверить работоспособность сервиса:

curl http://127.0.0.1:5000/health

Docker Hub

Docker-образ загружен в Docker Hub.

Ссылка на Docker Hub:




























