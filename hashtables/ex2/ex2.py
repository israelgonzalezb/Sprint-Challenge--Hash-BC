#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1) # minus one to get rid of final "NONE" destination in return array

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    index = 0
    while index < len(route):
        print(index)
        if index == 0:
            route[index] = hash_table_retrieve(hashtable, "NONE")
            print(route[index])
        else:
            route[index] = hash_table_retrieve(hashtable, route[index-1])
        index += 1
    
    return route

# Code used to test inline
# ticket_1 = Ticket("PIT", "ORD")
# ticket_2 = Ticket("XNA", "SAP")
# ticket_3 = Ticket("SFO", "BHM")
# ticket_4 = Ticket("FLG", "XNA")
# ticket_5 = Ticket("NONE", "LAX")
# ticket_6 = Ticket("LAX", "SFO")
# ticket_7 = Ticket("SAP", "SLC")
# ticket_8 = Ticket("ORD", "NONE")
# ticket_9 = Ticket("SLC", "PIT")
# ticket_10 = Ticket("BHM", "FLG")

# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
#             ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

# expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
#             "SLC", "PIT", "ORD"]
# result = reconstruct_trip(tickets, 10)

# print(result, expected)

class Graph:
    def __init__(self):
        self.vertices = {
            "A": {"B": 1},
            "B": {"C": 3, "D": 2},
            "C": {"E": 4},
            "D": {"E": 2},
            "E": {"F": 3},
            "F": {},
            "G": {"D": 1}
        }

class Graph:
    def __init__(self):
        #  A B C D E F G
        #A
        #B
        #C
        #D
        #E
        #F
        #G
        self.edges = [[0,1,0,0,0,0,0],
                      [0,0,3,2,1,0,0],
                      [0,0,0,0,4,0,0],
                      [0,0,0,0,2,0,0],
                      [0,0,0,0,0,3,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0]]

"""
The adjacency list takes up less space than the matrix, because the matrix tracks all edges.

It would be easier to add an item to the adjaceny list, because the matrix involves multiple array methods and shifts.

The graph is directed, so removing at item from the list would be easier.
Removing from the matrix would involve multiple array methods.

Finding an edge is easy in both.

Getting all edges is more difficult in the matrix because you would have to iterate through an entire row.
With the list, you ould just return the value of the specific vertex.
"""