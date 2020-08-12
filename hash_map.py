# Course: CS261 - Data Structures
# Assignment: 5
# Student:Tobi Fanibi
# Description:hashmap object class with linkedlist objects in indexes. Linkedlist provide collision control for calulated indexes from hashes.



# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        clears the hash map. By setting every index to an empty linkedlist
        """
        clear=LinkedList()
        size=self.capacity
        for index in range(0,size):
            self.buckets.set_at_index(index,clear)
            self.size=0


    def get(self, key: str) -> object:
        """
        Returns the value of a key, if not in hashmap returns None
        """
        if self.contains_key(key)==False:
            return None
        else:
            hash = self.hash_function(key)
            size = self.capacity
            index = hash % size
            return self.buckets.get_at_index(index).contains(key).value


    def put(self, key: str, value: object) -> None:
        """
        This function uses when of the put in hash functions to find the index. We use modulus to convert higher numbers
        into valid numbers given the size of the table
        """
        hash= self.hash_function(key)
        size=self.capacity
        index= hash%size
        linked=self.buckets.get_at_index(index)
        if self.is_empty_linked(linked)==True:
            linked.insert(key,value)
        elif linked.contains(key)!=None:
            linked.remove(key)
            self.size = self.size - 1
            linked.insert(key, value)
        else:
            linked.insert(key, value)
        self.size=self.size+1

    def is_empty_linked(self,linked):
        empty=True
        if linked.length()>0:
            empty=False
        return empty


    def remove(self, key: str) -> None:
        """
        Remove a key by finding index and then removing that value in the linked list. If none existant returns None
        """
        hash = self.hash_function(key)
        size = self.capacity
        index = hash % size
        value=None
        if self.buckets.get_at_index(index).contains(key)!=None:
            value=self.buckets.get_at_index(index).contains(key).value
            self.buckets.get_at_index(index).remove(key)
            self.size=self.size-1
        return value





    def contains_key(self, key: str) -> bool:
        """
        Find if hash map contains a key, buy finding index and then checking that linked list. If not found returns False, otherwise
        returns true
        """
        hash = self.hash_function(key)
        size = self.capacity
        index = hash % size
        t=self.buckets.get_at_index(index)
        if self.buckets.get_at_index(index).contains(key):
            return True
        return False

    def empty_buckets(self) -> int:
        """
        This implementation finds the number of empty index by going through the Dynamic table
        Finding which indexes have empty linkedlist
        """
        empty=0
        size=self.capacity
        for index in range(0,size):
            if self.buckets.get_at_index(index).length()==0:
                empty=empty+1
        return empty

    def table_load(self) -> float:
        """
        Very simple script to return the ratio of elements in table to the total capacity of that table
        """
        return self.size/self.capacity

    def resize_table(self, new_capacity: int) -> None:
        """
        resizes the hashmap and recalculates the indexes
        """


        if new_capacity==0:
            return
        newtable=DynamicArray()
        nodetable = DynamicArray()
        #create a new empty dynamic arrays
        for x in range(new_capacity):
            newtable.append(LinkedList())
        for x in range(0, self.size):
            nodetable.append(None)
        linkstart=0
       #get all the linked list in dynamic array, and get their nodes. Insert into keylist
        for x in range(self.capacity-1,-1,-1):
            linked=self.buckets.get_at_index(x)
            if self.is_empty_linked(linked)==True:
                continue
            currentlink=linkstart+linked.length()-1
            linkstart=currentlink+1
            for node in linked:
                nodetable.set_at_index(currentlink,node)
                currentlink=currentlink-1


        self.size = 0
        self.capacity =new_capacity
        self.buckets = newtable
       #reverse order because of how insert works by replacing the head
        for index in range(nodetable.length()-1,-1,-1):
            currentnode=nodetable.get_at_index(index)
            self.put(currentnode.key,currentnode.value)




    def get_keys(self) -> DynamicArray:
        """
        Creates a array of all the keys
        """
        j=0
        keys=DynamicArray(None)
        for i in range (0,self.size):
            keys.append(None)
        for i in range(0, self.buckets.length()):
            link = self.buckets.get_at_index(i)
            if link.length() == 0:
                continue
            else:
                for nodes in link:
                    keys.set_at_index(j,nodes.key)
                    j=j+1
        return keys


# BASIC TESTING
if __name__ == "__main__":

    # print("\nPDF - empty_buckets example 1")
    # print("-----------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key1', 10)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key2', 20)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key1', 30)
    # print(m.empty_buckets(), m.size, m.capacity)
    # m.put('key4', 40)
    # print(m.empty_buckets(), m.size, m.capacity)
    #
    # #
    # print("\nPDF - empty_buckets example 2")
    # print("-----------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('key' + str(i), i * 100)
    #     #print(i,m.empty_buckets(), m.size, m.capacity)
    #     if i % 30 == 0:
    #         print(m.empty_buckets(), m.size, m.capacity)
    #
    #
    # print("\nPDF - table_load example 1")
    # print("--------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.table_load())
    # m.put('key1', 10)
    # print(m.table_load())
    # m.put('key2', 20)
    # print(m.table_load())
    # m.put('key1', 30)
    # print(m.table_load())
    # #
    # #
    # print("\nPDF - table_load example 2")
    # print("--------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(50):
    #     m.put('key' + str(i), i * 100)
    #     if i % 10 == 0:
    #         print(m.table_load(), m.size, m.capacity)
    #
    # print("\nPDF - clear example 1")
    # print("---------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.size, m.capacity)
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key1', 30)
    # print(m.size, m.capacity)
    # m.clear()
    # print(m.size, m.capacity)
    #
    #
    # # print("\nPDF - clear example 2")
    # # print("---------------------")
    # # m = HashMap(50, hash_function_1)
    # # print(m.size, m.capacity)
    # # m.put('key1', 10)
    # # print(m.size, m.capacity)
    # # m.put('key2', 20)
    # # print(m.size, m.capacity)
    # # m.resize_table(100)
    # # print(m.size, m.capacity)
    # # m.clear()
    # # print(m.size, m.capacity)
    #
    #
    # print("\nPDF - put example 1")
    # print("-------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('str' + str(i), i * 100)
    #     if i % 25 == 24:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)
    #
    #
    #
    # print("\nPDF - put example 2")
    # print("-------------------")
    # m = HashMap(40, hash_function_2)
    # for i in range(50):
    #     m.put('str' + str(i // 3), i * 100)
    #     if i % 10 == 9:
    #         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)
    #
    #
    # print("\nPDF - contains_key example 1")
    # print("----------------------------")
    # m = HashMap(10, hash_function_1)
    # print(m.contains_key('key1'))
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key3', 30)
    # print(m.contains_key('key1'))
    # print(m.contains_key('key4'))
    # print(m.contains_key('key2'))
    # print(m.contains_key('key3'))
    # m.remove('key3')
    # print(m.contains_key('key3'))
    # #
    #
    # print("\nPDF - contains_key example 2")
    # print("----------------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 20)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.size, m.capacity)
    # result = True
    # for key in keys:
    #     # all inserted keys must be present
    #     result &= m.contains_key(str(key))
    #     # NOT inserted keys must be absent
    #     result &= not m.contains_key(str(key + 1))
    # print(result)
    #
    #
    # print("\nPDF - get example 1")
    # print("-------------------")
    # m = HashMap(30, hash_function_1)
    # print(m.get('key'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    #
    #
    # print("\nPDF - get example 2")
    # print("-------------------")
    # m = HashMap(150, hash_function_2)
    # for i in range(200, 300, 7):
    #     m.put(str(i), i * 10)
    # print(m.size, m.capacity)
    # for i in range(200, 300, 21):
    #     print(i, m.get(str(i)), m.get(str(i)) == i * 10)
    #     print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)
    #
    #
    # print("\nPDF - remove example 1")
    # print("----------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.get('key1'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    # m.remove('key1')
    # print(m.get('key1'))
    # m.remove('key4')
    # #
    # #
    # # print("\nPDF - resize example 1")
    # # print("----------------------")
    # # m = HashMap(20, hash_function_1)
    # # m.put('key1', 10)
    # # print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    # # m.resize_table(30)
    # # print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    #
    #
    # print("\nPDF - resize example 2")
    # print("----------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 13)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.size, m.capacity)
    #
    # for capacity in range(111, 1000, 117):
    #     m.resize_table(capacity)
    #
    #     m.put('some key', 'some value')
    #     result = m.contains_key('some key')
    #     m.remove('some key')
    #
    #     for key in keys:
    #         result &= m.contains_key(str(key))
    #         result &= not m.contains_key(str(key + 1))
    #     print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))
    #
    #
    # print("\nPDF - get_keys example 1")
    # print("------------------------")
    # m = HashMap(10, hash_function_2)
    # for i in range(100, 200, 10):
    #     m.put(str(i), str(i * 10))
    # print(m.get_keys())
    #
    # m.resize_table(1)
    # print(m.get_keys())
    #
    # m.put('200', '2000')
    # m.remove('100')
    # m.resize_table(2)
    # print(m.get_keys())

    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())
    m.resize_table(1)
    print(m.get_keys())


