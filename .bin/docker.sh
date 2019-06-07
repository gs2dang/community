docker build -t $DOCKER_USERNAME/$IMAGE_REPO_NAME .
echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
docker push $DOCKER_USERNAME/$IMAGE_REPO_NAME:test
