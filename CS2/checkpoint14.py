# การโจมตีของคุณกำลังคูลดาวน์ 10 วินาที
# ใช้คำสั่งอื่นเพื่อป้องกันตัวเองขณะรอการชาร์จ

while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    # เขียน else: ทำบางอย่างเมื่อ "cleave" ไม่พร้อม
    else:
        hero.attack(enemy)
        # อย่าลืมโจมตีศัตรู
        
        