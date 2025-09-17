def solution(numbers):
	from itertools import permutations
	answer = 0
	
	def generate_permutations(number: int):
		num_list = list(number)
		all_permutations = []
		for i in range(1, len(num_list)+1):
			p = permutations(num_list, i)
			all_permutations.extend(p)
		return set([int(''.join(permutation)) for permutation in all_permutations])
	
	def is_prime(n: int):
		if n < 2:
			return False
		
		for i in range(2, n):
			if n%i == 0:
				return False
		return True
	
	for num in generate_permutations(numbers):
		if is_prime(num):
			answer += 1
			
	return answer
