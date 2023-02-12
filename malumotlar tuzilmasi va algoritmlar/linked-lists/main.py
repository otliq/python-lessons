"""
Ma'lumotlar tuzilmasi va algoritmlar
#05-LINKED LISTS
Muallif: Anvar Narzullaev
Web sahifa: https://t.me/sariq.dev
"""

from linkedlistsfunc import Node, LinkedList

## Linked List yaratamiz
kun_tartibi_ll = LinkedList()

## Uchta node (tugun) yaratamiz
kun_tartibi_ll.head = Node('Bomdod nomozini oqish')
nonushta = Node('Nonushta qilish')
oqish = Node('Universitetga borib oqish')

## Tugunlarni bog'laymiz
kun_tartibi_ll.head.next = nonushta
nonushta.next = oqish

## Linked Listni konsolga chiqaramiz:
# kun_tartibi_ll.printList()

## List boshiga yangi tugun qo'shamiz
kun_tartibi_ll.push('Taxorat olish')
# kun_tartibi_ll.printList()

## List o'rtasiga element qo'shamiz
kun_tartibi_ll.insertAfter(kun_tartibi_ll.head.next.next, 'Darsga tayorlanish')
# kun_tartibi_ll.printList()

## List oxiriga tugun qo'shamiz
kun_tartibi_ll.append('Peshin oqish')
kun_tartibi_ll.append('Uyga qaytish')
kun_tartibi_ll.append('Choy ichish')
# kun_tartibi_ll.printList()

## Element o'chiramiz
kun_tartibi_ll.deleteNode('Choy ichish')
kun_tartibi_ll.printList()