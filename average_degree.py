import json
from get_tweet_info import *
from get_hashtag_graph import *

class AvgDegree:
  """ Generate average degree, with information from the pre_created tweet file.
  As tweets are pre created, I write parsed tweets into ft1 when I've parsed 3000 tweets. 
  In this case, I can write data sequentially. 

  The experiment data is about 8 seconds to parse 18729 tweets.
  """

  def __init__(self, input_file_name, output_file_name):
    self.input_file_name = input_file_name
    self.output_file_name = output_file_name
    self.tweet_info = GetInfo()
    self.edges = HashtagGraphEdges()
    self.nodes = HashtagGraphNodes()

  # Process and update a new tweet 
  # Store edges to self.edges, store nodes and edges to self.nodes
  # Return None, if tweet not in correct JSON format
  def add_one_tweet(self, tweet):
    tweet_json = json.loads(tweet)
    raw_hashtags, raw_datetime,  = self.tweet_info.get_raw_info(tweet_json)
    if raw_hashtags != None:
      hashtag_pair_list = self.tweet_info.get_hashtag_pair_list(raw_hashtags)
      datetime = self.tweet_info.get_datetime(raw_datetime)
      remove_edges = self.edges.get_edges(hashtag_pair_list, datetime)
      self.nodes.get_nodes(hashtag_pair_list)
      self.nodes.remove_nodes(remove_edges)
      return hashtag_pair_list
    return None, None
  
  # Recevie each tweet from input tweet file.
  # Update the Twitter hashtag graph each time receving a new tweet and hence, output the average degree of the graph
  # Graph only consists of tweets that arrived in the last 60 seconds as compared to the maximum timestamp that has been processed
  def output_avg_degree(self):
    output = open(self.output_file_name, 'w')
    is_start = False   
    count = 0
    with open(self.input_file_name) as tweets:
      for tweet in tweets:
        count += 1
        hashtag_pair_list = self.add_one_tweet(tweet)
        if hashtag_pair_list != None: 
          if is_start == False:
            is_start = True
            print 'Start calculating the average degree of a vertex in a Twitter hashtag graph for the last 60 seconds, and updating this each time a new tweet appears'
          if len(self.nodes.nodes) == 0:
            output.write(str(0) + '\n')
          else:
            output.write(format(2.0 * len(self.edges.edges) / len(self.nodes.nodes), '.3f') + '\n')
    tweets.close() 
    output.close()
    return count
