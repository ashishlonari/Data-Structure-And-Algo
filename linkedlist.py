class node:
    def __init__(self,data=None):
        self.data = data;
        self.next = None;

class linkedlist:
    def __init__(self):
        self.head = node();

    def append(self,data):
        new_node = node(data);
        cur = self.head;
        while cur.next != None:
            cur = cur.next;
        cur.next = new_node;

    def length(self):
        total = 0
        cur = self.head;
        while cur.next != None:
            total+=1;
            cur = cur.next;
        return total;

    def display(self):
        elements =[];
        cur_node = self.head;
        while cur_node.next != None : 
            cur_node = cur_node.next;
            elements.append(cur_node.data);
        print(elements);

    def get(self,index):
        if index >= self.length():
            print("index not in range");
            return None;
        cur_indx = 0;
        cur_node = self.head;
        while True:
            cur_node = cur_node.next;
            if cur_indx == index:
                return cur_node.data;
            cur_indx +=1;

    def erase(self,index):
        if index >= self.length():
            print("index not in range");
            return None;
        cur_indx = 0;
        cur_node = self.head;
        while True:
            last_node = cur_node;
            cur_node = cur_node.next;
            if cur_indx == index:
                last_node.next = cur_node.next;
                return;
            cur_indx +=1






mylist  = linkedlist();
mylist.append(5);
mylist.append(30);
mylist.append(51);
mylist.append(34);
mylist.display();
print(mylist.get(2));

mylist.erase(3);
mylist.display();
