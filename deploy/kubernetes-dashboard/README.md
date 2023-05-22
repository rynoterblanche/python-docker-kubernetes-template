# Kubernetes Dashboard

## Installation

* https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/
* https://github.com/kubernetes/dashboard/blob/master/docs/user/access-control/creating-sample-user.md
* https://github.com/kubernetes/dashboard

Steps:

1. Install Dashboard:

   `kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml`

2. Run `kubectl apply -f dashboard.adminuser.yml`
3. Get a token (see [creating sample user][create_sample_user]) by running the following. Copy the token into your
   clipboard.

   `kubectl -n kubernetes-dashboard create token admin-user`

4. Run `kubectl proxy`.
5. Visit http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
6. Paste the token into the login screen and sign in to the dashboard.

[create_sample_user]: https://github.com/kubernetes/dashboard/blob/master/docs/user/access-control/creating-sample-user.md