"""
Node class for the doubly linked list
"""
class Node:
    def __init__(self,val = 0, next = None , prev = None):
        # initialize 
        self.val = val
        self.next = next
        self.prev = prev


    def __str__(self):
        return str(self.val)

"""
Linked list class
"""
class Linked_list:
    def __init__(self, head: Node, tail :Node):
        self.head = head
        self.tail = tail


    def __str__(self):
        node = self.head
        string = str(node.val)
        node = node.next
        while(node != None):
            string = string + ", " + str(node.val)
            node = node.next
        return string


    def __len__(self):
        count = 0
        node = self.head
        while (node != None):
            count += 1
            node = node.next
        return count


    def append(self, new_node_value: int):
        node = self.head
        new_node = Node()
        new_node.val = new_node_value
        new_node.next = None
        self.tail = new_node
        while(node.next != None):
            node = node.next
        node.next = new_node
        new_node.prev = node



    def insert(self, new_node_value: int, index: int):
        node = self.head
        new_node = Node()
        new_node.val = new_node_value
        new_node.next = None
        num = index
        if index > self.__len__()-1:
            if index == self.__len__():
                self.append(new_node_value)
                return True
            else:
                print("Index is bigger than the list.")
                return False
        else:
            while num != 0:
                node = node.next
                num -= 1

            node.prev.next = new_node
            new_node.next = node
            new_node.prev = node.prev
            node.prev = new_node
            return True


    def reversed_str(self):
        node = self.tail
        string = str(node.val)
        node = node.prev
        while (node != None):
            string = string + ", " + str(node.val)
            node = node.prev
        return string


    def find_value(self, search_value :int):
        node = self.head
        while node.val != search_value:
            if node.next == None:
                return None
            node = node.next
        if node.val == search_value:
            return node


    def remove(self, removed_val: int):
        node = self.find_value(removed_val)
        if node != None:
            if node.val == self.head.val:
                self.head = self.head.next
                self.head.prev = None
            else:
                node.prev.next = node.next
                node.next .prev = node.prev
            return True
        else:
            return False

    def pop(self):
        node = self.head
        self.remove(self.head.val)
        return node


    def reverse_list(self):
        node = self.head
        while node != None:
            prev = node.next
            node.next = node.prev
            node.prev = prev
            node = node.prev
        node = self.tail
        self.tail = self.head
        self.head = node

    def is_palindrome(self):
        if self.__str__() == self.reversed_str():
            print("It is a Palindrome")
            return True
        else:
            print("It is not a palindrome")
            return False

    def is_also_palindrome(self):
        front = self.head
        back = self.tail
        is_palindrome = True
        while(front != None and back != None):
            if (front.val != back.val):
                is_palindrome = False
                break
            front = front.next
            back = back.prev
        if is_palindrome:
            print("It is a Palindrome")
        else:
            print("It is not a palindrome")

pain = Node()
pain.val = 1
trial = Linked_list(pain, pain)
trial.append(1)
trial.append(1)
trial.append(2)
trial.append(1)
trial.append(1)
trial.append(1)

print(trial)
# trial.reverse_list()
# print(trial)
trial.is_also_palindrome()



