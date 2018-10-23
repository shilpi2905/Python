# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 23:16:58 2018

@author: Shilpi

Task 
The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. You are given a pointer, , pointing to the root of a binary search tree. Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.

Input Format

The locked stub code in your editor reads the following inputs and assembles them into a binary search tree: 
The first line contains an integer, , denoting the number of nodes in the tree. 
Each of the  subsequent lines contains an integer, , denoting the value of an element that must be added to the BST.

Output Format

The locked stub code in your editor will print the integer returned by your getHeight function denoting the height of the BST.

Sample Input

7
3
5
2
1
4
6
7
Sample Output

3

"""
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
       # print("inside insert::", data, root)
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
               # print("inside if::",root.data, root.right,root.left)
                cur=self.insert(root.left,data)
                root.left=cur
            else:
              #  print("inside else::",root.data,root.right,root.left)
                cur=self.insert(root.right,data)
                root.right=cur
       # print("inside after if, else::",root.data, root.right,root.left)
        return root
    
    def getHeight(self,root):
        if root == None:
            return -1
        else:
            return 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        
        
        
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
    #print("root::",root.data, root.left, root.right)
height=myTree.getHeight(root)
print(height)
