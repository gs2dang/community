# install aws-sdk
sudo pip install --user awscli
export PATH=$PATH:$HOME/.local/bin
echo "awscli install and PATH setting success"

# install ecs-deploy
add-apt-repository ppa:eugenesan/ppa
apt-get update
apt-get install jq -y

curl https://raw.githubusercontent.com/silinternational/ecs-deploy/master/ecs-deploy | \
  sudo tee -a /usr/bin/ecs-deploy
sudo chmod +x /usr/bin/ecs-deploy
echo "ecs-deploy install success"

docker build -t $DOCKER_USERNAME/$REPO_NAME .
echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
docker push $DOCKER_USERNAME/$REPO_NAME:latest

# deploy the new image to the aws ecs
ecs-deploy -c $CLUSTER_NAME -n $SERVICE_NAME -i $DOCKER_USERNAME/$REPO_NAME:latest