#define dict
list = []
new_apple = {
    'name' : 'apple',
    'price' : 0.99,
    'barcode' : '2342355',
}
list.append(new_apple)
new_chips = {
    'name' : 'spicy chips',
    'price' : 1.25,
    'barcode' : '2543432',
}
list.append(new_chips)
new_bar = {
    'name' : 'protein bar',
    'price' : 2.50,
    'barcode' : '3451232'
}
list.append(new_bar)

print("---")
print("Using seq and for statement")
seq = [x['price'] for x in list]
print("The minimum price is", min(seq))
print("The maximum price is", max(seq))
print("---")
max_price_item = max(list, key=lambda x:x['price'])
min_price_item = min(list, key=lambda x:x['price'])
print('Using the key=lambda')
print("Max priced item", max_price_item)
print("Min priced item", min_price_item)
print("---")
print(list)