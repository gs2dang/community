# install AWS SDK
#pip install --user awscli
#export PATH=$PATH:$HOME/.local/bin

# install necessary dependency for ecs-deploy
#add-apt-repository ppa:eugenesan/ppa
#apt-get update
#apt-get install jq -y

# install ecs-deploy
#curl https://raw.githubusercontent.com/silinternational/ecs-deploy/master/ecs-deploy | \
#  sudo tee -a /usr/bin/ecs-deploy
#sudo chmod +x /usr/bin/ecs-deploy

# or login DockerHub
docker login --username $DOCKER_USERNAME --password $DOCKER_PASSWORD

# build the docker image and push to an image repository
docker build -t $DOCKER_USERNAME/$IMAGE_REPO_NAME:test .
docker tag $DOCKER_USERNAME/$IMAGE_REPO_NAME:test $IMAGE_REPO_FULLNAME:test
docker push $IMAGE_REPO_FULLNAME:test

# update an AWS ECS service with the new image
#ecs-deploy -c $CLUSTER_NAME -n $SERVICE_NAME -i $IMAGE_REPO_FULLNAME:latest
