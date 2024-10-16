# นำชาวบ้านและผู้รักษาผ่านเขตที่วางทุ่นระเบิด

while True:
    coin = hero.findNearestItem()
    healingThreshold = hero.maxHealth / 2
    # เช็กเพื่อดูว่าคุณได้รับบาดเจ็บสาหัสหรือไม่
    if hero.health < healingThreshold:
        # ไปทางซ้าย 10 เมตร
        hero.moveXY(hero.pos.x-10, hero.pos.y)
        # ขอให้รักษา
        hero.say("Can I get a heal?")
        pass
    # else เคลื่อนที่ไปที่เหรียญ
    elif coin:
        hero.moveXY(coin.pos.x, coin.pos.y)