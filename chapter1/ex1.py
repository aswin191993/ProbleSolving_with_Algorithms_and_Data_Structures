def anagram(s1,s2):
	if 0 < len(s1) and len(s1) == len(s2):
		list1=list(s1)
		list2=list(s2)
		i=0
		for j in list1:
			temp=1
			if j not in list2:
				return "not an angram"
			else:
				temp = 0
		if temp == 0:
			return "is an anagram"
	else:
		return "not an anagram" 		

















print anagram("qwehjkltyui","iuytrewq")
