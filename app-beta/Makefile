project = app-beta

image:
	echo "creating image $(project)"
	docker build -t bonfy/$(project) .

docker-run:
	docker run -d --name bonfy-$(project) -p 8888:80 bonfy/$(project)

docker-stop:
	echo "rm image bonfy-$(project)"
	docker stop bonfy-$(project)
	docker rm bonfy-$(project)