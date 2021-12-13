# acs-test-automation
# steps to run the project
step 1:
 pip install -r requirements.txt
step 2:
	(venv) PS D:\sowmy personal\tutorial\python> python src/main.py
	 USD rate is :1.12915
	USD rate is :1.12915
	JPY rate is :128.146656
	JPY rate is :128.146656

# Steps to run docker
    1. docker build -t sowkar/cache-demo:acs .
    2.

# To list created images
    docker images

# To run docker images
    docker run -d --name acs sowkar/cache-demo:acs

# To list all running images
    docker ps -a

# To view container logs
    docker container logs <container id>

# push to repository
    docker push sowkar/cache-demo:acs

# To run pytest
    pytest src/currency_file.py
    