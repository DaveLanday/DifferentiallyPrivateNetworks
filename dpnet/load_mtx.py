#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#load_mtx.py
#Dave Landay
#LAST UPDATED: 11-29-2019


import numpy as np
import networkx as nx

def load_mtx(path, create_using=None):
    """
    LOAD_MTX: loads an adjacency list stored in .mtx format

    param: path (string/pathlike): path to the .mtx file containing the adjacency list
    param: create_using (container): specifies what graph type should be used nx.Graph() or nx.DiGraph()

    returns: G (nx.Graph): a networkX graph object 
    """
    
    G = nx.read_edgelist(path, create_using=create_using)
    return G
