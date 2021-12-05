bi:
	isort src/Python
	black src/Python
	
test:
	flake8 src/Python
	mypy --ignore-missing src/Python
	pytest src/Python
build:
	docker-compose up -d