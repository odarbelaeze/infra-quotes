echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push odarbelaeze/quotes:$TRAVIS_COMMIT