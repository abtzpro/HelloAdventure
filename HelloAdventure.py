import random

# Define the player's starting attributes
player = {
    'name': '',
    'health': 100,
    'attack': 10,
    'gold': 0,
    'inventory': []
}

# Define the monsters and their attributes
monsters = [
    {'name': 'Goblin', 'health': 20, 'attack': 5},
    {'name': 'Skeleton', 'health': 30, 'attack': 10},
    {'name': 'Orc', 'health': 40, 'attack': 15},
    {'name': 'Dragon', 'health': 100, 'attack': 30},
]

# Define the loot items and their attributes
loot_items = [
    {'name': 'Potion', 'healing': 20},
    {'name': 'Gold', 'value': 10},
    {'name': 'Sword', 'attack': 10},
    {'name': 'Shield', 'defense': 10},
]

# Define the game loop
def game_loop():
    print('Welcome to the dungeon!')
    player['name'] = input('What is your name? ')

    # Loop until the player dies or quits
    while player['health'] > 0:
        print('You are in a room with a monster...')
        monster = random.choice(monsters)
        print('A', monster['name'], 'attacks you!')
        
        # Loop until either the player or the monster dies
        while player['health'] > 0 and monster['health'] > 0:
            print('Your health:', player['health'])
            print('Monster health:', monster['health'])
            action = input('Do you want to attack (a) or run away (r)? ')

            if action == 'a':
                # Player attacks the monster
                damage = player['attack'] + random.randint(1, 6)
                print('You attack the', monster['name'], 'for', damage, 'damage!')
                monster['health'] -= damage

                if monster['health'] > 0:
                    # Monster attacks the player
                    damage = monster['attack'] + random.randint(1, 6)
                    print('The', monster['name'], 'attacks you for', damage, 'damage!')
                    player['health'] -= damage
            else:
                # Player runs away
                print('You run away from the', monster['name'], 'and hide in another room.')
                break

        if player['health'] <= 0:
            print('You died...')
            break

        print('You defeated the', monster['name'], 'and found some loot!')
        loot_item = random.choice(loot_items)
        print('You found a', loot_item['name'])
        player['inventory'].append(loot_item)

        if 'healing' in loot_item:
            # Player found a healing item
            player['health'] += loot_item['healing']
            print('You use the', loot_item['name'], 'and heal for', loot_item['healing'], 'health!')

        if 'value' in loot_item:
            # Player found a gold item
            player['gold'] += loot_item['value']
            print('You found', loot_item['value'], 'gold!')
        
        print('Your inventory:', player['inventory'])
        print('Your gold:', player['gold'])

game_loop()
