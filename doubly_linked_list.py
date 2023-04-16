from node import Node

class Doubly_linked_list :
    def __init__(self, value: any) -> None:
        self.head_node = Node(value)
        self.len = 1

    def __repr__(self) -> str:
        str_list = ''

        iterator: Node = self.head_node
        while iterator.get_next_node() != None:
            str_list += f" {iterator.get_value()} "
            iterator = iterator.get_next_node()
        else:
            str_list += f" {iterator.get_value()} "   
        
        return str_list

    def add(self, value: any, index: int = None) -> None:
        iterator_node: Node = self.head_node

        match index: 
            case None: 
                while iterator_node.get_next_node() is not None:
                    iterator_node =  iterator_node.get_next_node()

                iterator_node.set_next_node(Node(value, iterator_node))

            case 0:
                new_node: Node = Node(value, None, iterator_node)
                iterator_node.set_prev_node(new_node)
                self.head_node = new_node

            case deful:
                if index >= self.len: return
               
                counter = 0
                while iterator_node.get_next_node() != None:
                    if counter == index:
                        prev_n: Node = iterator_node.get_prev_node()
                        next_n: Node = iterator_node.get_next_node()
                        new_node: Node = Node(value, prev_n, next_n)
                        prev_n.set_next_node(new_node)
                        next_n.set_prev_node(new_node)
                        break

                    iterator_node = iterator_node.get_next_node()  
                    counter += 1  

        self.len += 1

    def remove(self, value) -> None:
        iterator: Node = self.head_node
        
        while iterator.get_next_node() != None:
            if iterator.get_value() == value:
                break
            iterator = iterator.get_next_node()

        prev_node: Node = iterator.get_prev_node() if iterator.get_prev_node() is not None else None
        next_node: Node = iterator.get_next_node() if iterator.get_next_node() is not None else None

        if prev_node is not None:
            prev_node.set_next_node(next_node)
        else:
            iterator.set_prev_node(None)
            self.head_node = iterator.get_next_node()
            
        if next_node is not None:
            next_node.set_prev_node(prev_node)
       

        
       

        
