project = flask-beta

image:
	echo "creating image $(project)"
	docker build -t bonfy/$(project) .
swarm:
	docker swarm init
	docker stack deploy -c docker-compose.yml $(project)
remove-swarm:
	docker stack rm $(project)
	docker swarm leave --force