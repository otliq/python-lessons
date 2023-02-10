import unittest

from class_test import Shaxs, Talaba


class TestKlass(unittest.TestCase):
    def setUp(self):
        ism = "MuhammadZoir"
        familiya = "Sherboboev"
        passport = "AC999"
        idraqam = "007"
        self.tyil = 2003
        self.talaba = Talaba(ism,familiya,passport,self.tyil,idraqam)
        self.shaxs1 = Shaxs(ism,familiya)
        self.shaxs2 = Shaxs(ism,familiya,passport)

    def Shaxs_test(self):
        #qiymat mavjudligini assertIsNotNone metodi bilan tekshiradi
        self.assertIsNone(self.shaxs1.ism)
        self.assertIsNone(self.shaxs1.familiya)
        self.assertIsNone(self.shaxs2.ism)
        #qiymat mavjud emaslgini assertIsNone metodi bilan tekshiradi
        self.assertIsNone(self.shaxs1.passport)

    def test_get_id(self):
        self.assertIsNotNone(self.talaba.get_id())


    def test_both_class(self):
        self.assertIsInstance(self.talaba,Shaxs)
        self.assertIsInstance(self.shaxs1,Shaxs)

unittest.main()

