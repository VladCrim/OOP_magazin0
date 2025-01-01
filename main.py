# Создай класс Store. Атрибуты класса: name: название магазина.
# address: адрес магазина. items: словарь, где ключ - название товара, а значение - его цена.
# Например, {'apples': 0.5, 'bananas': 0.75}.
# Методы класса:
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь
# для items`.
# метод для добавления товара в ассортимент.
# метод для удаления товара из ассортимента.
# метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
# метод для обновления цены товара.
# 2. Создай несколько объектов класса Store:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь
# в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы:
# добавь товар, обнови цену, убери товар и запрашивай цену.

class Store():
    def __init__(self, name, address, items):
        self.name = name
        self.address = address
        self.items = items if items is not None else {}

    def add_item(self, name, price):
        self.items[name] = price
        print(f"Товар '{name}' добавлен в ассортимент магазина '{self.name}'.")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Товар '{name}' удален из ассортимента магазина '{self.name}'.")
        else:
            print(f"Товар '{name}' отсутствует в ассортименте магазина '{self.name}'.")

    def get_price(self, name):
        return self.items.get(name, None)

    def update_price(self, name, new_price):
        if name in self.items:
            self.items[name] = new_price
            print(f"Цена товара '{name}' в магазине '{self.name}' обновлена.")
        else:
            print(f"Товар '{name}' отсутствует в ассортименте магазина '{self.name}'.")

store1 = Store('Store1', 'address1', {'apples': 0.5, 'bananas': 0.75})
store2 = Store('Store2', 'address2', {'berries': 3.25, 'cherry': 1.35})
store3 = Store('Store3', 'address3', {'melons': 5.5, 'plums': 2.15})

print(store1.items)
print(store2.items)
print(store3.items)

store1.add_item('berries', 3.25)
store2.remove_item('cherry')
print(store1.items)
print(store2.items)
print(store3.items)

print(store1.get_price('apples'))
print(store2.get_price('berries'))
print(store3.get_price('melons'))

store1.update_price('apples', 0.75)
print(store1.items)
