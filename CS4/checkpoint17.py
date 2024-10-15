# ขั้นแรก ลูปศัตรูทั้งหมด...

enemies = hero.findEnemies()
enemyIndex = 0
# ... แต่โจมตีเฉพาะศัตรูประเภท "thrower"
while enemyIndex < len(enemies):
    enemy = enemies[enemyIndex]
    if enemy and enemy.type == "thrower":
        hero.attack(enemy)
    enemyIndex += 1
# แล้วลูปศัตรูทั้งหมดอีกครั้ง...
enemies = hero.findEnemies()
enemyIndex = 0
# ...และปราบทุกคนที่ยังไม่ตาย
while enemyIndex < len(enemies):
    enemy = enemies[enemyIndex]
    if enemy and enemy.health > 0:
        while enemy.health > 0:
            hero.attack(enemy)
    enemyIndex += 1
