# Python Project

The containers can be made up by using below commands.

```
docker-compsoe build
docker-compose up -d
```

## How to create DB
Application runs on 9000 port.

http://hostIP:9000/script - it creates db named script first time
http://hostIP:9000/script - it warn db already created after that.

For another DB to create we need to hit like http://hostIP:9000/script1
