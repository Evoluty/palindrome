def is_pal(s):
	return s[::-1] == s


def get_all_substrings(s, size):
	res = []
	for i in range(len(s)-size+1):
		res.append(s[i:i+size])
	return res


def biggest_pal(s):
	size = len(s)
	while (size > 1):
		sub_str = get_all_substrings(s, size)
		for item in sub_str:
			if (is_pal(item)):
				return item		
		size=size-1
	return s[0]


def main():
	print(biggest_pal("testtest"))

if __name__ == '__main__':
    main()
