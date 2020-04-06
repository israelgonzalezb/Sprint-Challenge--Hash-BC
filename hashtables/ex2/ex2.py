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