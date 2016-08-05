# Deploy flask code in Docker Machines
I am sure you guys want to try `docker`, it pretty new thing in the market and developer are appreciating.

## How to use

1. Download [docker](https://www.docker.com/products/docker-toolbox) package from their offical page.
2. Will use `docker-machine` which require [VirtualBox](https://www.virtualbox.org/) as prerequisite.
3. Type `docker-machine create -d virtualbox dev`
4. Follow instruction mention on console to export and eval variable and put in `.bashrc`
5. Type `docker-machine ls`
  ```sh
        
           NAME   ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER    ERRORS
           dev    *        virtualbox   Running   tcp://192.168.99.100:2376           v1.10.3
        
  ```
6. Navigate to `ops` folder and type `docker-compose up -d`
7. After successful build then type http:<docker-ip> for my case it's [http://192.168.99.100](http://192.168.99.100)

## Checklist

- [x] Create `guincorn` server and docker-compose.
- [x] Create `nginx` docker-compose.
- [ ] Static `js/css` example in flask and server from nginx.
- [ ] Flask Example of use of `postgres`.
- [ ] Docker image of postgres and usage.

## Issues:-
Feel free to raise it over [here](https://github.com/arpit2438735/docker_compose_centos_flask-gunicorn-nginx-postgres/issues).
