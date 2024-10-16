# พวกออร์คกำลังพยายามขโมยเหรียญ!
# เขียนฟังก์ชั่นเพื่อจัดการมันก่อนที่จะโดนพวกมันขโมยเหรียญไป

def pickUpCoin():
    coin = hero.findNearestItem()
    if coin:
        hero.moveXY(coin.pos.x, coin.pos.y)

# เขียนฟังก์ชั่น attackEnemy ด้านล่าง
# ค้นหาศัตรูที่อยู่ใกล้ที่สุดและโจมตีมัน!
def findandkill():
    enemy = hero.findNearestEnemy()
    if enemy:
        if hero.isReady("cleave"):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)

while True:
    findandkill()
    pickUpCoin()
    
