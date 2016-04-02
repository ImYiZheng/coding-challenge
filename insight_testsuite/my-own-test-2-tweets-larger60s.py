import sys
from datetime import datetime
from src.average_degree import *

get_avgdegree = AvgDegree(sys.path[0]+'\\tests\\my-own-test-2-tweets-larger60s\\tweet_input\\tweets.txt',sys.path[0]+'\\tests\\my-own-test-2-tweets-larger60s\\tweet_output\\output.txt')
start_time = datetime.now()
count = get_avgdegree.output_avg_degree()
print "Finished! There are " + str(count) + ' tweets processed '+ 'and the total running time is ' + str((datetime.now() - start_time).total_seconds())+'s'
