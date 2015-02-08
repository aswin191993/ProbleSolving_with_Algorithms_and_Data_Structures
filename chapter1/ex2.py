
def anagram(s1,s2):
	if 0 < len(s1) and len(s1) == len(s2):
		list1=sorted(list(s1))
		list2=sorted(list(s2))
		i=0
		while i < len(s1):
			temp=0
			if list1[i] == list2[i]:
				i=i+1
				temp=1
			else:
				return "is not an anagram"
				
		if temp == 1:
			return "is an anagram"
	else:
		return "not an anagram" 		

















print anagram("asdfghjkl","lkjhgfdsa")
