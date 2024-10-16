# อย่าโจมตีพวกเบิร์ล!
# ฟังก์ชันสามารถคืนค่าได้
# เมื่อเรียกใช้ฟังก์ชัน จะเท่ากับค่าที่ฟังก์ชันส่งคืน

def shouldAttack(target):
    # return False ถ้าไม่มี `target`
    if target:
        if target.type == "burl":
            return False
        else:
            return True
    # return False ถ้า target.type == "burl"
    # อย่างนั้น return True
    else:
        return False

while True:
    enemy = hero.findNearestEnemy()
    # เราใช้ shouldAttack() เพื่อตัดสินใจว่าเราควรโจมตีหรือไม่!
    # heroShouldAttack จะได้รับค่าเดียวกับที่ shouldAttack() ส่งคืน!
    heroShouldAttack = shouldAttack(enemy)
    if heroShouldAttack:
        hero.attack(enemy)