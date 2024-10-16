# พวกยักษ์ปลอมตัวเป็นเหรียญหรืออัญมณี!

while True:
    enemy = hero.findNearestEnemy()
    # หากคุณเห็นศัตรู - โจมตี
    if enemy:
        if hero.isReady("cleave"):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
    item = hero.findNearestItem()
    # หากคุณเห็นเหรียญหรืออัญมณี - ย้ายไปที่ตำแหน่ง X และ Y
    if item:
        itempos = item.pos
        itemx = itempos.x
        itemy = itempos.y
        hero.moveXY(itemx, itemy)