# flask-gcp
Create a simple flask app and host it on Google Cloud Platform. The app also integrates JS and CSS. 

### Commands to create docker container and run locally (Need to install docker)
docker build --tag gcp_flask_boilerplate .
docker run -p 5000:5000 gcp_flask_boilerplate

### Initialize gcloud
gcloud init

### Check if you are in right project
gcloud config get-value project

### Deploy on GCP
gcloud run deploy gcp_flask_boilerplate --region=europe-west2 --source=$(pwd) --allow-unauthenticated
