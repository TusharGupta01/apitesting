import argparse
import requests
from apitesting.utils import *
from apitesting.report import *
from apitesting.decorators import timeit

class ApiTesting:
	def __init__(self, filename = "", multiple = False, verborse = False):
		self.multiple = multiple
		self.verborse = verborse
		self.filename = filename

	def compare_apis_response(self, response1, response2):
		return compare_json(response1, response2)

	def compare_two_api(self, response1, response2):
		return compare_json(response1, response2)

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
			self.validate_multiple_api(method, requests)
		else:
			for request in requests:
				self.validate_single_api(method, request)

	def validate_single_api(self, method, request):
		url, response_file, postData_file, getData_file = \
		 fetch_request_details(request)

		payload = get_payload(postData_file)
		response_from_file = get_response(response_file)
		headers = None
		response = self.call_api(method, url, payload, headers)
		unmatchedKeys, unmatchedValues = self.compare_apis_response(\
			response.text, response_from_file)
		# generate_cmd_report(unmatchedKeys, unmatchedValues)

	def validate_multiple_api(self, method, requests):
		i = 0
		j = 0
		headers = None
		for i in range(0, len(requests)):
			url_i, response_file, postData_file, getData_file = \
		 		fetch_request_details(requests[i])
			payload_i = get_payload(postData_file)
			response_from_file_i = get_response(response_file)
			for j in range(i+1, len(requests)):
				url_j, response_file, postData_file, getData_file = \
		 			fetch_request_details(requests[j])
				payload_j = get_payload(postData_file)
				response_from_file_j = get_response(response_file)
				response_i = self.call_api(method, url_i, payload_i, headers)
				response_j = self.call_api(method, url_j, payload_j, headers)
				unmatchedKeys, unmatchedValues = self.compare_apis_response \
					(response_i.text, response_j.text)
				generate_cmd_report(unmatchedKeys, unmatchedValues)









