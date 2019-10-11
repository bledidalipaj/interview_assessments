# Instrcutions

1. Setting up 

Build the docker image by running the following command:

```
$ docker build -t mars_exploration .
```

After the image is successufly built, run the container with the command bellow:

```
$ docker run -p 5000:5000 mars_expoloration
```

Then you should see the output of running the mars_exploration.py script.

