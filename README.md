# Sprint Challenge: Hash Tables and Blockchain

This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint, we learned how hash tables combine two data structures to get the best of both worlds and were introduced into the fascinating world of blockchains. In your challenge this week, you will demonstrate proficiency by solving algorithms in Python using hash tables and add another key feature to your blockchain.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your work reflects your proficiency in Python and your command of the concepts and techniques in related to hash tables and blockchains.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.

## Description

This sprint challenge is divided up into three parts:  Hash tables coding, blockchain coding, and a short interview covering parts of hash tables and blockchain.

## Interview Questions

Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?
    - To access an item in an array, we need that item's index in the array. That operation occurs in constant time.
    - To add or remove an item from the front of an array requires shifting all other items in the array. That makes that operation O(n) in the worst case.
    - To add an item at the end of an array is considered constant amortized time. This is because the array's capacity may need to be increased, which involves allocating a new chunk of memory and copying all items to the new larger array. In the best case it is O(1) and in the worst cas it would be O(n).
* What is the worse case scenario if you try to extend the storage size of a dynamic array?
    - In the worst case it would be O(n), otherwise known as linear time. That's because the amount of operations could end up matching the amount of items in the array, as each item has to be copied over from the smaller array to the new larger array.


Explain how a blockchain is structured. 
* What are the blocks, what is the chain? How is the data organized?
    - A blockchain is basically a linked list of objects or dictionaries, otherwise known as blocks. These blocks contain certain pieces of data like a timestamp, the hash of the preceding block, some transactions encoded in that block, etc. The chain then is this linkage of blocks by hash.
* Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?
    - Proof of work is a system for producing pieces of data that are hard and costly to create but can easily be verified by another person. Because generating proofs requires time, energy and processing power, the systems that are working to generate those proofs only have as much power over the blockchain as they can afford. To overcome the entire network, an individual would have to control 51% of the network, thus increasing their chance of generating the correct hash before everyone else. This is called a 51% attack. The economics of this makes it exceedingly unlikely that it would occur, i.e. because the costs would not only outweigh the rewards, but the network would lose trust in the entire chain if it is discovered that one group or individual controls 51% amount of the workers.

    To generate a proof, a miner takes a stringification of the latest block in the chain and appends a random nonce to that block string. A hash is then generated from that block string-nonce concatenation. If that hash matches the verification parameters of the blockchain, the miner submits that proof to the blockchain node to collect a reward. The blockchain node then verifies that the proof matches the parameters, for example, that the generated hash is preceded by a certain amount of leading zeroes, and then decodes that hash to verify that the latest block in the chain is included in the proof.

## Project Set Up

#### [Hash Tables]

For the hash tables portion of the sprint challenge, you'll be working through two algorithm problems that are amenable to being solved efficiently using a hash table. You know the drill at this point. Navigate into each exercise's directory, read the instructions for the exercise laid out in the README, implement your solution in the .py skeleton file, then make sure your code passes the tests by running the test script with make tests.

A hash table implementation has been included for you already. Your task is to get the tests passing (using a hash table to do it). You can remind yourself of what hash table functions are available by looking at the hashtable.py file that is included in each exercise directory (note that the hash table implementations for both exercises differ slightly).

*You may not use any advanced, built-in Python functions to solve these problems.*

#### [Blockchain]

For the blockchain portion of the challenge, you will be writing code for a new miner that will solve a different Proof of Work algorithm than the one we have been working with.

Your goal is to mine at least one coin.  Keep in mind that with many people competing over the same coins, this may take a long time.  By our math, we expect that an average solution should be the first to find a solution at least once in an hour or two of mining.  

## Minimum Viable Product

#### [Hash Tables](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/hashtables)

#### [Blockchain](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/blockchain)


### Rubric

| *OBJECTIVE*                                                                                                     | *TASK*             | *1 - DOES NOT MEET EXPECTATIONS*                                                                                            | *2 - MEETS EXPECTATIONS*                                                                                                       | *3 - EXCEEDS EXPECTATIONS                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| implement and describe how high-level array functions work down to the memory level                             | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
| implement and utilize basic hash table + handle collisions and resizing in a hash table                         | Hash Problem 1 & 2 | Tests do not pass on one or both problems, or solutions do not use hash tables.                                             | Tests pass on both problems.  Solution utilizes a hash table.                                                                  | Tests pass on on both problems with solutions utilizing hash tables, linear runtime complexity, no flake8 complaints.                                 |
| diagram and code a simple blockchain, utilizing a cryptographic hash                                            | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
| utilize a Proof of Work process to protect a blockchain from attack                                             | Blockchain Problem | The student is unable to mine a coin before the end of lunch.                                                               | The student was able to mine a coin before the end of lunch.                                                                   | The student presented a unique solution that was able to mine more than 100 coins before the end of lunch.                                            |
| build a protocol to allow nodes in a blockchain network to communicate to share blocks and determine consensus. | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |

## Grading
The grade for this sprint challenge is the average of the number of points received (points/15)
