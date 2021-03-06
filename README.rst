May need `poetry add tzlocal==2.1` for O365
project1.ac1@outlook.com
JKndfu203Pfslkm23-k2(.Fun
```bash
###
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -v /home/queprocno/Desktop/post_data:/var/lib/postgresql/data -p 5432:5432 -d postgres
```

cd ~/Desktop/project1_be && rsync -avIL -e "ssh -i ~/.ssh/qacer" --exclude-from=".gitignore" ./* qacer@192.168.1.23:Desktop/project1_be/

```bash
sudo apt install python3.8-venv
sudo apt install python3-pip
python3 -m venv venv
. venv/bin/activate
# deactivate

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
# source $HOME/.poetry/env
# pg_config is required to build psycopg2 from source
sudo apt install libpq-dev python3-dev
```

```bash
cd /home/queprocno/Desktop/ts-redux-react-realworld-example-app
npm install
npm start # Open http://localhost:3000 to view it in the browser.
npm test	# Launches the test runner in the interactive watch mode.
npm run build		#Builds the app for production to the build folder.

```

```bash
# how to add venv to vscode
# Ctr+Shift+P, select interpreter
# /home/queprocno/.cache/pypoetry/virtualenvs/fastapi-realworld-example-app-XXmL_YhF-py3.8
# how to know where is this venv located:
poetry config --list
```





## FastAPI BE
```bash
#postgres driver
sudo apt install postgresql-client-12 python3-distutils alembic
# poetry
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

export POSTGRES_DB=rwdb POSTGRES_PORT=5432 POSTGRES_USER=postgres POSTGRES_PASSWORD=postgres
docker run --name pgdb -v ~/Desktop/post_data:/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_USER="$POSTGRES_USER" -e POSTGRES_PASSWORD="$POSTGRES_PASSWORD" -e POSTGRES_DB="$POSTGRES_DB" -d postgres
export POSTGRES_HOST=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' pgdb)
createdb --host=$POSTGRES_HOST --port=$POSTGRES_PORT --username=$POSTGRES_USER $POSTGRES_DB

git clone https://github.com/nsidnev/fastapi-realworld-example-app
cd fastapi-realworld-example-app
poetry install
poetry shell

touch .env
echo DB_CONNECTION=postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB >> .env
echo SECRET_KEY=$(openssl rand -hex 32) >> .env

alembic upgrade head
uvicorn app.main:app --reload --host 0.0.0.0
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc
# http://127.0.0.1:8000/openapi.json
```


convert data dict to text:
https://github.com/ilius/pyglossary
convert dict.org file format (.index file, together with .dz and .ini files) to text.










.. image:: ./.github/assets/logo.png

|

.. image:: https://github.com/nsidnev/fastapi-realworld-example-app/workflows/API%20spec/badge.svg
   :target: https://github.com/nsidnev/fastapi-realworld-example-app

.. image:: https://github.com/nsidnev/fastapi-realworld-example-app/workflows/Tests/badge.svg
   :target: https://github.com/nsidnev/fastapi-realworld-example-app

.. image:: https://github.com/nsidnev/fastapi-realworld-example-app/workflows/Styles/badge.svg
   :target: https://github.com/nsidnev/fastapi-realworld-example-app

.. image:: https://github.com/nsidnev/fastapi-realworld-example-app/workflows/Deploy/badge.svg
   :target: https://frw.nsidnev.dev/

.. image:: https://codecov.io/gh/nsidnev/fastapi-realworld-example-app/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/nsidnev/fastapi-realworld-example-app

.. image:: https://img.shields.io/github/license/Naereen/StrapDown.js.svg
   :target: https://github.com/nsidnev/fastapi-realworld-example-app/blob/master/LICENSE

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black

.. image:: https://img.shields.io/badge/style-wemake-000000.svg
   :target: https://github.com/wemake-services/wemake-python-styleguide

Quickstart
----------

First, run ``PostgreSQL``, set environment variables and create database. For example using ``docker``: ::

    export POSTGRES_DB=rwdb POSTGRES_PORT=5432 POSTGRES_USER=postgres POSTGRES_PASSWORD=postgres
    docker run --name pgdb --rm -e POSTGRES_USER="$POSTGRES_USER" -e POSTGRES_PASSWORD="$POSTGRES_PASSWORD" -e POSTGRES_DB="$POSTGRES_DB" postgres
    export POSTGRES_HOST=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' pgdb)
    createdb --host=$POSTGRES_HOST --port=$POSTGRES_PORT --username=$POSTGRES_USER $POSTGRES_DB

Then run the following commands to bootstrap your environment with ``poetry``: ::

    git clone https://github.com/nsidnev/fastapi-realworld-example-app
    cd fastapi-realworld-example-app
    poetry install
    poetry shell

Then create ``.env`` file (or rename and modify ``.env.example``) in project root and set environment variables for application: ::

    touch .env
    echo DB_CONNECTION=postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB >> .env
    echo SECRET_KEY=$(openssl rand -hex 32) >> .env

To run the web application in debug use::

    alembic upgrade head
    uvicorn app.main:app --reload

If you run into the following error in your docker container:

   sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not connect to server: No such file or directory
   Is the server running locally and accepting
   connections on Unix domain socket "/tmp/.s.PGSQL.5432"?

Ensure the DB_CONNECTION variable is set correctly in the `.env` file. 
It is most likely caused by POSTGRES_HOST not pointing to its localhost.

   DB_CONNECTION=postgresql://postgres:postgres@0.0.0.0:5432/rwdb



Run tests
---------

Tests for this project are defined in the ``tests/`` folder. 

This project uses `pytest
<https://docs.pytest.org/>`_ to define tests because it allows you to use the ``assert`` keyword with good formatting for failed assertations.


To run all the tests of a project, simply run the ``pytest`` command: ::

    $ pytest
    ================================================= test session starts ==================================================
    platform linux -- Python 3.8.3, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
    rootdir: /home/some-user/user-projects/fastapi-realworld-example-app, inifile: setup.cfg, testpaths: tests
    plugins: env-0.6.2, cov-2.9.0, asyncio-0.12.0
    collected 90 items

    tests/test_api/test_errors/test_422_error.py .                                                                   [  1%]
    tests/test_api/test_errors/test_error.py .                                                                       [  2%]
    tests/test_api/test_routes/test_articles.py .................................                                    [ 38%]
    tests/test_api/test_routes/test_authentication.py ..                                                             [ 41%]
    tests/test_api/test_routes/test_comments.py ....                                                                 [ 45%]
    tests/test_api/test_routes/test_login.py ...                                                                     [ 48%]
    tests/test_api/test_routes/test_profiles.py ............                                                         [ 62%]
    tests/test_api/test_routes/test_registration.py ...                                                              [ 65%]
    tests/test_api/test_routes/test_tags.py ..                                                                       [ 67%]
    tests/test_api/test_routes/test_users.py ....................                                                    [ 90%]
    tests/test_db/test_queries/test_tables.py ...                                                                    [ 93%]
    tests/test_schemas/test_rw_model.py .                                                                            [ 94%]
    tests/test_services/test_jwt.py .....                                                                            [100%]

    ============================================ 90 passed in 70.50s (0:01:10) =============================================
    $

This project does not use your local ``PostgreSQL`` by default, but creates it in ``docker`` as a container (you can see it if you type ``docker ps`` when the tests are executed, the docker container for ``PostgreSQL`` should be launched with with a name like ``test-postgres-725b4bd4-04f5-4c59-9870-af747d3b182f``). But there are cases when you don't want to use ``docker`` for tests as a database provider (which takes an additional +- 5-10 seconds for its bootstrap before executing the tests), for example, in CI, or if you have problems with the ``docker`` driver or for any other reason. In this case, you can run the tests using your already running database with the following command: ::

   $ USE_LOCAL_DB_FOR_TEST=True pytest

Which will use your local database with DSN from the environment variable ``DB_CONNECTION``.


If you want to run a specific test, you can do this with `this
<https://docs.pytest.org/en/latest/usage.html#specifying-tests-selecting-tests>`_ pytest feature: ::

    $ pytest tests/test_api/test_routes/test_users.py::test_user_can_not_take_already_used_credentials

Deployment with Docker
----------------------

You must have ``docker`` and ``docker-compose`` tools installed to work with material in this section.
First, create ``.env`` file like in `Quickstart` section or modify ``.env.example``.
``POSTGRES_HOST`` must be specified as `db` or modified in ``docker-compose.yml`` also.
Then just run::

    docker-compose up -d db
    docker-compose up -d app

Application will be available on ``localhost`` in your browser.

Web routes
----------

All routes are available on ``/docs`` or ``/redoc`` paths with Swagger or ReDoc.


Project structure
-----------------

Files related to application are in the ``app`` or ``tests`` directories.
Application parts are:

::

    app
    ????????? api              - web related stuff.
    ??????? ????????? dependencies - dependencies for routes definition.
    ??????? ????????? errors       - definition of error handlers.
    ??????? ????????? routes       - web routes.
    ????????? core             - application configuration, startup events, logging.
    ????????? db               - db related stuff.
    ??????? ????????? migrations   - manually written alembic migrations.
    ??????? ????????? repositories - all crud stuff.
    ????????? models           - pydantic models for this application.
    ??????? ????????? domain       - main models that are used almost everywhere.
    ??????? ????????? schemas      - schemas for using in web routes.
    ????????? resources        - strings that are used in web responses.
    ????????? services         - logic that is not just crud related.
    ????????? main.py          - FastAPI application creation and configuration.
