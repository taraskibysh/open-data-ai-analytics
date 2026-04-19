# Docker контейнеризація аналітичного проєкту

## Опис проєкту

Контейнеризована аналітична система для обробки вихідної кореспонденції Держкомтелерадіо за грудень 2025 року.

Система складається з 6 Docker-контейнерів, які автоматично запускаються, обробляють дані та відображають результати через веб-інтерфейс.

## Структура проєкту

```
project/
├── data/                          # Вхідні дані
│   └── dataset.csv                # CSV-файл з даними
├── data_load/                     # Сервіс завантаження даних
│   ├── app.py                     # Скрипт завантаження CSV у БД
│   ├── Dockerfile
│   └── requirements.txt
├── data_quality_analysis/         # Сервіс перевірки якості
│   ├── data_quality_analysis.ipynb
│   ├── Dockerfile
│   └── requirements.txt
├── data_research/                 # Сервіс дослідження даних
│   ├── data_research.ipynb
│   ├── Dockerfile
│   └── requirements.txt
├── visualization/                 # Сервіс візуалізації
│   ├── visualization.ipynb
│   ├── Dockerfile
│   └── requirements.txt
├── web/                           # Веб-інтерфейс
│   ├── web.ipynb
│   ├── templates/
│   ├── static/
│   ├── Dockerfile
│   └── requirements.txt
├── db/                            # База даних
│   └── init/
├── reports/                       # Згенеровані звіти (JSON)
├── plots/                         # Згенеровані графіки (PNG)
├── .env                           # Змінні середовища
├── compose.yaml                   # Docker Compose конфігурація
└── README.md                      # Цей файл
```

## Сервіси

| Сервіс | Опис | Технологія |
|--------|------|------------|
| **db** | MySQL база даних | MySQL 8.0 |
| **data_load** | Завантаження CSV у БД | Python 3.9 + pandas + SQLAlchemy |
| **data_quality_analysis** | Перевірка якості даних | Jupyter Notebook + nbconvert |
| **data_research** | Статистичний аналіз та кластеризація | Jupyter Notebook + scikit-learn |
| **visualization** | Побудова графіків | Jupyter Notebook + matplotlib + seaborn |
| **web** | Веб-інтерфейс для перегляду результатів | Voilà + ipywidgets |

## Порядок запуску сервісів

```
db (MySQL з healthcheck)
  └── data_load (чекає на service_healthy)
        ├── data_quality_analysis (чекає на service_completed_successfully)
        ├── data_research (чекає на service_completed_successfully)
        └── visualization (чекає на service_completed_successfully)
              └── web (чекає на завершення всіх аналітичних сервісів)
```

## Інструкція для запуску

### 1. Створіть файл `.env`

Файл `.env` вже включено в проєкт із такими налаштуваннями:

```env
MYSQL_ROOT_PASSWORD=rootpassword
MYSQL_DATABASE=docflow
MYSQL_USER=appuser
MYSQL_PASSWORD=apppassword
```

> За потреби змініть паролі на свої.

### 2. Запустіть систему

```bash
docker compose up --build
```

### 3. Відкрийте веб-інтерфейс

Після успішного запуску всіх сервісів веб-інтерфейс доступний за адресою:

🌐 **http://localhost:8866**

### 4. Зупинити систему

```bash
docker compose down
```

Для видалення даних БД:

```bash
docker compose down -v
```

## Мережа та томи

- **Мережа:** `data_network` (bridge) — всі контейнери бачать один одного за іменами
- **Томи:**
  - `db_data` — збереження даних MySQL
  - `./reports:/shared/reports` — обмін JSON-звітами
  - `./plots:/shared/plots` — обмін PNG-графіками
  - `./data:/data` — вхідні CSV-дані

## Порти

| Порт | Сервіс | Опис |
|------|--------|------|
| 8866 | web | Веб-інтерфейс Voilà |

## Датасет

**Назва:** Вихідні документи за грудень 2025 року
**Джерело:** [data.gov.ua](https://data.gov.ua/dataset/ffc99c1e-ac64-4b8f-ad97-858060cdb012/resource/dbfcbad0-3fc9-41b2-a5ad-5c7f25dbacda)