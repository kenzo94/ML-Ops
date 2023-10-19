# End to end ML Project

## Workflow

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update main.py
9. Update dvc.yaml

# How to run?
### STEPS:

Clone the repository

```bash
https://https://github.com/kenzo94/ML-Ops
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```

## MLflow
[Documentation](https://mlflow.org/docs/latest/index.html)

#### cmd
- mlflow ui


#### dagshub
[dagshub](https://dagshub.com)
MLFLOW_TRACKING_URI=https://dagshub.com/kenzo94/ML-Ops.mlflow \
MLFLOW_TRACKING_USERNAME=kenzo94 \
MLFLOW_TRACKING_PASSWORD=8753b04ed498c50f40388010fee24743d51213c5 \
python script.py

Run this to export as env variables
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/kenzo94/ML-Ops.mlflow 

export MLFLOW_TRACKING_USERNAME=kenzo94

export MLFLOW_TRACKING_PASSWORD=8753b04ed498c50f40388010fee24743d51213c5
```


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 153234415674.dkr.ecr.eu-central-1.amazonaws.com/mlops

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optional

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app


# Azure Deployment

1. Create Container Registry

# Afterwards Run from YOUR terminal

2. Build Container: docker build -t your_docker_registry_name/your_project_name:latest .

3. Login into registry: docker login your_docker_registry_name

4. Push to Registry: docker push your_docker_registry_name/your_project_name:latest

5. Create Azure Web App and take pushes container

## In Deployment center of the Web App

6. Set Source to GitHub actions

7. Set CD On

## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model
