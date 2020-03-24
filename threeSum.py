def threeNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
	answer_lst = []
	
	for c_index in range(len(array)):
		
		current_num = array[c_index]
		
		l = c_index + 1
		r = len(array) - 1
		
		while l < r:
			local_sum  = current_num + array[l] + array[r]
			
			if local_sum == targetSum:
				answer_lst.append([current_num, array[l], array[r]])
				l+=1
				r-=1
			
			if local_sum < targetSum:
			# we can add something bigger, so let's move the left pointer to someone who is probably bigger
				l+=1
			if local_sum > targetSum:
				r-=1
	return answer_lst
				

# T: O(nlogn) + O(n^2) ~ O(n^2)
# S: O(n) because we are storing a list of lists and the number of tems in the answer list is bouned by n
