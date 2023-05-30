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
export DOCKER_PACKAGE='helloworld-pkg1'
gcloud artifacts repositories create $DOCKER_REPO \
    --project=$PROJECT_ID \
    --repository-format=docker \
    --location=$ZONE \
    --description="Artifacts Docker repository"

# Check repo creation
gcloud artifacts repositories list

# Folder for Docker
mkdir flask-hollo-world
vi app.py
vi Dockerfile
vi .dockerignore

# Docker: Build & Push Package Hello-world-pkg1
gcloud builds submit --tag $ZONE-docker.pkg.dev/$PROJECT_ID/$DOCKER_REPO/$DOCKER_PACKAGE
# for Check
gcloud artifacts packages list --repository=$DOCKER_REPO --location $ZONE

# Deploy service ---> 25 --> northamerica-northeast1
export PORT=8082
# target service
gcloud config set run/region northamerica-northeast1
gcloud run deploy helloworld-srv1 --image $ZONE-docker.pkg.dev/$PROJECT_ID/$DOCKER_REPO/$DOCKER_PACKAGE --allow-unauthenticated

# For check
curl https://helloworld-srv1-zfdiq2g7aa-nn.a.run.app

```
# Create Service Account
```
#================
#*** creation by console ---> IAM a Admin and after "Service Accounts"
# Adding roles: Viewer, Cloud Run Service Agent
#=================
# for check 
export PROJECT_ID='rl-project-test1'
export SERVICE_ACCOUNT_EMAIL=srv-account-github-actions@rl-project-test1.iam.gserviceaccount.com
gcloud iam service-accounts list --project=$PROJECT_ID
# or 
gcloud iam service-accounts list
# with email adress ---> srv-account-github-actions@rl-project-test1.iam.gserviceaccount.com
# export information of Service Account in *** keys.json *** file
# be carreful in creating secrets action ===> GCP_SA_KEY_JSON
gcloud iam service-accounts keys create ./keys.json --iam-account srv-account-github-actions@rl-project-test1.iam.gserviceaccount.com



#**************************
# URL: https://cloud.google.com/iam/docs/service-accounts-create
#-----

export SERVICE_ACCOUNT_EMAIL2=srv2-account-github-actions2@rl-project-test1.iam.gserviceaccount.com
export PROJECT_ID='rl-project-test1'


# Service Account Creation  - be carreful to current project
gcloud iam service-accounts create srv2-account-github-actions2 \
    --description="Description: srv2-account-github-actions2" \
    --display-name="SA2-Github"

# set role to sevice account : srv2-account-github-actions2
# Service Account Adding role ---> roles/run.serviceAgent
gcloud projects add-iam-policy-binding $PROJECT_ID --member=serviceAccount:$SERVICE_ACCOUNT_EMAIL2 --role=roles/run.serviceAgent
 
# Service Account Adding role ---> roles/viewer
gcloud projects add-iam-policy-binding $PROJECT_ID --member=serviceAccount:$SERVICE_ACCOUNT_EMAIL2 --role=roles/viewer

# get roles ??
gcloud iam service-accounts get-iam-policy serviceAccount:$SERVICE_ACCOUNT_EMAIL2 --project $PROJECT_ID

# export keys.json --> information of Service Account
gcloud iam service-accounts keys create ./keys2.json --iam-account $SERVICE_ACCOUNT_EMAIL2




```

