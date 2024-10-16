# ดูเหมือนว่า Ogre Chieftain กำลังขโมยอัญมณีของคุณ!
# ใช้ปืนใหญ่สองกระบอกสำหรับเป้าหมายของคุณ

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        enemyPos = enemy.pos.x + " " + enemy.pos.y
        hero.say("ศัตรูอยู่ที่ " + enemyPos)
        
    # ตอนนี้คุณได้แก้แค้นที่แสนหวานแล้ว
    # ทำไมต้องเลือกอย่างเสียอย่างด้วยล่ะ?
    # ค้นหาตำแหน่งของไอเท็มและ
    item = hero.findNearestItem()
    if item:
        itempos = item.pos.x + " " + item.pos.y
        hero.say("ไอเทมอยู่ที่" +  itempos)
    # พูดเพื่อให้ปืนใหญ่ของคุณกำหนดเป้าหมาย