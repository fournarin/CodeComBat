# ตีเฉพาะศัตรูที่เป็น "munchkin" และ "thrower" เท่านั้น
# อย่าโจมตี "burl" หนีจาก "ogre" ดีกว่า!
while True:
    enemy = hero.findNearestEnemy()
    
    # ข้อควรจำ: อย่าโจมตีประเภท "burl"!
    if enemy.type == "burl":
        hero.say("ฉันไม่ได้โจมตี Burl นั่น!")
    
    # คุณสมบัติ "type" จะบอกคุณว่ามันเป็นสิ่งมีชีวิตประเภทไหน
    if enemy.type == "munchkin":
        hero.attack(enemy)
    
    # ใช้ "if" เพื่อโจมตี "thrower"
    if enemy.type == "thrower":
        hero.attack(enemy)
    
    # ถ้าเป็น "ogre" ให้ใช้ moveXY หนีไปที่ประตูหมู่บ้าน!
    if enemy.type == "ogre":
        hero.moveXY(41, 47)