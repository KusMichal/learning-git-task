shop = {
"rowerowy":["opony","oświetlenie do roweru","kask"],
"decathlon":["rękawiczki", "kask"]
}
print("Lista zakupów")
for items in shop:
    print(f'Idę do {items.upper()} kupuję tu: {shop[items]}')
x=len(shop["rowerowy"])+ len(shop["decathlon"])
print(f'W Sumie kupiłem {x} produktów')