from scipy.sparse import lil_matrix
import pickle

def naive():
  return

def construct_matrix():
  A = lil_matrix((43873, 11537))
  f1 = open('data/yelp_training_set/users_inverse.pickle', 'r')
  f2 = open('data/yelp_training_set/businesses_inverse.pickle', 'r')
  f3 = open('data/yelp_training_set/reviews.pickle', 'r')
  f4 = open('data/yelp_training_set/user_item_mat.pickle', 'w')
  users_inv = pickle.load(f1)
  busi_inv = pickle.load(f2)
  rev = pickle.load(f3)
  f1.close()
  f2.close()
  f3.close()
  revs = rev.keys()
  ctr = 0
  for r in revs:
    print 'Review {0}'.format(ctr)
    l = rev[r]
    usr_idx = users_inv[l[0]]
    bus_idx = busi_inv[l[1]]
    rating = l[2]
    A[usr_idx, bus_idx] = rating
    ctr += 1
  pickle.dump(A, f4)
  f4.close()
  return A

def get_user_item_matrix():
  print 'Building..'
  return construct_matrix()

def main():
  return

if __name__ == '__main__':
  main()
