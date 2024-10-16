# มันชกินส์เข้ามา! ปกป้องเมือง!

# กำหนดฟังก์ชั่นของคุณเองเพื่อต่อสู้กับศัตรู!
def cleaveOrAttack():
    # ในการทำงาน ค้นหาศัตรู จากนั้นโจมตีหรือโจมตีมัน
    ogre = hero.findNearestEnemy()
    if ogre:
        if hero.isReady("cleave"):
            hero.cleave(ogre)
        # มิฉะนั้นโจมตียักษ์:
        hero.attack(ogre)
# ย้ายระหว่างจุดลาดตระเวนและเรียกใช้ฟังก์ชัน
while True:
    hero.moveXY(35, 34)
    # ใช้ฟังก์ชัน cleaveOrAttack ที่คุณกำหนดไว้ข้างต้น
    cleaveOrAttack()
    hero.moveXY(47, 27)
    # เรียกใช้ฟังก์ชันอีกครั้ง
    cleaveOrAttack()
    hero.moveXY(60, 31)
    # เรียกใช้ฟังก์ชันอีกครั้ง
    cleaveOrAttack()
