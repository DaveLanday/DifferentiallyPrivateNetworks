#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#tools.py
#Dave Landay
#LAST UPDATED: 12-02-2019

import numpy as np
from copy import deepcopy
from . import tools

def clip(arr, l=None, u=None):
    return np.clip(arr, l, u)

def clipGraph(g, b):
    """
        Clips the edges that have a degree which exceeds an upper bound

        param: g (Graph): a networkX Graph() object
        param: b (int): clipping parameter, upper bound

        returns: g' (Graph): a clipped network
    """
    g_ = deepcopy(g)
    n2check = [(k, abs(v-b)) for k,v in g_.degree() if v > b]
    for node in n2check:
        e = list(g.edges(node[0]))
        edges = np.random.choice(list(range(len(e))), size=node[1], replace=False)
        e2remove = [e[i] for i in edges]
        g_.remove_edges_from(e2remove)
    return g_

def ls_at_distance(g, upper, k):
    """
        Calculates local sensitivity at a distance k.
        
        param: g (Graph): a networkX Graph() object
        param: upper (int): a proposed upper bound on sensitivity
        param: k (int): step distance away from dataset

        returns: np.abs(upper/(len(g.nodes) - k + 1)
    """
    return np.abs(upper/(len(g.nodes) - k + 1))

def smoothSensitivity(g, upper, k, epsilon):
    """
        Calculates smooth sensitivity of upperbound on graph g

        param: g (Graph): a networkX Graph() object
        param: upper (int): a proposed upper bound on sensitivity
        param: k (int): step distance away from dataset
        param: epsilon (float): privacy budget
    """
    # Get the number of nodes:
    nodes = g.nodes()

    # Define delta:
    delta = 1 / len(nodes)**2

    # Set beta:
    beta = epsilon / (2 * np.log(2 / delta))

    # Compute smooth sensitivity:
    r = [np.exp(-beta * i) * ls_at_distance(g, upper, i) for i in range(0,k)]
    S = np.max(r)

    sensitivity = 2*S

    return sensitivity

def create_dict(n, e):
    d = {}
    count = 0
    tmp = 0

    for i in range(len(n)):
        d[i] = 0

    for i in e:
        if i[0] != tmp:
            d[tmp] = count
            tmp = i[0]
            count = 1
        else:
            count += 1

    return d

def edge_mean(d):
    d_sum = 0
    for x, y in d.items():
        d_sum += y
    return d_sum/len(d)

def pct_error(predicted, truth):
    """
        Calculates the error in a differentially private query and the true query answer

        param: predicted (float): the predicted true answer
        param: truth (int): the ground truth
        
        returns: err (float): the percent of the true value the predicted value is
    """
    return np.abs(predicted-truth) / truth * 100
