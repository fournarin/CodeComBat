# ทางออกเดียวถูกบล็อกโดยยักษ์
# ซ่อนตัวจากโครงกระดูกและปราบยักษ์ทีละตัว

# ฟังก์ชั่นนี้ควรโจมตีศัตรูและซ่อนตัว
def hitOrHide(target):
    # หากมี 'target' อยู่:
    if target:
        # โจมตี 'target'
        hero.attack(target)
        # จากนั้นย้ายไปที่เครื่องหมายสีแดง
        hero.moveXY(32, 17)
    pass

while True:
    enemy = hero.findNearestEnemy()
    hitOrHide(enemy)
