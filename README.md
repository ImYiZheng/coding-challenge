Hello, my name is Yi Zheng, Let's get started!
===========================================================
Insight Data Engineering - Coding Challenge

## Quick scan

   - In the tweet_input directory, the input tweets.txt has size 27.3M, including 9999 tweets, this file is from data-gen directory.The corresponding output output.txt is in tweet_output directory.   
   - In insight_testsuite directory, I made two simple tests. You can find the corresponding outputs in the tweet_output directory.

## Development Summary

I write all codes in Python.  

The functions of my tool:

1. Extract the hashtags and created_at fields from the raw JSON tweets that come from a prepared tweets file.
2. Build a Twitter hashtag graph.
3. Calculate the average degree of a vertex in a Twitter hashtag graph for the last 60 seconds, and update this each time a new tweet appears.

## Algorithm and Data Structure
Implement the hashtag graph with double linked list.

1. LRU (least recently used) algorithm: Aims to calculate the average degree with tweets in latest 60s and remove the timeout tweets. It also provides the edge number of every node. 
   - It's implemented with HashMap and Double LinkedList. 
   - The key of the HashMap is a hashtag_pair (e.g. ('#apache', '#hadoop')), while the value is a doubly LinkedList Node which contains the same hashtag_pair, the datetime of the tweet and the two linked list pointers, Next and Previous. 
   - The Double LinkedList is sorted in ascending order with datetime, which would be helpful to remove timeout hashtag_pair. 
   - Whenever I update the graph, I will add new edges and remove timeout edges, which are outside the latest 60 seconds window. Such data structure is **O(1) time complexity** when put or remove an element. 
2. Graph Adjacent Set: Aims to get total nodes in the graph. 
   - Store the whole graph information with HashMap, which key is node (hashtag) in the graph, value is a set of neighbor (hashtags appear in the same tweet with the key). 
   - I choose HashMap and HashSet because get() and set() of them are **O(1) time complexity**. 
   - Whenever I update the graph, I will add new nodes and related neighbours and remove timeout nodes and related neighbours.

The code files contain detailed explanation about every classes and functions.


## How to test and run the code
- run_test.sh : run testcase
- run_pre_create.sh : run script that process pre created tweets in ./tweet_input/pre_create_tweets.txt
- run_realtime.sh : run script that process real time tweets 

**Prerequiste**   
To run any program, you need some general python libraries, like json, sys, datetime.
