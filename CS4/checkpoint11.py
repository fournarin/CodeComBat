# เรียกชาวบ้านทีละคน

# ยูนิตเป็นกลางถูกตรวจพบว่าเป็นศัตรู
neutrals = hero.findEnemies()
while True:
    if len(neutrals):
        # พูดยูนิตแรกในอาร์เรย์เป็นกลาง
        hero.say(neutrals[0])
        pass
    else:
        hero.say("ไม่มีใครที่นี่")
    
    # กำหนดตัวแปรความเป็นกลางใหม่โดยใช้ findEnemies()
    neutrals = hero.findEnemies()