docker build -t $DOCKER_USERNAME/$REPO_NAME:latest .
echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
docker push $DOCKER_USERNAME/$REPO_NAME:latest