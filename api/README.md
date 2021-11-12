
# Domain Checker API Backend

## Installing Dependencies

### Python 3.7
Follow instructions to install the latest version of python for your platform in the python docs



#### Key Dependencies

- [Flask](http://flask.pocoo.org/)  Flask is required to handle requests and responses. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is used to handle cross origin requests from the frontend server. 
- zeep - (https://docs.python-zeep.org/en/master/)  Python SOAP client
        ```bash
           pip install zeep
        ```
- python-dotenv - (https://pypi.org/project/python-dotenv/) reads key-value pairs from a .env file and can set them as environment variables.
        ```bash
           pip install python-dotenv
        ```

## Running the server


To run the server, execute:

```bash
set FLASK_APP=main.py
flask run
```

## Credential 
In order to be able to interact with the API, it is necessary to sign up to https://regtons.com/en/settings/admins/  and either paste the credential to main.py or create a designated .env file and load the environment variables from there. For more information see http://regtons.com/manual/?cmd=Main

## API Endpoints and Expected Behavior

POST /overit-domenu
General:
Fetches data relative to a domain from SOAP API http://regtons.com/wsdl

Sample: 
curl http://127.0.0.1:5000/overit-domenu -X POST -H "Content-Type: application/json" -d'{"domain_name":"google.com"}

                {
                    "akce": "overeni domeny",
                    "availability": 0,
                    "name": "google.com",
                    "status": "Ok"
                }

