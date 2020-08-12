# Course: CS261 - Data Structures
# Assignment: 5
# Student:Tobi Fanibi
# Description:minheap object Class. Heap is implemented on top of a DynamicArray


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *

class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Add a new element to heap and perculate it down
        """
        end_index=self.heap.length()
        parent_index=((end_index-1)//2)
        if end_index==0:
            self.heap.append(node)
        else:
            self.heap.append(node)
            while self.heap.get_at_index(end_index)<self.heap.get_at_index(parent_index):
                self.heap.swap(end_index,parent_index)
                end_index=parent_index
                if end_index==0:
                    break
                parent_index=(end_index-1)//2

    def get_min(self) -> object:
        """
        Return the top of the minheap if empty return None
        """
        if self.is_empty()==True:
            return None
        return self.heap.get_at_index(0)

    def find_min_child(self,index1, index2):
        """
        Find the minumum index between two or one or No children. If No children returns None
        """
        try:
            min1=self.heap.get_at_index(index1)
        except:
            min1=None

        try:
            min2 = self.heap.get_at_index(index2)
        except:
            min2 = None
        if min1==None and min2==None:
            return None
        elif min2 == None and min1 != None:
            return index1
        elif min1==None and min2!=None:
            return index2
        elif min1<=min2:
            return index1
        elif min2<min1:
            return index2

    def remove_min(self) -> object:
        """
        Remove the top of the minheap and perculate the replacement value(last value) down
        """
        if self.is_empty():
            raise MinHeapException
            return
        parent_index=0
        parent=self.get_min()
        #parent=5
        #print(parent)
        #print(self)
        self.heap.swap(parent_index,self.heap.length()-1)
        self.heap.pop()
        if self.is_empty():
            return parent
        min_child=self.find_min_child(1,2)
        while min_child!=None:
            if self.heap.get_at_index(min_child)>self.heap.get_at_index(parent_index):
                break
            self.heap.swap(min_child,parent_index)
            parent_index=min_child
            if parent_index==None:
                break
            min_child=self.find_min_child((parent_index * 2)+1,(parent_index * 2) + 2)
        return parent


    def build_heap(self, da: DynamicArray) -> None:
        """
        Sort and Unsorted array to make a minheap
        """
        da2=DynamicArray()
        #We want da to not change so we need to create a hard copy of da, not tied to the same memory address
        #this operation is n
        for x in range(0,da.length()):
            da_int=da.get_at_index(x)
            da2.append(da_int)
        if da2.length()==0:
            raise MinHeapException
            return
        self.heap = da2
        end=self.heap.length()-1
        #unlock default heap_sort current starts at the last leaf node. So only that section is
        #heap_sorted instead of the entire minheap
        current=(end//2)-1
        #this is n, so 2n or O(n) with the base removed
        self.build_heap_helper(current)



    def build_heap_helper(self, current):
        """
        Helper function for build heap
        """
        if current==-1:
            return
        parent_index=current
        min_child=self.find_min_child((parent_index * 2)+1,(parent_index * 2) + 2)
        while min_child!=None:
            if self.heap.get_at_index(parent_index)<self.heap.get_at_index(min_child):
                break
            self.heap.swap(min_child,parent_index)
            parent_index=min_child
            min_child=self.find_min_child((parent_index * 2)+1,(parent_index * 2) + 2)
            if min_child==None:
                break
        self.build_heap_helper(current-1)





# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([13,15,15,20,18,16,24,28,32])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    #da = DynamicArray([32,12,2,8,16,20,24,40,4])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
