# Clidio-Demo


## Requirements
  * Python-version -: Python 3.9.9
  * Django-version -: 4.0.0

### After installing requirements cross-check it using:
```sh
$ python3 -V
$ django-admin --version
```
## Setup

The first thing to do is to clone the repository:
```sh
$  git clone https://github.com/AvinashRajPurohit/Clidio_Demo.git
$ cd Clidio_Demo
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ sudo apt install python3-venv
$ python3 -m venv env
$ source env/bin/activate
```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Once `pip` has finished downloading the dependencies:

# Add the SECRET_KEY in Env variables:
```
export SECRET_KEY=django-insecure-chm2=7o$x7s8l7846w-8ndipj_hn^vwb)&ruusm4dw=1e+93k=
```

## DataBase configurations
Set Debug=True for using sqlite /or/ configure DB 


```sh
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`


 

