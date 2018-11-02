# Image Classifier

My awesome Bear classifier.
Can distinguish between "Teddy" , "Grizzly" , "Black"


# Deployment

## Option A: Heroku
Setup
```
wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh
heroku container:login
heroku create img-classifier
```

```
heroku container:push web
#new command
heroku container:release web
heroku open --app img-classifier
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
