# webfortune

## About
This web application will have the following features

```/fortune/```
Where you can get a random fortune

```/cowsay/<anytext>```
Where you can have a cow repeat your text back to you

```/cowfortune/```
Where you can have a cow tell you a random fortune

You can run this either via locally or through a docker image

## Running locally
To run this web application locally follow these directions
* Clone the repository by ```git clone https://github.com/SamBardwell/webfortune```
* Navigate to the repository
* Create a virtual environemnt by ```python3 -m venv env
* Activate the environment ```source env/bin/activate```
* Install the requeirments.txt ```pip install -r requirments.txt```
* Start the flask application ```flask run --host=0.0.0.0```
* Go to this url ```http://10.92.21.106:5000/```
* After the 5000 you navigate to the following
```
/fortune/
/cowsay/<anytext>
/cowfortune/
```
* Once you are done using the application, in the terminal you can press ```CTR-C```
* Then deactivate your environment by typing ```deactivate```
