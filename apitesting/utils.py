import yaml
import os
import json

def read_yaml(filename):
	if if_exits(filename):
		with open(filename, 'r') as stream:
		    try:
		        return yaml.safe_load(stream)
		    except yaml.YAMLError as exc:
		        print("Error Occured:", exc)
	else:
		return filename + " does not exits or File path is wrong!!"

def parse_yaml_file(filename):
	reader = read_yaml(filename)
	if "APIS" not in reader:
		print ("Error Occured: YAML file format is not correct, could not \
		 find 'APIS'")
	else:
		return reader
				
def parse_json(filename):
	if if_exits(filename):
		with open(filename) as f:
			return json.load(f)
	else:
		return filename + " does not exits or File path is wrong!!"

def load_json(filename):
	return open(filename, 'rb').read()

def fetch_details(api_dict):
	compareApis = False
	method = "POST"
	requests = []
	for key in api_dict:
		if key == "compare":
			try:
				compareApis = bool (api_dict["compare"])
			except:
				compareApis = False
				print ("\033[1;33;40m Compare is not either of True or False")
		elif key == "method":
			method = api_dict["method"]
		elif "request" in key:
			requests.append(api_dict[key])
		else:
			print ("\033[1;31;40m " + key + " is not expected in yaml file.")
	return compareApis, method, requests

def fetch_request_details(request):
	url = ""
	response_file = ""
	postData_file = ""
	getData_file = ""
	if "url" in request:
		url = request["url"]
		if "filepath" in request:
			for file in request["filepath"]:
				if file == "response_file":
					response_file = request["filepath"]["response_file"]
				elif file == "postData_file":
					postData_file = request["filepath"]["postData_file"]
				elif file == "getData_file":
					getData_file = request["filepath"]["getData_file"]
	else:
		print ("\033[1;31;40m Url is not given for request.")
	return url, response_file, postData_file, getData_file

def get_payload(filename):
	return load_json(filename)

def compare_json(json1, json2):
	unmatchedKeys = []
	unmatchedValues = []
	json_dict_a = json.loads(json1)
	json_dict_b = json.loads(json2)
	for key in json_dict_b.keys():
	    value = json_dict_b[key] 
	    if key not in json_dict_a:
	    	unmatchedKeys.append(key)
	    else:
	    	if json_dict_a[key] != value:
	    		unmatchedValues.append({ key : value })
	return unmatchedKeys, unmatchedValues

def get_response(filename):
	return load_json(filename)

def if_exits(filename):
	return os.path.isfile(filename)
