import argparse
import requests
from apitesting.utils import *
from apitesting.decorators import timeit

class ApiTesting:
	def __init__(self, filename = "", multiple = False, verborse = False):
		self.multiple = multiple
		self.verborse = verborse
		self.filename = filename

	def compare_apis_response(self):
		

	def call_api(self, method, url, payload, headers):
		response = requests.request(method, url, data=payload, headers=headers)
		return response

	@timeit
	def run_test(self):
		yamlDict = parse_yaml_file(self.filename)
		for key in yamlDict:
			if key == "APIS":
				compareApis, method, requests = fetch_details(yamlDict[key])
				self.process_requests(compareApis, method, requests)


	def process_requests(self, compare, method, requests):
		if compare == True:
			pass
		else:
			for request in requests:
				self.validate_single_api(method, request)

	def validate_single_api(self, method, request):
		url, response_file, postData_file, getData_file = \
		 fetch_request_details(request)

		payload = get_payload(postData_file)
		headers = None
		response = self.call_api(method, url, payload, headers)
		print (response)






