# สัตว์เลี้ยงของคุณควรแปลคำสั่งได้
 
def onHear(event):
    # ข้อความที่สัตว์เลี้ยงได้ยินอยู่ใน event.message
    message = event.message
    # หากข้อความเป็น "North"
    if message == "North":
        # สัตว์เลี้ยงพูดว่า "Htron"
        pet.say("Htron")
    # หากข้อความเป็น "South"
    if message == "South":
        # สัตว์เลี้ยงพูดว่า "Htuos"
        pet.say("Htuos")
        pass
    # หากข้อความเป็น "East"
    if message == "East":
        # สัตว์เลี้ยงพูดว่า "Tsae"
        pet.say("Tsae")

# กำหนดตัวจัดการอีเวนท์
pet.on("hear", onHear)

while True:
    enemy = hero.findNearestEnemy()
    # อย่าโจมตี Brawlers
    if enemy and enemy.type != "brawler":
        hero.attack(enemy)
    else:
        hero.moveXY(26, 26)
