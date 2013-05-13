import json
import re
import pickle
from collections import defaultdict


users = defaultdict() # int -> string
users_inv = defaultdict(int) # string -> int
busi = defaultdict() # int -> string
busi_inv = defaultdict(int) # string -> int
reviews = defaultdict(list) # string -> [string, string]
ctr = 0


"""tokenize text and convert to lower case"""
def tokenize(text):
  tok = re.split(r'\W+', text, flags=re.UNICODE)
  lower_tok = []
  for t in tok:
    if(t is None or t == ''):
      continue
    lower_tok.append(t.lower())
  return lower_tok


def parse_users(lines):
  global ctr
  for line in lines:
    js = json.loads(line)
    usid = js['user_id']
    users[ctr] = usid
    users_inv[usid] = ctr
    ctr += 1
  f = open('data/yelp_training_set/users.pickle', 'w')
  pickle.dump(users, f)
  f.close()
  f = open('data/yelp_training_set/users_inverse.pickle', 'w')
  pickle.dump(users_inv, f)
  f.close()
  ctr = 0
  return


def parse_businesses(lines):
  global ctr
  for line in lines:
    js = json.loads(line)
    busid = js['business_id']
    busi[ctr] = busid
    busi_inv[busid] = ctr
    ctr += 1
  f = open('data/yelp_training_set/businesses.pickle', 'w')
  pickle.dump(busi, f)
  f.close()
  f = open('data/yelp_training_set/businesses_inverse.pickle', 'w')
  pickle.dump(busi_inv, f)
  f.close()
  return


def parse_reviews(lines):
  for line in lines:
    js = json.loads(line)
    revid = js['review_id']
    reviews[revid] = [js['user_id'], js['business_id'], int(js['stars'])]
  f = open('data/yelp_training_set/reviews.pickle', 'w')
  pickle.dump(reviews, f)
  f.close()
  return


def read_file(filename):
  f = open(filename, 'r')
  lines = f.readlines()
  f.close()
  return lines


def main():
  #l = read_file('data/yelp_training_set/yelp_training_set_user.json')
  #parse_users(l)
  #l = read_file('data/yelp_training_set/yelp_training_set_business.json')
  #parse_businesses(l)
  l = read_file('data/yelp_training_set/yelp_training_set_review.json')
  parse_reviews(l)
  return


if __name__ == '__main__':
  main()
