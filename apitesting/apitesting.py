import argparse
import requests
import apitesting.utils as utils

class ApiTesting:
	def __init__(self, filename = "", multiple = False, verborse = False):
		self.multiple = multiple
		self.verborse = verborse
		self.filename = filename

	def diff_apis(self):
		print ("This is api diff function")

	def call_api(self, method = "POST", url, payload, headers):
		# utils.parse_yaml_file(filename)
		payload = "{\n\"url\": \"http://localhost:8000/cfutilservice/v1/shorten\"\n}"
		url = "http://localhost:8000/cfutilservice/v1/shorten"
		headers = {
		    'cache-control': "no-cache",
		    'postman-token': "0230ced8-6e21-80f3-ddc1-b5642ecc2fea"
		    }
		response = requests.request(method, url, data=payload, headers=headers)

	def run_test(self):
		readerDict = utils.parse_yaml_file(self.filename)
		if 


