def enemyInRange(enemy):
    # คืนค่าเป็น true หากศัตรูอยู่ห่างออกไปน้อยกว่า 5 ยูนิต
    distance = hero.distanceTo(enemy)
    if distance < 5:
        return True
    else:
        return False

def cleaveOrAttack(enemy):
    if hero.isReady('cleave'):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # ตรวจสอบระยะทางของศัตรูโดยการเรียก enemyInRange
        if enemyInRange(enemy):
            cleaveOrAttack(enemy)