#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:17:08 2023

@author: deeptanshupaul
"""


class Node():
    def __init__(self, name):
        self.name = name
        self.children = set()

    def add_child(self, node):
        self.children.add(node) 
    
    def get_children(self):
        return self.children.copy()
    
    def get_descendants(self):
        descendants = list(self.children.copy())
        for child in self.children:
            descendants.append(child.get_descendants())
        return descendants