# สัตว์เลี้ยงของคุณควรวิ่งไปมาบนเครื่องหมาย X
# ฮีโรต้องคอยเชียร์ไปตลอด!

# เขียนฟังก์ชันอีเวนท์บน onSpawn สำหรับสัตว์เลี้ยง
# ฟังก์ชั่นนี้ควรทำให้หมาป่าวิ่งไปมา
# ขั้นแรก ให้วิ่งไปที่เครื่องหมายทางขวา ตามด้วยเครื่องหมายทางซ้าย
def onSpawn (event):
    while True:
        pet.moveXY(48, 8)
        pet.moveXY(12, 8)

pet.on("spawn", onSpawn)
# เชียร์สัตว์เลี้ยงของคุณ อย่าลบสิ่งนี้
while True:
    hero.say("วิ่ง!!!")
    hero.say("เร็วขึ้น!")
