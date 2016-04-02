from datetime import datetime

class GetInfo:
  """ GetInfo extracts 'hashtags' and 'created_at' fields of each tweet, then
      get datetime in datetime format from raw datetime in unicode format,
      get a hashtag pair list from raw hashtags
  """

  # Return the hashtags and created_at fields of each entry in input Tweets
  # Return None if the input Tweets not in correct JSON format
  def get_raw_info(self, raw_tweet):
    try:  
      raw_hashtags = raw_tweet['entities']['hashtags']
      raw_datetime = raw_tweet['created_at']
      return raw_hashtags, raw_datetime
    except Exception as e:
      return None, None

  # Return a hashtag_pair_list from hashtags
  def get_hashtag_pair_list(self, raw_hashtags):
    # store each hashtag in a hashtag_list
    hashtag_list = []
    for num in range(len(raw_hashtags)):
      hashtag_list.append(raw_hashtags[num]['text'])  # check and store hashtag   
    hashtag_list = list(set(hashtag_list))  # remove repeated hastag
    hashtag_list.sort()   # sort the hashtag in accending order 
    
    # return hashtag_pair_list, consisting of every two hashtags in hastag_list as accending order in pair
    # arrange the hashtags in an unifom order
    hashtag_pair_list = []
    for i in range(0, len(hashtag_list)):
      for j in range(i + 1, len(hashtag_list)):
        hashtag_pair_list.append((hashtag_list[i], hashtag_list[j]))
    return hashtag_pair_list  

  # Return datetime from raw datetime in string format
  def get_datetime(self, raw_datetime):
    return datetime.strptime(raw_datetime,'%a %b %d %H:%M:%S +0000 %Y')
    

