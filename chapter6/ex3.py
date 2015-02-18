
import binarysearch

def new_find_successor(tree):
	current = tree.root.find_min()
	while current != None:
		print '%d : %s' %(current.key,current.payload)
		current = current.find_successor()


new_tree = binarysearch.binarysearch()
new_tree[3] = "red"
new_tree[4] = "blue"
new_tree[6] = "yellow"
new_tree[2] = "at"

new_find_successor(new_tree)
