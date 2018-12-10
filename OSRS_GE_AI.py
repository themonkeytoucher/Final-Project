import urllib.request, json
from get_item import get_catalogue, get_graph
import math

#class Node:
#    def __init__(self):


def ID3(x, y, label, node):
    node = Node()


def entropy(pos, neg):
	sumpos = sum(pos)
	sumneg = sum(neg)
	return sumpos*log(sumpos, 2) - sumneg*log(sumneg, 2)

if __name__ == "__main__":
    id = int(input("Enter item ID"))
    graph = get_graph(id)
    print(graph['daily'])