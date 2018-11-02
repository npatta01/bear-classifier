# Image Classifier

My awesome Bear classifier.
Can distinguish between "Teddy" , "Grizzly" , "Black"


# Deployment

## Option A: Heroku
Setup
```
wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh
heroku container:login
```

```
APP_NAME="np-img-classifier"
heroku create $APP_NAME

heroku container:push web --app ${APP_NAME}


heroku container:push web
#new command
heroku container:release web --app ${APP_NAME}
heroku open --app $APP_NAME
```


## Option B: Now
Setup
```
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs


sudo npm install -g --unsafe-perm now 

```

Deploy
```
now
```
