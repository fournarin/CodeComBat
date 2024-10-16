# สัตว์เลี้ยงของคุณสามารถช่วยให้คุณอยู่รอดได้จนกว่าคุณจะสามารถหลบหนีได้

def onHear(event):
    # event.message มีข้อความที่ได้ยิน
    # ถ้าใครพูด "ยิง"
    if event.message == "ยิง":
        # ไปที่เครื่องหมาย X ด้านล่างด้วย pet.moveXY()
        pet.moveXY(64, 16)
        # พูดอะไรกับ pet.say()
        pet.say("!!")
        pass
    # ถ้าใครพูด "รักษา"
    elif event.message == "รักษา":
        # ไปที่เครื่องหมาย X ด้านบนด้วย pet.moveXY()
        pet.moveXY(64, 52)
        # พูดอะไรกับ pet.say()
        pet.say("UwU")
        pass

pet.on("hear", onHear)

# คุณไม่จำเป็นต้องเปลี่ยนโค้ดด้านล่าง
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # หากศัตรูแข็งแกร่งเกินไป
        if enemy.type == "brawler":
            hero.say("ยิง")
        else:
            hero.attack(enemy)
    else:
        # ถ้าฮีโร่ของคุณต้องการการรักษา
        if hero.health < hero.maxHealth / 2:
            hero.say("รักษา")