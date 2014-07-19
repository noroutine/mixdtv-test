How I learn Python
----


### To not forget how to install python on Mac with pip and virtualenv

Python 3.4

```
sudo port install python34 py34-pip py34-virtualenv
sudo port select --set python python34
sudo port select --set pip pip34
sudo port select --set virtualenv virtualenv34
```

Python 2.7

```
sudo port install python27 py27-pip py27-virtualenv
sudo port select --set python python27
sudo port select --set pip pip27
sudo port select --set virtualenv virtualenv27
```

### Automatic python virtualenv 

[Gist](https://gist.github.com/noroutine/55c49ee39e65a5643302)

### pip requirements file allows to install project packages

```
pip freeze > requirements.txt
```

[Everything Jeff Knupp knows about Python...](http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)

[Some other intro](http://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/)
