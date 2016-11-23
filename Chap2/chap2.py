import sys


class node:
    def __init__(self, cargo=None, next_val=None):
        self.cargo = cargo
        self.next_val = next_val

    def __str__(self):
        return str(self.cargo)


def insert(head, val):
    if not head:
        head = node(val)
        return head

    temp = head
    while temp.next_val:
        temp = temp.next_val
    temp.next_val = node(val)


def delete(head, val):
    temp = head

    while temp.cargo != val:
        prev = temp
        temp = temp.next_val

    prev.next_val = temp.next_val
    del (temp)


def remove_dupli(head):
    num = 0
    temp = head
    while temp:
        a = temp.cargo
        if not num & 1 << a:
            num = num | 1 << a
            prev = temp
            temp = temp.next_val
        else:
            prev.next_val = temp.next_val
            del(temp)
            temp = prev.next_val



def main():
    head = None
    head = insert(head, 1)
    insert(head, 2)
    insert(head, 4)
    insert(head, 7)
    insert(head, 7)
    insert(head, 89); insert(head, 17)

    temp = head
    while temp:
        print temp.cargo
        temp = temp.next_val

    #delete(head, 7)
    remove_dupli(head)
    while head:
        print head.cargo
        head = head.next_val


if __name__ == '__main__':
    main()
