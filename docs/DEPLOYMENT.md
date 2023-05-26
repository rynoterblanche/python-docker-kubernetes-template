# Deployment

## Docker Compose - Usage

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

## Kubernetes

1. Run the following to add the database passwords as secrets:

   `kubectl create secret generic db-passwords --from-literal=db-password='password' --from-literal=db-root-password='password'`

   Note: These are simple passwords used for demo purposes only. Use strong passwords for real setup!

2. Start everything:

   `kubectl create -f .k8s`

3. Delete everything:

   `kubectl delete -f .k8s`
