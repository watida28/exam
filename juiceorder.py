class JuiceOder:
    
    menu_type = "JuiceOder"
    total = 0
    def __init__(self,menu:str,size:str,price:int) -> None:
        self.menu = menu.upper()
        self.size = size
        self.price = 0

    def check_menu(self):
        menu_dictionary = {
            'OJ':25,
            'AJ':25,
            'WJ':30,
            'PJ':30,
        }
         
        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)

    def JuiceOder(self):
        
        if self.size == 'R':
            #self.price = self.price + 1
            self.price += 0
        elif self.size == 'L':
            self.price += 5
        else:
            self.price
            
        JuiceOder.total = self.num * self.price

    def display_detail(self):
        self.check_menu()
        self.compute_price()
        return f' {self.manu} {self.size} * ${self.price} => ${JuiceOder.total}'

    def __del__(self):
        print("Object was destroyed")

    if __name__ =="__main__":
     order1 = JuiceOder('WJ','L')
     order2 = JuiceOder('OJ','R')
     order3 = JuiceOder('PJ','R')

    print(order1.display_detail())
    print(order2.display_detail())
    print(order3.display_detail())