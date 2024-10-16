# ไปที่วิซาร์ดและรับค่าลับ
hero.moveXY(20, 24)
secretA = hero.findNearestFriend().getSecretA()
secretB = hero.findNearestFriend().getSecretB()
secretC = hero.findNearestFriend().getSecretC()

# ถ้าทั้งสามค่าเป็นจริง ให้ใช้เส้นทางสูง
# มิฉะนั้นให้ใช้เส้นทางที่ต่ำ บันทึกค่าที่ 4
secretD = secretA and secretB and secretC
if secretD:
    hero.moveXY(30, 33)
else:
    hero.moveXY(30, 15)

# หากค่าใดค่าหนึ่งในสามค่าเป็นจริง ให้ใช้เส้นทางด้านซ้าย
# ไม่งั้นก็ไปทางขวา บันทึกค่าที่ 5
secretE = secretA or secretB or secretC
if secretE:
    hero.moveXY(20, 24)
else:
    hero.moveXY(40, 24)
# หากค่าทั้งห้าเป็นจริง ให้ใช้เส้นทางที่สูง
# มิฉะนั้นให้ใช้เส้นทางที่ต่ำ
secretF = secretA and secretB and secretC and secretC and secretE
if secretF:
    hero.moveXY(30, 33)
else:
    hero.moveXY(30, 15)