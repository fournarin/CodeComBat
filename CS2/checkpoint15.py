# มัสกิ้นกำลังโจมตี!
# ฝูงจะมาทุกช่วงเวลาที่กำหนด
# เมื่อใดก็ตามที่ทำได้ ใช้ cleave เพื่อกวาดล้างศัตรูเป็นกองๆ

while True:
    enemy = hero.findNearestEnemy()
    # ใช้ if-statement กับ isReady เพื่อตรวจสอบ "cleave":
    if hero.isReady("cleave"):
        # ฟาดเบิ้ม!
        hero.cleave(enemy)
    # มิฉะนั้น หาก cleave ยังไม่พร้อม:
    else:
        # โจมตีออร์คที่ใกล้ที่สุด!
        hero.attack(enemy)
