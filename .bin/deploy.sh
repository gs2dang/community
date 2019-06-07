# install aws-sdk
pip install --user awscli
export PATH=$PATH:$HOME/.local/bin
echo "awscli install and PATH setting success"

# install ecs-deploy
add-apt-repository ppa:eugenesan/ppa
apt-get update
apt-get install jq -y

#curl https://raw.githubusercontent.com/silinternational/ecs-deploy/master/ecs-deploy | \
#  sudo tee -a /usr/bin/ecs-deploy
#sudo chmod +x /usr/bin/ecs-deploy
echo "ecs-deploy install success"

# Use this for AWS ECR
# eval $(aws ecr get-login --region us-east-1)

# Use this for Docker Hub
docker login --username $DOCKER_USERNAME --password $DOCKER_PASSWORD

# Build and push the image to the repository
docker build -t $DOCKER_USERNAME/$IMAGE_REPO_NAME .
echo "Docker build success"
#echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
docker tag $DOCKER_USERNAME/$IMAGE_REPO_NAME:latest $IMAGE_REPO_FULLNAME:latest

docker push $DOCKER_USERNAME/$IMAGE_REPO_NAME:latest
echo "Docker push success"
# deploy the new image to the aws ecs
ecs-deploy -c $CLUSTER_NAME -n $SERVICE_NAME -i $IMAGE_REPO_FULLNAME:latest