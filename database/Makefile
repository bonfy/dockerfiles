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


# 补充

# docker run -it --link bonfy-redis:redis --rm redis redis-cli -h redis -p 6379