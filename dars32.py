class Shaxs():
    """Shaxs nomli klass yaratamiz"""
    __s_soni = 0
    def __init__(self,ism,familiya):
        self.ism = ism
        self.familiya = familiya
        Shaxs.__s_soni += 1
    @classmethod
    def get_s_num(cls):
        return Shaxs.__s_soni

    def get_info(self):
        """Shaxs haqida malumot"""
        return f"{self.ism} {self.familiya}. "

    def get_name(self):
        """Shaxs ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Shaxs familiyasini qaytaradi"""
        return self.familiya


class Talaba(Shaxs):
    """Talaba nomli klass"""
    __t_soni = 0
    def __init__(self,ism,familiya):
        super().__init__(ism,familiya)
        self.ism = ism
        Talaba.__t_soni += 1
    @classmethod
    def get_t_num(cls):
        return Talaba.__t_soni
men = Shaxs("Muhammad","Sherboboev")
talaba = Talaba(men.get_name(),men.get_lastname())
print(talaba.get_s_num())