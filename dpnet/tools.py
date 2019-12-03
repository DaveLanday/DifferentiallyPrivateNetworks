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
        param: b (upper): clipping parameter, upper bound

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