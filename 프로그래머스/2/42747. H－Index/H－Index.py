def solution(citations):
	# 1. 내림차순 정렬
	citations.sort(reverse=True)
	print(citations)
    
	# 2. 인덱스 번호와 h값 비교
	for i, citation in enumerate(citations):
		if i+1 > citation:
			return i
	return len(citations)