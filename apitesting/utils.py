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
		print ("Error Occured: YAML file format is not correct, could not find 'APIS'")
	else:
		return reader
				
def parse_json(filename):
	if if_exits(filename):
		with open(filename) as f:
	    	data = json.load(f)
	else:
		return filename + " does not exits or File path is wrong!!"

def get_url(filename):
	return None

def diff_json(json1, json2):
	return None

def diff_type(json1, typejson):
	return None

def if_exits(filename):
	return os.path.isfile(filename)


