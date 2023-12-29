class ShoppingList():
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_items(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
    
    def remove_item(self, item):
        self.shopping_list.remove(item)

    def view_list(self):
        print(self.shopping_list)

pet_store_list = ShoppingList("Pet Store Shopping List")

pet_store_list.add_items("dog food")
pet_store_list.add_items("frisbee")
pet_store_list.add_items("bowl")
pet_store_list.add_items("collars")
pet_store_list.add_items("flea collars")

pet_store_list.remove_item("flea collars")

pet_store_list.add_items("frisbee")

pet_store_list.view_list()