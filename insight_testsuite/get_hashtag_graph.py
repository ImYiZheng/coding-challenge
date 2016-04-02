from datetime import *

class HashtagGraphEdges:
  """ Double linked list method is used to build the Twitter hashtag graph. The double linked list stands for the structure of the hashtags according. 
  The keys of dictionary are the edges of two hastags(hashtage_pair in hashtage_pair_list) and the coressponding values are double linked nodes(storing the hashtage_pair and datetime)
  This data structure aims to get the total edges og tweets in latest 60s, the degrees of nodes in Twitter hashtag graph is 2*the number of edges.
  """
  # Double Linked List DuLNode
  class DuLNode:
    
    def __init__(self, hashtag_pair, datetime):
      self.hashtag_pair = hashtag_pair  # hashtage_pair
      self.datetime = datetime  # datetime
      self.prev = None
      self.next = None
  
  # Double linked list initialization
  # Create the head and tail nodes of the double linked list
  # Connect the head and tail node
  def __init__(self):
    self.edges = {}   # each hashtag_pair is an edge, set the hashtag_pair as the key of the dictionary 
    self.head = self.DuLNode(None, None)    # head and tail nodes are void
    self.tail = self.DuLNode(None, None)    
    self.head.next = self.tail
    self.tail.next = self.head
    
  # Set a list of hashtag_pair to the data structure
  # Return a list of timeout hashtag_pair
  def get_edges(self, hashtag_pair_list, time):
    for hashtag_pair in hashtag_pair_list:
      self.add_node(hashtag_pair, time)
    return self.remove_edges(time)
  
  # Add every new DuLNode to the double linked list 
  # Each DuLNode has value <hashtag_pair, datetime>, use hashtag_pair as the key, and the DuLNode as the value of the key  
  def add_node(self, hashtag_pair, datetime):
    if None != self.check_node(hashtag_pair):
      self.edges.get(hashtag_pair).datetime = datetime                     
    else:
      current = self.DuLNode(hashtag_pair, datetime)
      if 0 == len(self.edges):
        self.head.next = current
        current.prev = self.head
        current.next = self.tail
        self.tail.prev = current
      else:
        self.move_node_to_tail(current)
      self.edges[hashtag_pair] = current

  # Check whether the new DuLNode is in the double linked list
  # If yes, move the node to the tail of double linked list
  def check_node(self, hashtag_pair):
    if hashtag_pair not in self.edges:
      return None
    else:
      current = self.edges[hashtag_pair]                           
      current.prev.next = current.next
      current.next.prev = current.prev
      self.move_node_to_tail(current)
      return current.datetime

  # Move the current DuLNode to tail of the double linked list
  def move_node_to_tail(self, current):
    self.tail.prev.next = current
    current.prev = self.tail.prev
    current.next = self.tail
    self.tail.prev = current

  # Remove timeout hashtag_pair in the data structure
  def remove_edges(self,current_time):
    remove_edges = []
    timestamp = current_time - timedelta(seconds = 60)
    current = self.head.next
    while (current != self.tail and current.datetime < timestamp):
      self.head.next = current.next
      current.next.prev = self.head
      remove_edges.append(current.hashtag_pair)
      del self.edges[current.hashtag_pair]
      current = current.next
    return remove_edges



class HashtagGraphNodes:
  """
  This data structure aims to get the total hashtags(nodes) in the in Twitter hashtag graph in latest 60s. 
  """
  def __init__(self):
    self.nodes = {}   # Hashtag(node) in the Hashtag Graph

  # Store hashtag pairs in the data structure
  # Each hashtag is the key of dictionary and the value is another hashtage connnected with it
  def get_nodes(self, hashtag_pair_list):
    for hashtag_pair in hashtag_pair_list:
      # first hashtag of hashtag_pair
      if hashtag_pair[0] not in self.nodes:
        self.nodes[hashtag_pair[0]] = set([hashtag_pair[1]])  # first edge to the hashtag
      else:
        self.nodes[hashtag_pair[0]].add(hashtag_pair[1])    # other edge to the hashtag
      # second hashtag of hashtag_pair
      if hashtag_pair[1] not in self.nodes:
        self.nodes[hashtag_pair[1]] = set([hashtag_pair[0]])
      else:
        self.nodes[hashtag_pair[1]].add(hashtag_pair[0])
        
  # Remove hashtag pairs in the data structure
  def remove_nodes(self, remove_edges):
    for edge in remove_edges:
      self.nodes[edge[0]].remove(edge[1])
      if 0 == len(self.nodes[edge[0]]): 
        del self.nodes[edge[0]]   # when the hashtag(node) has no edge, remove this hashtage(node) in Hashtag Graph
      self.nodes[edge[1]].remove(edge[0])
      if 0 == len(self.nodes[edge[1]]): 
        del self.nodes[edge[1]]
