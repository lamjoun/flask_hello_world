# flask_hello_world
For tests by a simple flask app to show Hello World 

# URLs
- https://cloud.google.com/kubernetes-engine/docs/quickstarts/deploy-app-container-image#python_1
- https://github.com/GoogleCloudPlatform/cloud-run-microservice-template-python
- dfsdf
- sdfsd

# Commands
```
# create Project
export PROJECT_ID='rl-project-test1'
gcloud projects create $PROJECT_ID --name 'rl-project-test1-name' --set-as-default
gcloud projects list
gcloud config get-value project

# Billing in order to create Artifactes Docker Repo
# to activate go to console and search --> Billing projects
# to check ?
gcloud beta billing projects describe $PROJECT_ID

# Create artifacts repo hello-repo
export ZONE='us-central1'
export DOCKER_REPO='hello-repo'
export DOCKER_PACKAGE='Hello-world-pkg1'
gcloud artifacts repositories create $DOCKER_REPO \
    --project=$PROJECT_ID \
    --repository-format=docker \
    --location=$ZONE \
    --description="Artifacts Docker repository"

# Check repo creation
gcloud artifacts repositories list

# Docker: Build & Push Package Hello-world-pkg1
gcloud builds submit --tag $ZONE-docker.pkg.dev/$PROJECT_ID/$DOCKER_REPO/$DOCKER_PACKAGE

```


