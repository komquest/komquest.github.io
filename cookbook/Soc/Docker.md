# Docker Default Container location
```
/var/lib/docker
```

# Docker Commands
```
docker container ls

docker container inspect
```

# Login to Docker Container and copy a file from it:

```
docker ps

docker exec -it --user root ContainerId/Name bash

bash-4.2$ cd yourapplication/path/log/

bash-4.2$ exit


 docker cp edd5064178db:yourapplication/path/log/request.log /your/local/location
```

# Links

- Use bind mounts to access external file outside container:
https://docs.docker.com/storage/bind-mounts/

---

# Pics

![image](https://user-images.githubusercontent.com/97367610/149612962-2ef61002-e5af-441f-a92b-97d590c3ca38.png)
