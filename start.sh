!#/bin/bash

# Start minikube
#minikube start

# Set docker env
#eval $(minikube docker-env)

# Build image
docker build -t <user_dockerhub_username>/python:latest .

# loging to push image to docker hub 
docker login -u <user_dockerhub_username>  - p <user_dockerhub_password> 

# push docker image
docker push <user_dockerhub_username>/python:lagtest


#Kubectl shoud be configured run bellow command.

# create deployment for kubernates cluster  
kubectl create deployment your-app --image=<user_dockerhub_username> /python:latest .

# expose dpeloyment as a service to access from out side the cluster
kubectl expose deployment your-app --type=LoadBalancer --port=80 --target-port 5000

# view running pods inside kubernates cluster
kubectl get pods

# view Deployments in kubernates cluster
kubectl get deployments

# view exposed services and here you will be able to get public IP addrees to access service 
kubectl get svc

