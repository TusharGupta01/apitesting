# ApiTesting

ApiTesting is a very handy library to test your apis.

### Functionality
- Compare response with response file.
- Compare one api response with another.
- Compare type of the response or get type of each key in response.

### Installation

ApiTesting is complete written in python3. 

Install the dependencies and devDependencies.

```sh
$ pip3 install -r requirements_dev.txt
```

Setup the Library...

```sh
$ python3 setup.py install
```

### How to use it?

```python
import apitesting

tester = apitesting.ApiTesting(filename = "test.yaml")
tester.run_test()
```

YAML file format
```
APIS:
  compare: False
  method: POST
  request1:
    url: http://localhost:8000/cfutilservice/v1/shorten
    filepath:
      response_file: ./response/shorten.json
      postData_file: ./postData/shorten.json
  request2:
    url: http://localhost:8000/cfutilservice/v1/shorten
    filepath:
      response_file: ./response/shorten.json
      postData_file: ./postData/shorten.json
```







