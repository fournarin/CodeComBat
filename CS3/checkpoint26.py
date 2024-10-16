# ยักษ์โอเกอร์กำลังโจมตีนิคมใกล้เคียง!
# แต่จงระวัง เพราะพวกยักษ์ได้หว่านยาพิษลงดินแล้ว
# รวบรวมเหรียญและปราบยักษ์ให้หมด แต่หลีกเลี่ยงเบิร์ลและยาพิษ!

while True:
    enemy = hero.findNearestEnemy()
    if enemy.type == "munchkin" or enemy.type == "thrower":
        hero.attack(enemy)
    item = hero.findNearestItem()
    # ตรวจสอบประเภทไอเท็มเพื่อให้แน่ใจว่าฮีโร่ไม่หยิบยาพิษ!
    # หากประเภทของรายการคือ "gem" หรือ "coin":
    if item.type == "gem" or item.type == "coin":
        # จากนั้นเคลื่อนที่และหยิบขึ้นมา:
        hero.moveXY(item.pos.x,item.pos.y)