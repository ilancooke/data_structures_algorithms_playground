'''
Implement a simple encoding for a collection of strings. The encoding should be as compact as possible, and should allow for efficient retrieval of the original strings. 

Example 1:
Input: ["hello", "world"]
'''


def decode(encoded):
	pos = 0 #main pointer
	result = []
	while pos < len(encoded):
		#find the length
		sep = pos #second pointer
		while encoded[sep] != '#':
			sep += 1 #at the end, sep will be at the end of the length portion, string starts at sep+1
		#length portion
		string_length = int(encoded[pos:sep])
		#read the string
		start = sep+1
		end = start+string_length
		result.append(encoded[start:end])
		
		# move pointer to the end of our string
		pos = end
	return result
	
	
def decode(encoded):
	pos = 0 #main pointer
	result = []
	while pos < len(encoded):
		#find the length
		sep = pos #second pointer
		while encoded[sep] != '#':
			sep += 1 #at the end, sep will be at the end of the length portion, string starts at sep+1
		#length portion
		string_length = int(encoded[pos:sep])
		#read the string
		start = sep+1
		end = start+string_length
		result.append(encoded[start:end])
		
		# move pointer to the end of our string
		pos = end
	return result