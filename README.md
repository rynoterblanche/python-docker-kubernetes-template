# Template for Python apps on Docker & Kubernetes

This template includes:

- a nginx server as frontend
- a small web service written in Flask
- a MySQL db backend
- basic starter configurations for both Docker & Kubernetes deployment

The application follows a Clean Architecture design.

## Docker & Kubernetes

### Docker Compose

1. Set environment variables & substitute your docker account as necessary:

   ```
   export APP_ENV=development or export APP_ENV=production
   export DOCKER_ACCT=vatie
   ```

   (for standard Windows command shell use `set` instead of `export`)

   or in Windows Powershell use:
   ```
   $env:APP_ENV = "development"
   $env:DOCKER_ACCT = "vatie"
   ```

2. Run `docker-compose build`
3. Run `docker-compose up`

## Kubernetes - Usage

1. Run the following to add the database passwords as secrets:

   `kubectl create secret generic db-passwords --from-literal=db-password='password' --from-literal=db-root-password='password'`

   Note: These are simple passwords used for demo purposes only. Use strong passwords for real setup!

2. Start everything:

   `kubectl create -f .k8s`

3. Delete everything:

   `kubectl delete -f .k8s`

## Local Development

1. You can run the [Flask web service](./src/product_service) locally. The local [configuration](./config.yml) uses an
   in-memory db.

   ```shell
   # Using Powershell
   poetry install
   poetry run python .\src\product_service\app.py --config config.yml
   ```

2. You can also run & debug the service directly in PyCharm or VSCode from [app.py](./src/product_service/app.py)
