from input import parseTree
from dfs import *
from bfs import bfs

print "Tree:"
nodes, edges = parseTree()
print "Test dfs"
print "Preorder"
print map(lambda x: nodes[x], preorder(edges, 0))
print "Inorder"
print map(lambda x: nodes[x], inorder(edges, 0))
print "Postorder"
print map(lambda x: nodes[x], postorder(edges, 0))
print "Test bfs"
print map(lambda x: nodes[x], bfs(edges, 0))
