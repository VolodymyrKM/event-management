EVENT MANAGEMENT sample application
Setup
The first thing to do is to clone the repository:

$ git clone https://github.com/VolodymyrKM/event-management.git

$ cd eventmanagement
Create a virtual environment to install dependencies in and activate it:

$ python3 -m venv env
$ source env/bin/activate
Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment.

Once pip has finished downloading the dependencies:

(env)$ cd event_management
(env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/


(env)$ python3 manage.py test event_app
