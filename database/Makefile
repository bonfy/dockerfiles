mysql:
	docker run -v /tmp/volumes/mysql:/var/lib/mysql --name bonfy-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=abc123 -d mysql

down-mysql:
	docker container stop bonfy-mysql
	docker container rm bonfy-mysql

redis:
	docker run -v /tmp/volumes/redis:/data --name bonfy-redis -p 6379:6379 -d redis redis-server --appendonly yes

down-redis:
	docker container stop bonfy-redis
	docker container rm bonfy-redis

rabbitmq:
	docker run -d --hostname bonfy-rabbit --name bonfy-rabbit -e RABBITMQ_DEFAULT_USER=root -e RABBITMQ_DEFAULT_PASS=abc123 rabbitmq:3-management

down-rabbitmq:
	docker container stop bonfy-rabbit
	docker container rm bonfy-rabbit

# 补充

# docker run -it --link bonfy-redis:redis --rm redis redis-cli -h redis -p 6379