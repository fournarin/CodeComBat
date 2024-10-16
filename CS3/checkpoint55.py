# เก็บกุญแจสามดอกและปลดปล่อยพาลาดิน

def onSpawn(event):
    # สัตว์เลี้ยงควรค้นหาและคาบกุญแจสามดอก
    # คุณต้องการไอเทมที่มีประเภทต่อไปนี้
    # "bronze-key", "silver-key" และ"gold-key".
    bkey = pet.findNearestByType("bronze-key")
    skey =  pet.findNearestByType("silver-key")
    gkey = pet.findNearestByType("gold-key")
    pet.fetch(bkey)
    pet.fetch(skey)
    pet.fetch(gkey)

pet.on("spawn", onSpawn)

while True:
    enemy = hero.findNearestEnemy()
    if enemy and enemy.team == "ogres":
        hero.attack(enemy)
    if hero.health < 300:
        # คุณสามารถใช้สัตว์เลี้ยงในเธรดหลักได้เช่นกัน
        potion = pet.findNearestByType("potion")
        if potion:
            hero.moveXY(potion.pos.x, potion.pos.y)