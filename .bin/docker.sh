# Build and push the image to the repository
docker build -t $DOCKER_USERNAME/$IMAGE_REPO_NAME .
echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
docker tag $DOCKER_USERNAME/$IMAGE_REPO_NAME:test $IMAGE_REPO_FULLNAME:test
docker push $DOCKER_USERNAME/$IMAGE_REPO_NAME:test