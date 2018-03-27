mysql:
	docker run -v /tmp/volumes/mysql:/var/lib/mysql --name bonfy-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql

down-mysql:
	docker container stop bonfy-mysql
	docker container rm bonfy-mysql

redis:
	docker run -v /tmp/volumes/redis:/data --name bonfy-redis -p 6379:6379 -d redis redis-server --appendonly yes

down-redis:
	docker container stop bonfy-redis
	docker container rm bonfy-redis

rabbitmq:
	docker run -d --hostname bonfy-rabbit --name bonfy-rabbit -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3-management

down-rabbitmq:
	docker container stop bonfy-rabbit
	docker container rm bonfy-rabbit

postgres:
	docker run --name bonfy-postgres -v /tmp/volumes/postgres:/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres

down-postgres:
	docker container stop bonfy-postgres
	docker container rm bonfy-postgres

# 补充
# docker run -it --link bonfy-redis:redis --rm redis redis-cli -h redis -p 6379
