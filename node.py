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
        if self.acyclic_test(node):
            self.children.add(node)
        else:
            raise Exception("Acyclic property has been violated")

    def get_children(self):
        return self.children.copy()

    def get_descendants(self):
        descendants = set(self.children.copy())
        for child in self.children:
            descendants.update(child.get_descendants())
        return descendants

    def acyclic_test(self, node):
        if self in node.get_descendants():
            return False
        return True