# ไปที่เครื่องหมาย X สีแดง แต่ระวังตัว!
# พื้นที่ป่าเหล่านี้อาจมีพวก ogres!

hero.moveXY(19, 33)
enemy = hero.findNearestEnemy()
# คำสั่ง if จะตรวจสอบว่าตัวแปรมีโอกเรไหม
if enemy:
    hero.attack(enemy)
    hero.attack(enemy)
    pass

hero.moveXY(30, 50)
hero.moveXY(49, 51)
enemy = hero.findNearestEnemy()
if enemy:
    # โจมตีศัตรูตรงนี้:
    hero.attack(enemy)
    hero.attack(enemy)
    # คำสั่ง `pass` เป็นตัววาง. มันไม่ได้ทำอะไรและช่วยปิด if-statements.
    pass
pet.moveXY(67, 47)
hero.moveXY(66, 20)
hero.moveXY(58, 14)
enemy = hero.findNearestEnemy()
# ใช้ if-statement เพื่อตรวจสอบว่ามีศัตรูอยู่หรือไม่:
if enemy:
    hero.attack(enemy)
    hero.attack(enemy)
    pass
    # ถ้ามีศัตรู ให้โจมตีมัน:
    