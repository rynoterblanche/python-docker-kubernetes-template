#### Using a StorageClass, PersistentVolume, PersistentVolueClaim, and ConfigMap

## Running the MySQL Deployment

Example deployment config using StorageClass, PersistentVolume & PersistentValueClaim

1. Create the following folder structure on your local system:

   **Windows:**   `c:/temp/data/db`

   **Linux:** `/tmp/data/db`

2. Edit the `mysql.deployment.yml` and change the PVs local `path` to one of the following:

   **Windows:**  `/c/temp/data/db`. If you're using WSL with Docker desktop try using `/mnt/c/temp/data/db`
   or `/run/desktop/mnt/host/c/temp/data/db` (depending on your WSL version and setup)

   **Linux:** `/tmp/data/db`

3. Start up the Pod:

   `kubectl create -f mysql.deployment.yml`

4. Run `kubectl get pods` to see the pod.
5. Run `kubectl exec [msql-pod-name] -it sh` to shell into the container. Run the `msql` command to make sure the
   database is working. Type `exit` to exit the shell.

   Note: If you have a tool that can hit MySQL externally you can `kubectl port-forward` to the pod to expose 3306.

6. Delete the mongo Pod: `kubectl delete pod [msql-pod-name]`
7. Once the pod is deleted, run `kubectl get pv` and note the reclaim policy that's shown and the status (should show
   Bound since the policy was Retain)
8. Delete everything else: `kubectl delete -f mysql.deployment.yml`