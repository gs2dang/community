docker build -t gs2dang/bulletin_board:test .
echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
docker push gs2dang/bulletin_board:test