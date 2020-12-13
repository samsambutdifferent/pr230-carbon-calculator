# co2 calculator

## setup

```bash
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
```

### windows ver
py -m venv env
Set-ExecutionPolicy Unrestricted -Scope Process
.\env\Scripts\activate
py -m pip install -r requirements.txt


### run

```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run --port=1081

### windows ver
    set FLASK_APP=app.py
    set FLASK_ENV=development
    flask run --port=1081

```

## deployment

### manual

gcloud builds submit --tag gcr.io/project2030/carbon-calculator

gcloud run deploy --image gcr.io/project2030/carbon-calculator --platform managed --region europe-west1 --allow-unauthenticated