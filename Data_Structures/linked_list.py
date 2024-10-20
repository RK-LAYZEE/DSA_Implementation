class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f'Node Data: {self.data}'

class LL:
    def __init__(self) -> None:
        self.head = None

    def size(self) -> int:
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next
        return count

    def insert_start(self, data) -> None:
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_end(self, data) -> None:
        new = Node(data)
        current = self.head

        if not current:
            return self.insert_start(data)

        while current.next:
            current = current.next

        current.next = new
        new.next = None

    def insert_index(self, data, index):
        if index == 0:
            return self.insert_start(data)
        
        new = Node(data)
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                next_node = current.next
                new.next = next_node
                current.next = new
                return None
            current = current.next
            count += 1 
        return "Index Not Found"

    def search_index(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1
        return "Index Not Found"

    def search_value(self, value):
        current = self.head
        count = 0
        while current:
            if current.data == value:
                return f"Element {value} found at index: {count}"
            current = current.next
            count += 1
        return "Element Not Found" 

    def delete_start(self) -> None:
        if self.size() == 0:
            return None
        
        current = self.head
        self.head = current.next

    def delete_end(self) -> None:
        if self.size() == 0:
            return None
        if self.size() == 1:
            return self.delete_start()
        
        current = self.head
        next_node = current.next
        while next_node.next:
            current = next_node
            next_node = current.next
        current.next = None

    def delete_index(self, index) -> None:
        current = self.head
        count = 0
        if self.size() == 0:
            return "List has not elements"
        if self.size() == 1:
            if index != 0:
                return "Index Not Found"
            else:
                return self.delete_start()
        while current.next:
            if index == 0:
                return self.delete_start()
            if count == index - 1:
                next_node = current.next
                current.next = next_node.next
                return None
            current = current.next
            count += 1
        return "Index Not Found"

    def delete_value(self, value) -> str:
        current = self.head
        if self.size() == 0:
            return "List has no values"
        if current.data == value:
            return self.delete_start()
        while current.next:
            next_node = current.next
            if next_node.data == value:
                current.next = next_node.next
                return "Value Deleted"
            current = current.next
        return "Value Not Found"

    def __repr__(self) -> str:
        linked_path = []
        current = self.head
        if not current:                                         # if current is None 
            return "Empty List"
        
        while current:                                          # while current != None
            linked_path.append(f'{current.data}')
            current = current.next
        
        return ' -> '.join(linked_path)
    
