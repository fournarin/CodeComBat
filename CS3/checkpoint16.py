# คุณติดอยู่ อย่าขยับ เดี๋ยวจะเจ็บเสียเปล่าๆ

# ฟังก์ชันนี้จะตรวจสอบว่าศัตรูอยู่ในระยะการโจมตีของคุณหรือไม่
def inAttackRange(enemy):
    distance = hero.distanceTo(enemy)
    # ดาบเกือบทั้งหมดมีระยะโจมตีที่ 3
    if distance <= 3:
        return True
    else:
        return False

# ยักษ์โจมตีก็ต่อเมื่อพวกมันอยู่ในระยะเอื้อมถึงเท่านั้น
while True:
    # ค้นหาศัตรูที่ใกล้ที่สุดและเก็บไว้ในตัวแปร
    enemy = hero.findNearestEnemy()
    # เรียก inAttackRange(ศัตรู) โดยให้ศัตรูเป็นอาร์กิวเม็นต์
    # และบันทึกผลลัพธ์ในตัวแปร canAttack
    canAttack = inAttackRange(enemy)
    # หากผลลัพธ์ที่เก็บไว้ใน canAttack คือ True, จากนั้นจู่โจม!
    if canAttack == True:
       hero.attack(enemy)
    pass