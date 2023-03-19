shop = {
"rowerowy":["opony","oświetlenie do roweru","kask"],
"decathlon":["rękawiczki", "kask"]
}
print("Lista zakupów")
for items in shop:
    print(f'Idę do {items.upper()} kupuję tu: {shop[items]}')