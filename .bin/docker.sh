# Use this for Docker Hub
docker login --username $DOCKER_USERNAME --password $DOCKER_PASSWORD
echo "DockerHub login success"

# Build and push the image to the repository
docker build -t $DOCKER_USERNAME/$IMAGE_REPO_NAME .
echo "Docker build success"
docker tag $DOCKER_USERNAME/$IMAGE_REPO_NAME:test $IMAGE_REPO_FULLNAME:test
docker push $DOCKER_USERNAME/$IMAGE_REPO_NAME:test
echo "Docker push success"