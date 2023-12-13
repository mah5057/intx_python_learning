APP_NAME := web_app

.PHONY: docker-up
docker-up:
	docker build -t web_app .
	docker run web_app
