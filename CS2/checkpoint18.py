while True:
    # เช็คระยะห่างจากศัตรูที่อยู่ใกล้ที่สุด
    nearestEnemy = hero.findNearestEnemy()
    distance = hero.distanceTo(nearestEnemy)
    # ถ้ามันเข้ามาใกล้กว่า 10 เมตร, ฟันมันให้ละเอียด!
    if distance < 10:
        if hero.isReady("cleave"):
            hero.cleave(nearestEnemy)
        else:
            hero.attack(nearestEnemy)
    # ถ้าไม่มีอย่างอื่น ให้โจมตี "Chest" ตามชื่อ
    else:
        hero.attack("Chest")
    pass
    