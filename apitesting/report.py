

def generate_cmd_report(unmatchedKeys, unmatchedValues):
	if len(unmatchedKeys) <= 0:
		print ("\033[1;32;40m All key from both response matched")
	else:
		print ("\033[1;31;40m Some key from both the response did not matched")
		print ("\033[1;31;40m ", unmatchedKeys)

	if len(unmatchedValues) <= 0:
		print ("\033[1;32;40m All values from both response matched")
	else:
		print ("\033[1;31;40m Some values from both the response did not matched")
		print ("\033[1;31;40m ", unmatchedValues)