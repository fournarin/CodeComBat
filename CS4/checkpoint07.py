# ล่อยักษ์เข้าไปซุ่มโจมตี!

# while ทองของคุณน้อยกว่า 25 ให้สะสมเหรียญ
while hero.gold <25 :
    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
# หลังลูป while ให้สร้าง "decoy" ที่ X สีขาว
hero.buildXY("decoy", 72, 68)
# ในขณะที่สุขภาพของคุณเท่ากับ maxHealth พูดคำดูถูก
while hero.health == hero.maxHealth:
    hero.say("WOW")
# จากนั้นกลับไปที่ X สีแดง
hero.moveXY(22, 15)