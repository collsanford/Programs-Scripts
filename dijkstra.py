#########################################################################
# Collin Sanford
# dijkstra.py
# 02/11/19
# Program the implements dijkstra's algorithim for a graphs link state
#########################################################################

import sys

# parse all the data from the csv file
def start():
        if (len(sys.argv) < 2):
                print "Usage: python {} <datafile>".format(sys.argv[0])
                exit(0)

        datafile = open(sys.argv[1], "r")
        contents = datafile.readlines()
        Node, A, B, C, D, E, F, G, H, I, J  = [], [], [], [], [], [], [], [], [], [], []
        
	for line in contents[1:]:
                x, k, l, m, n, o, p, q, r, s, t = line.strip().split(",")
		Node.append(x)
                A.append(k)
                B.append(l)
                C.append(m)
                D.append(n)
		E.append(o)
		F.append(p)
		G.append(q)
		H.append(r)
		I.append(s)
		J.append(t)

        return Node, A, B, C, D, E, F, G, H, I, J


# prints out a readable table for the data
def printtables(Node, A, B, C, D, E, F, G, H, I, J):

	print "Node A    B    C    D    E    F    G    H    I    J"
	for i in range(len(Node)):
		print "{0:4} {1:4} {2:4} {3:4} {4:4} {5:4} {6:4} {7:4} {8:4} {9:4} {10:4}".format(Node[i], A[i], B[i], C[i], D[i], E[i], F[i], G[i], H[i], I[i], J[i])
		

###############
# Main
##############

#Get individual data
Node, A, B, C, D, E, F, G, H, I, J  = start()

#printtables(Node, A, B, C, D, E, F, G, H, I, J)

# store list A-J into 2d array
data = start()[1:]

# make the data integers
for i in range(len(data)):
	for j in range(len(data[i])):
		data[i][j] = int(data[i][j])


source = raw_input("Please type the node name and press enter: ")

# find the starting node's indice
for i in range(len(Node)):
	if (source == Node[i]):
		sourceind = i
		break

# start with the source node in the shortest path tree
sptSet = []
sptSet.append(sourceind)

# make a list with the distances for the source node
visnode = int(sptSet[len(sptSet) - 1])
dist = data[visnode]

# initialize trees
sourcetree = ['', '', '', '', '', '', '', '', '', '']

# append sourcenode to the source tree for all links
for i in range(len(dist)):
	if (dist[i] < 1000):
		sourcetree[i] += source

for i in range(len(Node)):
	
	# always work with the visiting node
	visnode = int(sptSet[len(sptSet) - 1])

	# if the total distance from sourcenode is less than the current distance
	# replace that distance for that node and update the source tree
	for i in range(len(dist)):
		if ((data[visnode][i] + dist[visnode]) < dist[i]):
			dist[i] = data[visnode][i] + dist[visnode]
			sourcetree[i] = sourcetree[visnode]
			sourcetree[i] += Node[visnode]
		
	sdist = 1000
	
	# choose node with shortest distance that's not in sptSet and append
	for i in range(len(dist)):
		if i not in sptSet:
			if (dist[i] < sdist):
				sdist = dist[i]
				pos = i
	sptSet.append(pos)


# add each node to their own shortest path branch
for i in range(len(sourcetree)):
	if (sourcetree[i] != Node[i]):
		sourcetree[i] += Node[i]

# get rid of redundancy
finaltree = []

for i in range(len(sourcetree)):
	
	unique = True

	for j in range(len(sourcetree)):

		if ((sourcetree[i] in sourcetree[j]) and (sourcetree[i] != sourcetree[j])):
			unique = False
	if (unique):
		finaltree.append(sourcetree[i])
	
# format output
print "Source tree for node {}:".format(source)
print ', '.join(finaltree)
print "Costs for node {}:".format(source)
print "A:{0}, B:{1}, C:{2}, D:{3}, E:{4}, F:{5}, G:{6}, H:{7}, I:{8}, J:{9}".format(*dist)


