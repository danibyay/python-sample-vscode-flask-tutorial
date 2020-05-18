# Python/Flask tutorial sample for Visual Studio Code

* This sample contains the completed program from the tutorial, make sure to visit the link: [Using Flask in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask). Intermediate steps are not included.
* It also contains the Dockerfile and uwsgi.ini files necessary to build a container with a production server. The resulting image works both locally and when deployed to Azure App Service. See [Deploy Python using Docker containers](https://code.visualstudio.com/docs/python/tutorial-deploy-containers).

## Navigation

The `startup.py` file, for its part, is specifically for deploying to Azure App Service on Linux without containers. Because the app code is in its own *module* in the `hello_app` folder (which has an `__init__.py`), trying to start the Gunicorn server within App Service on Linux produces an "Attempted relative import in non-package" error. The `startup.py` file, therefore, is just a shim to import the app object from the `hello_app` module, which then allows you to use startup:app in the Gunicorn command line (see `startup.txt`).

## Contributing

Contributions to the sample are welcome. When submitting changes, also consider submitting matching changes to the tutorial, the source file for which is [tutorial-flask.md](https://github.com/Microsoft/vscode-docs/blob/master/docs/python/tutorial-flask.md).

Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot automatically determines whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

## Additional details

* This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
* For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
* Contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.


## Added dependencies

> pip install flask-wtf

> pip install flask-sqlalchemy

> pip install flask-migrate

## To run the development server

> export FLASK_APP=startup.py

> flask run

## To use Flask-Migrate

Only the first time. 
> flask db init

Generate migration script.
the -m message is optional.
> flask db migrate -m "users table"

Apply changes in the database
> flask db upgrade

After updating the database uri, runupgrade again, so the database will be created in the remote server.

## Start the python interpreter with all the flask dependencies of your app installed

> flask shell


## Troubleshooting with Database URI

Right now the URI is hardcoded. Follow this advice to fix the string format in the migrations/env.py file.
(Flask issue, SQLAlchemy works)
[Link 1](https://stackoverflow.com/questions/61710596/cant-apply-flask-db-migrate-when-using-pyodbc-w-sql-server-error-neither-dsn)

[Link 2](https://stackoverflow.com/questions/46739295/connect-to-mssql-database-using-flask-sqlalchemy)

[Link 3](https://github.com/miguelgrinberg/Flask-Migrate/issues/328#issuecomment-629870874)

Test command on independent script:

> print(engine_azure.table_names())

output: 

> 2020-05-18 01:42:24,631 INFO sqlalchemy.engine.base.Engine ('dbo', 'BASE TABLE')
['alembic_version', 'post', 'user']

## NExt step May 17

* Commit changes to master and verify with pipeline deployment (merge branch & push to origin)

* but before, upgrade requirements.txt, even if the database is not visibly working in the app, the imports would break.