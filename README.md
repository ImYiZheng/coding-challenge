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

1. HashtagGraphEdges: To get edges of hashtags in latest 60s and remove the timeout edges. 
   - The double linked list node contains the hashtag_pair, the datetime of one tweet and the two pointers, Next and Previous. The double linked list is used for the structure of hashtag graph. For example, Whenever I receive one tweet, I will add new nodes and remove timeout nodes, which are outside the latest 60 seconds window in the linked list.     
   - Use a dictionary to store the hashtag graph. The key of the dictionary is a hashtag_pair (e.g. ('#Spark', '#Apache')) and the values is the double linked list node. The number of the keys is the number of edges so the total degrees equals to 2*the number of edges

2. HashtagGraphNodes: To get total nodes in the hashtag graph. 
   - Store the nodes in hashtag graph in a dictionary.   
   - Whenever I update the graph, I will add new nodes and related neighbours and remove timeout nodes and related neighbours.

For detail information, please see the code files.


## How to test and run the code
- run_test.sh : run testcase
- run_pre_create.sh : run script that process pre created tweets in ./tweet_input/pre_create_tweets.txt
- run_realtime.sh : run script that process real time tweets 

**Prerequiste**   
To run any program, you need some general python libraries, like json, sys, datetime.
