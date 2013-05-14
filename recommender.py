from scipy.sparse import lil_matrix
from numpy.random import rand
import pickle

""" naive impl of recommendation """
def naive():
  return

""" construct user-item matrix """
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

""" construct a subset of ratings """
def construct_matrix_small():
  A = lil_matrix((1000, 1000))
  A[0, :100] = rand(100)
  A[1, 100:200] = A[0, :100]
  A.setdiag(rand(1000))
  return A

""" construct a subset of ratings """
def construct_small_matrix():
  U = 1000
  B = 500
  A = lil_matrix((U, B))
  f1 = open('data/yelp_training_set/users_inverse.pickle', 'r')
  f2 = open('data/yelp_training_set/businesses_inverse.pickle', 'r')
  f3 = open('data/yelp_training_set/reviews.pickle', 'r')
  f4 = open('data/yelp_training_set/user_item_mat_small.pickle', 'w')
  users_inv = pickle.load(f1)
  busi_inv = pickle.load(f2)
  rev = pickle.load(f3)
  f1.close()
  f2.close()
  f3.close()
  revs = rev.keys()
  usrs = users_inv.keys()[:U]
  busi = busi_inv.keys()[:B]
  ctr = 0
  nonz = 0
  for r in revs:
    print 'Review {0}'.format(ctr)
    l = rev[r]
    if l[0] in usrs and l[1] in busi:
      try:
        usr_idx = users_inv[l[0]]
        bus_idx = busi_inv[l[1]]
        rating = l[2]
        A[usr_idx, bus_idx] = rating
        nonz += 1
      except IndexError, e:
        print 'Error!'
        pass
    ctr += 1
  pickle.dump(A, f4)
  f4.close()
  print A
  print '------'
  print nonz
  return A

""" method exposed for outside world to get a user-item matrix """
def get_user_item_matrix():
  print 'Building..'
  return construct_matrix()

""" main function """
def main():
  return

if __name__ == '__main__':
  main()
