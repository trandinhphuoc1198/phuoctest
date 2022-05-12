from gettext import find
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    #Show tree in terminal simply
def display(node,level=0,space='\t'):
    if node is None:
        print(space*level,'None')
        return
    display(node.left,level+1,space)
    print(space*level,node.data)
    display(node.right,level+1,space)
#Using common way
def find_max(node,maximun):
    if node is None:
        return maximun
    maximun=find_max(node.left,maximun)
    maximun=find_max(node.right,maximun)
    if node.data>maximun:
        maximun=node.data
    return maximun
#Using In-Order Traversal
def find_max_2(node,previous=None,max=None):
    global prev
    global maxx
    if node is None:
        return
    if max is None:
        maxx=node.data
    if previous and maxx and maxx<node.data:
        maxx=node.data
    prev=node.data
    find_max_2(node.left,prev,maxx)
    find_max_2(node.right,prev,maxx)
    return maxx
def insert_node(node,value):
    if node is None:
        node=Node(value)
    elif value>node.data:
        node.right=insert_node(node.right,value)
    else:
        node.left=insert_node(node.left,value)
    return node
#List a binary tree 
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [node.data] + list_all(node.right)
#Build a binary tree from a sorted list
def BST_from_sortedList(list,start,end):
    mid=(start+end)//2
    if start>end:
        return None
    node=Node(list[mid])
    node.left=BST_from_sortedList(list,start,mid-1)
    node.right=BST_from_sortedList(list,mid+1,end)
    return node
#Find if there is value in BST
def find_node(node,value):
    if node is None:
        return None
    if node.data==value:
        return node
    elif node.data>value:
        node=find_node(node.left,value)
    else:
        node=find_node(node.right,value)
    return node

#Build a binary tree from a tuple
def parse_tuple(tupleTarget,node=None):
        if isinstance(tupleTarget,tuple):
            node=Node(tupleTarget[1])
            node.left=parse_tuple(tupleTarget[0],node.left)
            node.right=parse_tuple(tupleTarget[2],node.right)
            return node
        else:
            return Node(tupleTarget)

#Check if the tree is balanced
def check_balance(node,height=0):
    if node is None:
        return height,True
    height_left,is_balance_l=check_balance(node.left,height+1)
    height_right,is_balance_r=check_balance(node.right,height+1)
    is_balance=is_balance_r and is_balance_l and abs(height_right-height_left)<=1
    return max(height_left,height_right),is_balance
#Count height of the given BST
def count_height(node,height=0):
    if node is None:
        return height
    left=count_height(node.left,height+1)
    right=count_height(node.right,height+1)
    return max(left,right)

#Self-balance a tree 

sortedList=[0,1,2,3,4,5,6,9]
BSTfromlist=BST_from_sortedList(sortedList,0,len(sortedList)-1)

display(BSTfromlist)
