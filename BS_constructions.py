# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

	# Average runtime for insert is O(log n) because everytime we consider half of the tree
	# as candidate as potential area for we can insert

	# Worst case runtime: O(n) because the tree might be very skewed and unbalanced and we may have to
	# visit all the nodes untill we find the appropriate place at the very end.
	
	# How about space complexity. 
	# think about it, on average case, we consider half the tree every time, so avg space is O(log n)
	# worst case space complexity: O(n) because we may encounter a very skewed tree and have to go through
	# all the nodes to insert at the end or bottom.
#     def insert(self, value):
#         # Write your code here.
# 		# go to the right subtree
# 		if value >= self.value:
# 			if self.right:
# 				self.insert(self.right, value)
# 			else:
# 				self.right = BST(value)
		
# 		# go to the left subtree
# 		else:
# 			if self.left:
# 				self.insert(self.left, value)
# 			else:
# 				self.left = BST(value)		
#         # Do not edit the return statement of this method.
#         return self

# Avg runtime: T: O(log n).  S:O(1)
# worst runtime: T: O(n), tree can be skewed; S: O(1)
	def insert(self, value):
		cur_node = self
		while True:
			# go to right subtree
			if value >= cur_node.value:
				
				if cur_node.right == None:
					cur_node.right = BST(value)
					break
				# just update the cur_node pointer
				else:
					cur_node = cur_node.right
			else:
				if cur_node.left == None:
					cur_node.left = BST(value)
					break
				else:
					cur_node  = cur_node.left		
		return self

	
	# # avg runtime, T: O(log n), and avg space T: O(log n)
	# # worst case T: O(n) and space is also O(n) because we may have to visit all
	# # the nodes in order to search the right node when the tree is very unbalanced
	# # or heavily skewed
	# def contains(self, value):
	# # Write your code here.
	# if self.value == value:
	# 		return True
	# 	if value > self.value:
	# 		self.contains(self.right, value)
	# 	else:
	# 		self.contains(self.left, value)
	# 	return False
	
	# avg runtime:
	# 	T: O(log n)
	# 	S: O(1)
	# worst runtime:
	# 	T: O(n)
	# 	S:(1)
	def contains(self, value):
		cur_node = self
		while cur_node != None:
			if value == cur_node:
				return True
			if value >= cur_node.value:
				cur_node = cur_node.right
			else:
				cur_node = cur_node.left
		return False
		
		
	
    def remove(self, value,parent = None):
		# idea is to have parent node and current node
		cnode = self
		while cnode != None:
			if value > cnode.value:
				parent = cnode
				cnode = cnode.right
			elif value < cnode.value:
				parent = cnode
				cnode = cnode.left
			
			#we found the node we need to remove
			#it is cnode and we also know the parent
			else:
				# case1 
				# c node had legit left and right childs
				if cnode.left != None and cnode.right != None:
					# find the smallest on the right subtree
					cnode.value = cnode.right.findSmallest()
					cnode.right.remove(cnode.value, cnode.right)
				
				
				# EDGE CASE: we want to remove the root node
				# note: we know that at this point cnode at either left or right child BUT NOT Both
				# previous case handles the both case
				if parent == None:
					if cnode.left is not None:
						cnode.value = cnode.left.value
						cnode.right = cnode.left.right
						cnode.left = cnode.left.left
					
					if cnode.right is not None:
						cnode.value = cnode.right.value
						cnode.left = cnode.right.left
						cnode.right = cnode.right.right
				
				# case 2 cnode is the left child of parent
				# make parent point to the correcnt child of the
				# cnode, by-passing it.
				elif parent.left == cnode:
					if cnode.left:
						parent.left = cnode.left
					else:
						parent.left = cnode.right
					
				# case 3: cnode is the right child of parent
				# so we make parent point o the corrent child of
				# the cnode, bi-passing it
				elif parent.right == cnode:
					if cnode.right:
						parent.right = cnode.right
					else:
						parent.right = cnode.left
		
        # Do not edit the return statement of this method.
        return self

	
	def findSmallest(self):
		cur_node = self
		while cur_node.left != None:
			cur_node = cur_node.left
		return cur_node.value

		
		
		
