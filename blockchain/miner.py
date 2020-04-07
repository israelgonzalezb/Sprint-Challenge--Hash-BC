import hashlib
import requests

import sys
import json

from uuid import uuid4

from timeit import default_timer as timer

import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()
    last_proof = f'{last_proof}'.encode()

    last_hash = hashlib.sha256(last_proof).hexdigest()
    print("Previous proof and hash", last_proof, last_hash)


    print("Searching for next proof")
    def random_proof():
        power = 10**random.randrange(3,17) # create a random power of 10 to help us round our random number on the next line
        return round(random.random()*power) # init proof with a random guess right off the bat
    
    proof = random_proof()
    #  TODO: Your code here
    while valid_proof(last_hash, proof) is False:
        proof = random_proof()

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the hash
    of the new proof?

    IE:  last_hash: ...AE9123456, new hash 123456E88...
    """

    # TODO: Your code here!
    last_hash_trailing_chars = last_hash[-6:]

    proof = f'{proof}'.encode()
    proof = hashlib.sha256(proof).hexdigest()
    proof_leading_chars = proof[:6]

    print("Matcher", last_hash_trailing_chars, proof_leading_chars)
    
    if last_hash_trailing_chars == proof_leading_chars:
        return True
    else:
        return False


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))
