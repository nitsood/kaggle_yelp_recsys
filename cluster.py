import numpy as np
from sklearn import metrics
from scipy.sparse import *
from sklearn import cluster
from collections import defaultdict
import pickle
import sys
import MySQLdb
from namespace import no_use2

import recommender

cpick = defaultdict(set)
centers = defaultdict(no_use2)

def cluster_items(matrix1):
  f = open('data/yelp_training_set/cluster_centers.pickle', 'w')
  #inp = pickle.load(f)
  #reverse = defaultdict(int)
  #ctr = 0
  #for i in inp.keys():
  #  li = inp[i]
  #  lj = []
  #  for l in genres:
  #    lj.append(li[l])
  #  matrix1.append(lj)
    #reverse[ctr] = i
  #  ctr += 1
  #f.close()
  #distmat = np.array([row for row in matrix1]).astype(np.float)
  N = 50
  #a = np.zeros(shape=(N, N))
  #for i in xrange(0, 50):
  #  empty = [0.0]*50
  #  empty[i] = 1.0
  #  a[i] = empty
  k_means = cluster.KMeans(n_clusters=N, max_iter=50, init='k-means++', verbose=1)
  k_means.fit(matrix1)
  k_means_labels = k_means.labels_
  k_means_centers = k_means.cluster_centers_
  #print 'LABELS==='
  #print k_means_labels
  #print
  print 'CENTERS==='
  print k_means_centers
  pickle.dump(k_means_centers, f)
  f.close()
  print
  print 'REPORT==='
  print k_means.inertia_
  """stats = defaultdict(int)
  clustered = defaultdict(set)
  ctr = 0
  for label in k_means_labels:
    stats[label] += 1
    clustered[label].add(ctr)
    ctr += 1
  for c in clustered.keys():
    print 'Label {0} Results--'.format(c)
    members = clustered[c]
    for m in members:
      tags = get_tags(reverse[m])
      print '{0}-> {1}'.format(reverse[m], tags)
    print
  for label in sorted(stats.keys()):
    print 'Label {0}: {1}'.format(label, stats[label])
  print
  print 'CENTER REPORT==='
  labeled_dict = defaultdict()
  for cent in xrange(0, len(k_means_centers)):
    val, dim = max((val, dim) for (dim, val) in enumerate(k_means_centers[cent]))
    gen = genres[dim]
    labeled_dict[cent] = gen
    for d in xrange(0, len(genres)):
      centers[gen][genres[d]] = k_means_centers[cent][d]
    print 'Center {0} is closest to dimension {1}'.format(cent, dim)
  f = open('clusters2.pickle', 'wb')
  for c in clustered.keys():
    gen = labeled_dict[c]
    members = clustered[c]
    for m in members:
      cpick[gen].add(reverse[m])
  pickle.dump(cpick, f)
  f.close()"""
  return

def naive_cluster(matrix):
  clusters = defaultdict(int)
  for mat in matrix:
    dim = find_max(mat)
    clusters[dim] += 1
  for k, v in sorted(clusters.items(), key=lambda v: v[0]):
    print k, v
  return

def main():
  cluster_items(recommender.get_user_item_matrix())

if __name__ == '__main__':
  main()
