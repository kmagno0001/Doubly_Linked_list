class Node:
    def __init__(self, value: any, prev_node = None, next_node = None ) -> None:
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def get_value(self) -> any:
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def get_prev_node(self) :
        return self.prev_node

    def set_next_node(self, new_next_node) -> None:
        self.next_node = new_next_node   

    def set_prev_node(self, new_prev_node) -> None:
        self.prev_node = new_prev_node    