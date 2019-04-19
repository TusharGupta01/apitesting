

def generate_cmd_report(unmatchedKeys, unmatchedValues):
	if len(unmatchedKeys) <= 0:
		print ("\033[1;32;40mAll key from both response matched")
	else:
		print ("\033[1;31;40mSome key from both the response did not matched")
		print ("\033[1;31;40m ", unmatchedKeys)

	if len(unmatchedValues) <= 0:
		print ("\033[1;32;40mAll values from both response matched")
	else:
		print ("\033[1;31;40mSome values from both the response did not matched")
		for unmatchedValue in unmatchedValues:
			print (unmatchedValue)