import sys
from datetime import datetime
from average_degree import *

get_avgdegree = AvgDegree(sys.path[0]+'\\tests\\my-own-test-2-tweets-larger60s\\tweet_input\\tweets.txt',sys.path[0]+'\\tests\\my-own-test-2-tweets-larger60s\\tweet_output\\output.txt')
start_time = datetime.now()
count_total_tweets, count_valid_tweets = get_avgdegree.output_avg_degree()
print "Finished!"
print "There are "+ str(count_total_tweets) + " tweets in the input file"
print str(count_valid_tweets) + ' tweets are processed '
print 'the total running time is ' + str((datetime.now() - start_time).total_seconds())+'s'
