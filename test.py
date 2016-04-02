import sys
from datetime import datetime
from average_degree import *

get_avgdegree = AvgDegree(sys.path[0]+'\\tweet_input\\tweets1.txt',sys.path[0]+'\\tweet_output\\output1.txt')
start_time = datetime.now()
count = get_avgdegree.output_avg_degree()
print "Finished! There are " + str(count) + ' tweets processed '+ 'and the total running time is ' + str((datetime.now() - start_time).total_seconds())+'s'
