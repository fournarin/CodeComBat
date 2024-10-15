def findStrongestEnemy(enemies):
    strongest = None
    strongestHealth = 0
    enemyIndex = 0
    
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        
        if enemy.health > strongestHealth:
            strongest = enemy  
            strongestHealth = enemy.health  
        
        enemyIndex += 1
    
    return strongest

enemies = hero.findEnemies()
leader = findStrongestEnemy(enemies)

if leader:
    hero.say(leader.id)