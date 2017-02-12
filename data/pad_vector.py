import numpy as np 

def pad_vector(vector, padding, length, prefix=True):
	pad_length = length - len(vector)
	padded_vector = np.repeat(padding, pad_length)

	if prefix:
		full_vector = np.concatenate((padded_vector, vector))
	else:
		full_vector = np.concatenate((vector, padded_vector))

	return full_vector