#!/usr/bin/env python
# -*-coding: utf-8 -*-
 
#mechanisms.py
#Dave Landay
#LAST UPDATED: 11-30-2019

import numpy as np

def laplace_mech(query, epsilon, sensitivity):
    """
        The Laplace Mechanism
    """
    return query + np.random.laplace(loc=0, scale=sensitivity/epsilon)
