# integer 
black_grams = 14
ginger_grams = 14

total_grams = black_grams + ginger_grams
print(f'Total grams of base tea {total_grams}')

remaining_tea = ginger_grams - black_grams # normal division 
print(f'Total grams of tea remaining {remaining_tea}')

milk_litres = 7
serving = 4

milk_per_serving = milk_litres / serving # division 
print(f'Milk per serving is {milk_per_serving}')

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots #  division with not caring about decimal 
print (f'Tea bags per pot {bags_per_pot}')

total_cardamom_pods = 10
pods_per_cup = 3

left_over_pods = total_cardamom_pods % pods_per_cup # when we want to have remainder 
print(f'leftover cadamom pods {left_over_pods}')

Base_flavor_strenght = 2
scale_factor = 3
powerful_flavor = Base_flavor_strenght ** scale_factor # 2 to the power 3

print(f'exponential {powerful_flavor}')

total_tea_leaves_harvested = 1_000_000_000
print(f'tea leaves {total_tea_leaves_harvested}')




