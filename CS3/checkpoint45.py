# ล่อยักษ์เข้าไปในกับดัก พวกยักษ์พวกนี้ระวังตัวดีมาก
# พวกเขาจะตามมาก็ต่อเมื่อฮีโร่ได้รับบาดเจ็บ

# ฟังก์ชันนี้จะตรวจพลังชีวติของฮีโร่
# และส่งกลับค่าบูลีน
def shouldRun():
    if hero.health < hero.maxHealth / 2:
        return True
    else:
        return False

while True:
    enemy = hero.findNearestEnemy()
    # ย้ายไปที่ X แค่ตอนที่ shouldRun() ส่งคืน True
    if shouldRun() :
        hero.moveXY(75, 37)
    # ไม่อย่างนั้นให้โจมตี
    else:
        hero.attack(enemy)