build-image:
	docker build -t python-fastapi .

build-image-nc:
	docker build --no-cache -t python-fastapi .

run-image:
	docker run -it python-fastapi

run-shell:
	docker run -it --entrypoint "/bin/bash" python-fastapi

run-app:
	docker run -p 8000:80 python-fastapi

run-app-bg:
	docker run -p 8000:80 --name myfastapicontainer -d python-fastapi