import unittest
from name import get_full_name,get_biggest,get_list,get_even,check_fibo

class NameTest(unittest.TestCase):

    def test_ism(self):
        formatted_name = get_full_name('muhammadzoir','sherboboev')
        self.assertEqual(formatted_name, 'Muhammadzoir Sherboboev')

    def test_ifo(self):
        name = get_full_name("muhammadzoir","sherboboev","ibrakhimjanovich")
        self.assertEqual(name,"Sherboboev Muhammadzoir Ibrakhimjanovich")

    def test_get_biggest(self):
        num = get_biggest(5,3,1)
        self.assertEqual(num,5)

    def test_get_list(self):
        mylist = get_list(['hammaga assalom alaykum, vahokazo'])
        self.assertEqual(mylist,'Hammaga Assalom Alaykum, Vahokazo')

    def test_even(self):
        evens = get_even([2,4,6,8,10,9,7,5,3,1])
        self.assertEqual(evens,[2,4,6,8,10])

    def test_fibo(self):
        son = check_fibo(13)
        self.assertEqual(son,True)
unittest.main()