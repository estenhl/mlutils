def tokens_to_ids(text):
	ids = []
	refs = {}

	for paragraph in text:
		for token in paragraph:
			token = token.lower()
			if token in refs:
				ids[refs[token]] = {'token': token, 'count': ids[refs[token]]['count'] + 1}
			else:
				ids.append({'token': token, 'count': 1})
				refs[token] = len(ids) - 1

	return ids, refs
