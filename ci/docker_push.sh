echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker tag odarbelaeze/quotes:$TRAVIS_COMMIT odarbelaeze/quotes:latest
docker push odarbelaeze/quotes:$TRAVIS_COMMIT
docker push odarbelaeze/quotes:latest

