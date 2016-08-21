def is_isomorphic(str1, str2):

	if not len(str1) == len(str2):
		return False

	char_map = {}

	for i in range(len(str1)):
		c1 = str1[i]
		c2 = str2[i]

		if c1 in char_map:
			if not c2 == char_map[c1]:
				return False

		else:
			for key, value in char_map.iteritems():
				if value == c2:
					return False

			char_map[c1] = c2

	return True

print is_isomorphic("egg", "add")


print is_isomorphic("foo", "bar")