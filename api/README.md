
# Domain Checker API Backend

## Installing Dependencies

### Python 3.7
Follow instructions to install the latest version of python for your platform in the python docs



#### Key Dependencies

- [Flask](http://flask.pocoo.org/)  Flask is required to handle requests and responses. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is used to handle cross origin requests from the frontend server. 
- [zeep] (https://docs.python-zeep.org/en/master/)  Python SOAP client
        ```bash
           pip install zeep
        ```

## Running the server


To run the server, execute:

```bash
set FLASK_APP=api.py
set FLASK_ENV=development
flask run
```
## API Endpoints and Expected Behavior

POST /objednat
General:
Sends email address, name of student and the course he/she signed up for

Sample: 
curl http://127.0.0.1:5000/objednat -X POST -H "Content-Type: application/json" -d'{"first_name":"John", "last_name":"Smith", "starting_date":"2021-11-03", "course_name":"Mzdové účetnictví", "email":"example@example.com"}


GET /text2'
General:
This endpoint fetches data related to the selection of courses for economists

sample: curl http://127.0.0.1:5000/text2

      singleCardContent = [
              {
                "id": 1,
                "url": "/kurzy/",
                "nadpis": "Mzdové účetnictví",
                "foto": "mzdove.jpg",
                "cena": "10 990 Kč",
                "trvani": "80 hodin",
                "obsah": ["daň z příjmu",
                          "daň z příjmu právnických osob",
                          "daň z přidané hodnoty",
                          "silniční daň",
                          "daň z převodu nemovitostí",
                          "spotřební daně",
                          ]
            },
            {
                "id": 2,
                "url": "/kurzy/",
                "nadpis": "Daňová evidence",
                "foto": "dane.jpg",
                "cena": "5 990 Kč",
                "trvani": "40 hodin",
                "obsah": ["daň z příjmu fyzických osob",
                          "daň z příjmu právnických osob",
                          "daň z přidané hodnoty",
                          "silniční daň",
                          "daň z nemovitosti",
                          "daň dědická",
                          "daň darovací",
                          "daň z převodu nemovitostí",
                          "spotřební daně",
                          "daňový řád", ]
            },
            ]

GET /ucetnictvi'
General:
This endpoint fetches data related to the selection of financial services offered by the school
sample: curl http://127.0.0.1:5000/ucetnictvi


    ucetnictviContent = [
        {
            "id": 1,
            "url": "/ucetnictvi/",
            "nadpis": "ÚČETNICTVÍ",
            "foto": "mzdove.jpg",
            "cena": "",
            "trvani": "",
            "obsah":[
                    "Vedení deníku a hlavních knih",
                    "Evidence majetku",
                    "Roční uzávěrka",
                    "Nemusíte platit upgrade účetního a mzdového softwaru",
                    "Vyhotovování přehledů, sestav, tabulek"
                      ]
        },
        {
            "id": 2,
            "url": "/ucetnictvi/",
            "nadpis": "DAŇOVÁ EVIDENCE",
            "foto": "dane.jpg",
            "cena": "",
            "trvani": "",
            "obsah": ["Vedení peněžního deníku",
                      "Vedení knih pohledávek a závazků",
                      "Evidence majetku",
                      "Evidence DPH",
                      "Roční uzávěrka",
                      "Vyhotovování přehledů, sestav a tabulek",
                    ]
        },
]

