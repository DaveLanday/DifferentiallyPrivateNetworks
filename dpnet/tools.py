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
    n2check = [(k, abs(v-b)) for k,v in g.degree() if v > b]
    for node in n2check:
        e = list(g_.edges(node[0]))
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
    delta = 1 / len(nodes)

    # Set beta:
    beta = epsilon / (2 * np.log(2 / delta))

    # Compute smooth sensitivity:
    r = [np.exp(-beta * i) * ls_at_distance(g, upper, i) for i in range(0,k)]
    S = np.max(r)

    sensitivity = 2*S

    return sensitivity
