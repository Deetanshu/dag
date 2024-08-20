#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:01:52 2023

@author: Deeptanshupaul
"""

import pytest
from node import Node

def test_node_constructor():
    given_name = 'Parent'
    node = Node(given_name)
    assert node.name == given_name

def test_node_with_no_name():
    with pytest.raises(TypeError):
        node = Node()
        
def test_node_add_children():
    parent_node = Node('Parent')
    child_node = Node('Child')
    parent_node.add_child(child_node)
    assert child_node in parent_node.children

def test_add_two_children():
    parent_node = Node('Parent')
    child_node = Node('Child')
    child_node_2 = Node('Child2')
    parent_node.add_child(child_node)
    parent_node.add_child(child_node_2)
    assert parent_node.children =={child_node, child_node_2}
    
def test_add_same_child_twice():
    parent_node = Node('Parent')
    child_node = Node('Child')
    parent_node.add_child(child_node)
    parent_node.add_child(child_node)
    assert len(parent_node.children) == 1

def test_immutable_children():
    parent_node = Node('Parent')
    child_node = Node('Child')
    cuckoo_node = Node('Cuckoo')
    parent_node.add_child(child_node)
    children=parent_node.get_children()
    children.add(cuckoo_node)
    assert cuckoo_node not in parent_node.get_children()

def test_get_descendants():
    parent_node = Node("Parent")
    child_node = Node("Child")
    grandchild_node = Node("Grandchild")
    parent_node.add_child(child_node)
    child_node.add_child(grandchild_node)
    descendants = parent_node.get_descendants()
    assert len(descendants) == 2 

def test_multiple_branch_descendants():
    parent_node = Node("Parent")
    child_node = Node("Child")
    child_node_2 = Node("Child2")
    grandchild_node = Node("Grandchild")
    grandchild_node_2 = Node("Grandchild2")
    parent_node.add_child(child_node)
    parent_node.add_child(child_node_2)
    child_node.add_child(grandchild_node)
    child_node_2.add_child(grandchild_node_2)
    descendants = parent_node.get_descendants()
    assert len(descendants) == 4

def test_acyclic_exception():
    parent_node = Node("Parent")
    child_node = Node("Child")
    error = None
    parent_node.add_child(child_node)
    with pytest.raises(Exception, match = "Acyclic property has been violated") as exception:        
        child_node.add_child(parent_node)
