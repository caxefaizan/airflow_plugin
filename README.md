# airflow_plugin
How to add a Plugin on the Airflow UI

Run the following commands
```
minikube start

docker build -t airflow-local:1.0.0 .

minikube image load airflow-local:1.0.0

helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace -f values.yaml --debug

kubectl port-forward svc/airflow-webserver 8080:8080 --namespace airflow
```
