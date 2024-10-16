# ในระดับนี้ หินปีศาจคือสิ่งที่แย่มาก! หลบหลีกพวกเขาเดินไปทางอื่นดีกว่า
while True:
    evilstone = hero.findNearestItem()
    if evilstone:
        pos = evilstone.pos
        if pos.x == 34:     # == หมายถึง "is equal to"
            # หากหินปีศาจอยู่ทางซ้าย ให้ไปทางด้านขวา
            hero.moveXY(46, 22)
            pass
        else:
            # หากหินปีศาจอยู่ทางขวา ให้ไปทางด้านซ้าย
            if pos.x == 46:
                hero.moveXY(34, 22)
            pass
    else:
        # ถ้าไม่มีหินปีศาจ ไปที่ตรงกลาง
        hero.moveXY(40,22)
        pass
