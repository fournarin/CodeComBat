# ถ้ามีศัตรู ให้โจมตีมัน
# มิฉะนั้น โจมตีหีบสมบัติ!

while True:
    enemy = hero.findNearestEnemy()
    # ใช้ if/else
    if enemy:
        hero.attack(enemy)
        hero.attack(enemy)
    else:
        hero.attack("Chest")
    
    