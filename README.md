# flask-gcp
Create a simple flask app and run it on Google Cloud Platform

docker build --tag flask_skeleton .
docker run -p 5000:5000 flask_skeleton

gcloud init

gcloud config get-value project

# This will build your container
docker build --tag gcp_flask_boilerplate .

# Run the container
docker run -p 5000:5000 gcp_flask_boilerplate

gcloud run deploy gcp_flask_boilerplate --region=europe-west2 --source=$(pwd) --allow-unauthenticated
