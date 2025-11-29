class Node:
    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, student_id, name, score):
        new_node = Node(student_id, name, score)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self, student_id):
        cur = self.head
        if cur and cur.student_id == student_id:
            self.head = cur.next
            return
        prev = None
        while cur and cur.student_id != student_id:
            prev = cur
            cur = cur.next
        if cur:
            prev.next = cur.next

    def print_list(self):
        cur = self.head
        print("Student ID | Name       | Score")
        print("-" * 30)
        while cur:
            print(f"{cur.student_id:<10} | {cur.name:<8} | {cur.score}")
            cur = cur.next

# Example with real data
students = SinglyLinkedList()
students.append("S01", "Alice", 85)
students.append("S02", "Bob", 90)
students.append("S03", "Charlie", 78)
students.append("S04", "Diana", 88)

print("=== Original Student List ===")
students.print_list()

students.delete("S03")
print("\n=== After Deleting S03 (Charlie) ===")
students.print_list()