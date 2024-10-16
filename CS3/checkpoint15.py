# บอกพ่อมดถึงระยะทางของยักษ์ที่กำลังมา

# ฟังก์ชันนี้จะค้นหาศัตรูที่ใกล้ที่สุดและส่งกลับระยะทางไปยังศัตรู
# หากไม่มีศัตรู ฟังก์ชันจะคืนค่า 0
def nearestEnemyDistance():
    enemy = hero.findNearestEnemy()
    result = 0
    if enemy:
        result = hero.distanceTo(enemy)
    return result

while True:
    # เรียก nearestEnemyDistance() และ
    # บันทึกผลลัพธ์ในตัวแปร enemyDistance.
    enemyDistance = nearestEnemyDistance()
    # หาก enemyDistance  มากกว่า 0:
    if enemyDistance > 0:
        # บอกค่าของตัวแปร enemyDistance
        
        hero.say(enemyDistance)