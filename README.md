# PyConAfrica 2020 - Building production-worthy websites with Django

[![Build Status](https://travis-ci.com/Emmarex/PyconAfrica2020.svg?token=UrwRzHuApu2JJndPbucm&branch=master)](https://travis-ci.com/Emmarex/PyconAfrica2020)

## Getting started

1. Clone this application - ```git clone https://github.com/Emmarex/PyconAfrica2020.git```

2. Install and configure virtualenv

```bash
pip install --upgrade pip

pip install virtualenv

virtualenv env

# or specify python path

virtualenv --python=/usr/local/bin/python3 env

# activate the virtual environment

source env/bin/activate
```

3. Install project dependencies.
```bash
# switch to project directory

cd PyconAfrica2020

pip install -r requirements.txt
```

4. Edit init_env.sh

5. Set required environment variables
```bash

chmod +x init_env.sh

sh init_env.sh

```
6. [OPTIONAL- Compulsory for production settings only] Follow the steps [here](https://django-storages.readthedocs.io/en/latest/backends/gcloud.html#authentication) to configure Google Cloud Storage.

7. Make migrations and start the application
```bash

python manage.py makemigrations && python manage.py migrate

python manage.py runserver

```