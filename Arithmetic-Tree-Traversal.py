
import sys

#==================================
# H E L P E R  F U N C T I O N S
#==================================


# Unoptimised File Processing (for testing)
#------------------------------------------
def file_reader():
    data_list = []
    for line in sys.stdin:
        data_list += [line]
    return data_list

def create_digraphs(data=[]):
    # returns a list of digraph objects
    if data == []:
        data = file_reader()
    digraph_list = []
    pred_arr = []
    value_arr = []
    current_index = 0
    counter = 0

    while (current_index <= len(data)):
        if (counter == 2):
            digraph_list += [Digraph(pred_arr, value_arr)]
            counter = 0
            if current_index == len(data):
                current_index += 1
        elif (counter == 0):
            pred_arr = data[current_index].split(",")
            counter += 1
            current_index += 1
        elif (counter == 1):
            value_arr = data[current_index].split(",")
            counter += 1
            current_index += 1

    return digraph_list

#==========================================
# Q U E S T I O N  F U N C T I O N S
#==========================================

def question_one(data=[]):
    if data == []:
        counter = 0
        pred_arr = []
        value_arr = []
        value_str = ""
        for line in sys.stdin:
            if (counter == 2):
                digraph = Digraph(pred_arr, value_arr)
                value_str += str(digraph.calculate_tree()) + "\n"
                pred_arr = line.split(",")
                counter = 1
            elif (counter == 0):
                pred_arr = line.split(",")
                counter += 1
            elif (counter == 1):
                value_arr = line.split(",")
                counter += 1
        digraph = Digraph(pred_arr, value_arr)
        value_str += str(digraph.calculate_tree()) + "\n"
    else:
        counter = 0
        pred_arr = []
        value_arr = []
        value_str = ""
        for line in data:
            if (counter == 2):
                digraph = Digraph(pred_arr, value_arr)
                value_str += str(digraph.calculate_tree()) + "\n"
                pred_arr = line.split(",")
                counter = 1
            elif (counter == 0):
                pred_arr = line.split(",")
                counter += 1
            elif (counter == 1):
                value_arr = line.split(",")
                counter += 1
        digraph = Digraph(pred_arr, value_arr)
        value_str += str(digraph.calculate_tree()) + "\n"
    print(value_str)

def question_one_optimised(data=[]):
    if data == []:
        counter = 0
        pred_arr = []
        value_arr = []
        value_str = ""
        for line in sys.stdin:
            if (counter == 2):
                digraph = [pred_arr, value_arr]
                value_str += str(calculate_tree_external(digraph)) + "\n"
                pred_arr = line.strip().split(",")
                counter = 1
            elif (counter == 0):
                pred_arr = line.strip().split(",")
                counter += 1
            elif (counter == 1):
                value_arr = line.strip().split(",")
                counter += 1
        digraph = [pred_arr, value_arr]
        value_str += str(calculate_tree_external(digraph)) + "\n"
    else:
        counter = 0
        pred_arr = []
        value_arr = []
        value_str = ""
        for line in data:
            if (counter == 2):
                digraph = [pred_arr, value_arr]
                value_str += str(calculate_tree_external(digraph)) + "\n"
                pred_arr = line.split(",")
                counter = 1
            elif (counter == 0):
                pred_arr = line.split(",")
                counter += 1
            elif (counter == 1):
                value_arr = line.split(",")
                counter += 1
        digraph = [pred_arr, value_arr]
        value_str += str(calculate_tree_external(digraph)) + "\n"
    print(value_str)

def calculate_tree_external(digraph):
    pred_arr = digraph[0]
    value_arr = digraph[1]
    root = pred_arr.index("-1")
    return evaluate_subtree_external(root, pred_arr, value_arr)

def evaluate_subtree_external(node, pred_arr, value_arr):
    if node > len(pred_arr):
        return 0
    operator = value_arr[node]
    if operator == "*":
        sum = 1
    else:
        sum = 0
    for i in range(len(pred_arr)):
        if pred_arr[i] == str(node):
            child = i
            if value_arr[child] in ["*", "+"]:
                if operator == "*":
                    sum *= evaluate_subtree_external(child, pred_arr, value_arr)
                elif (operator == "+"):
                    sum += evaluate_subtree_external(child, pred_arr, value_arr)
                else:
                    sum = 1
            else:
                if operator == "*":
                    sum *= int(value_arr[child])
                else:
                    sum += int(value_arr[child])
    return sum

def question_one_dict(data=[]):
    if data == []:
        counter = 0
        pred_arr = []
        value_arr = []
        value_str = ""
        for line in sys.stdin:
            if (counter == 2):
                digraph = [pred_arr, value_arr]
                value_str += str(calculate_tree_dict(digraph)) + "\n"
                pred_arr = line.strip().split(",")
                counter = 1
            elif (counter == 0):
                pred_arr = line.strip().split(",")
                counter += 1
            elif (counter == 1):
                value_arr = line.strip().split(",")
                counter += 1
        digraph = [pred_arr, value_arr]
        value_str += str(calculate_tree_dict(digraph)) + "\n"
    else:
        counter = 0
        pred_arr = []
        value_arr = []
        value_str = ""
        for line in data:
            if (counter == 2):
                digraph = [pred_arr, value_arr]
                value_str += str(calculate_tree_dict(digraph)) + "\n"
                pred_arr = line.split(",")
                counter = 1
            elif (counter == 0):
                pred_arr = line.split(",")
                counter += 1
            elif (counter == 1):
                value_arr = line.split(",")
                counter += 1
        digraph = [pred_arr, value_arr]
        value_str += str(calculate_tree_dict(digraph)) + "\n"
    print(value_str)

def calculate_tree_dict(digraph):
    pred_arr = digraph[0]
    value_arr = digraph[1]
    pred_dict = {}
    for i in range(len(pred_arr)):
        if pred_arr[i] == "-1":
            root = i
        pred_dict[i] = []
        if value_arr[i] in ["*", "+"]:
            for x in range(len(pred_arr)):
                if pred_arr[x] == str(i):
                    pred_dict[i] += [x]
    return evaluate_subtree_dict(root, pred_dict, value_arr)

def evaluate_subtree_dict(node, pred_dict, value_arr):
    if node > len(value_arr):
        return 0
    operator = value_arr[node]
    if operator == "*":
        sum = 1
    else:
        sum = 0
    children = pred_dict[node]
    for child in children:
        if value_arr[child] == "*" or value_arr[child] == "+":
            if operator == "*":
                sum *= evaluate_subtree_dict(child, pred_dict, value_arr)
            elif (operator == "+"):
                sum += evaluate_subtree_dict(child, pred_dict, value_arr)
            else:
                sum = 1
        else:
            if operator == "*":
                sum *= int(value_arr[child])
            else:
                sum += int(value_arr[child])
    return sum

#==========================================
# N O D E  &  D I G R A P H  C L A S S E S
#==========================================

class Node:

    def __init__(self, location, value):
        self.location = location
        self.linked_indexes = []
        self.colour = "W"
        self.predecessor = -1;
        self.seen = 0
        self.done = -1
        self.depth = None
        self.source = None
        try:
            self.value = int(value)
        except:
            self.value = None

class Digraph:

    def __init__(self, pred_arr, value_arr):
        #Fundamental Attributes
        self.order = len(pred_arr)
        self.nodes = []
        self.global_time = 0
        self.value = 0
        self.forward_arc = "\n"
        self.cross_arc = "\n"
        self.pred_arr = pred_arr
        self.value_arr = value_arr
        self.root = pred_arr.index("-1")
        #Node Initialisation
        self.child_arr = [[] for x in range(self.order)]
        for i in range(len(pred_arr)):
            self.nodes += [Node(i, value_arr[i])]
            parent = int(pred_arr[i])
            if parent != -1:
                self.child_arr[parent] += [i]


    def evaluate_subtree(self, node):
        if node > len(self.nodes):
            return 0
        operator = self.value_arr[node]
        if self.value_arr[node] == "*":
            sum = 1
        else:
            sum = 0
        for child in self.child_arr[node]:
            current_node = self.nodes[child]
            if self.value_arr[child] in ["*", "+"]:
                if (operator == "*"):
                    sum *= self.evaluate_subtree(child)
                elif (operator == "+"):
                    sum += self.evaluate_subtree(child)
            else:
                if operator == "*":
                    sum *= current_node.value
                else:
                    sum += current_node.value
        return sum

    def evaluate_subtree_V2(self, node):
        if node > self.order:
            return 0
        operator = self.value_arr[node]
        if self.value_arr[node] == "*":
            sum = 1
        else:
            sum = 0
        for i in range(len(self.pred_arr)):
            if self.pred_arr[i] == str(node):
                child = i
                if self.value_arr[child] in ["*", "+"]:
                    if operator == "*":
                        sum *= self.evaluate_subtree_V2(child)
                    elif (operator == "+"):
                        sum += self.evaluate_subtree_V2(child)
                    else:
                        sum = 1
                else:
                    if operator == "*":
                        sum *= int(self.value_arr[child])
                    else:
                        sum += int(self.value_arr[child])
        return sum

    def calculate_tree(self):
        return self.evaluate_subtree(self.root)


#======================================
# H E L P E R  C L A S S E S 
#======================================

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)                
    def pop(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)        
    def __str__(self):
        return str(self.items)[:-1] + ' <-'
    def clear(self):
        self.items = []  

class Queue:
    def __init__(self):
        self.__items = []
    def is_empty(self):
        return self.__items == []
    def enqueue(self, item):
        self.__items.insert(0,item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Error: The queue is empty!')
        return self.__items.pop() 
    def size(self):
        return len(self.__items)
    def peek(self):
        if self.is_empty():
            raise IndexError('Error: The queue is empty!')
        return self.__items[len(self.__items)-1]
    def __str__(self):
        return '-> |' + str(self.__items)[1:-1] + '| ->'

#==============================
# M A I N ( )  C O D E
#==============================

data = ["-1,0,0,0,1,1", "+,*,2,3,0,7", "2,0,-1,0", "+,3,*,3"]
data2 = ["3,8,9,4,-1,1,1,4,3,7,7,16,9,16,1,9,8", "-1,*,1,*,*,3,5,*,*,*,-2,5,2,-4,4,-5,+", "-1,0,0", "+,-2,-1", "3,3,0,-1", "*,-3,-4,*", "7,0,10,12,9,12,7,4,10,-1,6,10,6,0,7", "*,2,-2,-1,+,-3,*,*,-5,*,*,-3,*,2,5", "-1,0,0,0", "*,1,-4,-3"]
data3 = ["3,8,9,4,-1,1,1,4,3,7,7,16,9,16,1,9,8", "-1,*,1,*,*,3,5,*,*,*,-2,5,2,-4,4,-5,+"]
question_one(data2)


#=============================
# D I S C A R D E D  C O D E
#=============================