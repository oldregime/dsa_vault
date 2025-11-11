class Node :
    def __init__(self,data):

        self.data = data
        self.next = None
# a class node contain a data fieled to store pointer info and pointer to next node

def taversal(head):
    while head is not None :
        print(head.data , end = " " )
        if head.next is not None :
            print("->" , end = " ")
        head =head.next
    print()


# create the first node 
head = Node(10)
#link to second node
head.next = Node(120)

head.next.next = Node(30)
head.next.next.next = Node(30)
head.next.next.next.next = Node(40)

temp = head 
# while temp is not None :
#     print(temp.data , end = " ")
#     temp = temp.next

taversal(temp)

        
        