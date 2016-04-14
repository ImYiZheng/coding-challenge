Hello, my name is Yi Zheng, Let's get started!
===========================================================
Insight Data Engineering - Coding Challenge  
https://github.com/InsightDataScience/coding-challenge

## Quick test

   - In the tweet_input directory, the input tweets.txt has size 27.3M, including 9999 tweets, 9295 tweets are valid and processed(invalid tweet, e.g. {"limit": {"track":5,"timestamp_ms":"1446218985743"} } will be removed by my tool). This file is from data-gen directory.The corresponding output output.txt is in tweet_output directory.   
   - In insight_testsuite directory, I made two simple tests. You can find the corresponding outputs in the tweet_output directory.

## Directory structure
	├── README.md 
	├── test.py  
	├── average_degree.py  
	├── get_hashtag_graph.py  
	├── get_tweet_info.py
	├── src
	│   └── average_degree.py  
	│   └── get_hashtag_graph.py  
	│   └── get_tweet_info.py
	├── tweet_input
	│   └── tweets.txt
	├── tweet_output
	│   └── output.txt
	└── insight_testsuite
	    ├── my-own-test-2-tweets-larger60s.py  
	    ├── test-2-tweets-all-distinct.py
	    └── tests
	        └── test-2-tweets-all-distinct
	        │   ├── tweet_input
	        │   │   └── tweets.txt
	        │   └── tweet_output
	        │       └── output.txt
	        └── my-own-test-2-tweets-larger60s
	            ├── tweet_input
	            │   └── tweets.txt
	            └── tweet_output
	                └── output.txt

## Development Summary

I write all codes in Python.  

The functions of my tool:

1. Extract the hashtags and created_at fields from the raw JSON tweets that come from a prepared tweets file.
2. Build a Twitter hashtag graph.
3. Calculate the average degree of a vertex in a Twitter hashtag graph for the last 60 seconds, and update this each time a new tweet appears.

## Data Structure and algorithms
Implement the hashtag graph with double linked list.

1. HashtagGraphEdges: To get edges of hashtags in latest 60s and remove the timeout edges. 
   - The double linked list node contains the hashtag_pair, the datetime of one tweet and the two pointers, Next and Previous. The double linked list is used for the structure of hashtag graph. For example, Whenever receiving one tweet, it will add new nodes and remove timeout nodes, which are outside the latest 60 seconds window in the linked list.     
   - Use a dictionary to store the hashtag graph. The key of the dictionary is a hashtag_pair (e.g. ('#Spark', '#Apache')) and the values is the double linked list node. The number of the keys is the number of edges so the total degrees equals to 2*the number of edges

2. HashtagGraphNodes: To get total nodes in the hashtag graph. 
   - Store the nodes in hashtag graph in a dictionary.   
   - Whenever receiving one tweet, it will add new nodes and connected neighbour nodes and remove timeout nodes and connected neighbour nodes.

For detail information, please see the code files.


## How to test and run the code  
In windows, after downloading the zip file and uncompress it, you can run xxx.py directly such as python xxx.py in command line. Then find the ouput.txt in corresponding directory.
- test.py : run test.py directly
- my-own-test-2-tweets-larger60s.py : run my-own-test-2-tweets-larger60s.py directly
- test-2-tweets-all-distinct.py : run test-2-tweets-all-distinct.py directly  
  
or  
run run_test.sh
run run_my-own-test-2-tweets-larger60s.sh
run run_test-2-tweets-all-distinct.sh

**Prerequiste**   
To run any program, you need some general python libraries, like json, sys, datetime.
