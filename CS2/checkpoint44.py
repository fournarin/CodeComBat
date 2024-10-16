# สัตว์เลี้ยงของคุณสามารถใช้ pet.moveXY() ได้

def onSpawn(event):
    while True:
        # ขั้นแรก ย้ายไปที่เครื่องหมาย X ด้านซ้าย
        pet.moveXY(9, 24)
        # ถัดไป ย้ายไปที่เครื่องหมาย X ด้านบน
        pet.moveXY(30, 43)
        # ย้ายสัตว์เลี้ยงของคุณไปที่เครื่องหมาย Xด้านขวา
        pet.moveXY(51, 24)
        # ย้ายสัตว์เลี้ยงของคุณไปที่เครื่องหมาย X ด้านล่าง
        pet.moveXY(30, 5)

# ใช้ pet.on() เพื่อจัดการกับอีเวนท์ "spawn" ด้วย onSpawn
pet.on("spawn", onSpawn)

# เชียร์สัตว์เลี้ยงของคุณ!
# อย่าลบคำสั่งด้านล่าง
while True:
    hero.say("ดีมาก!")
    hero.say("คุณทำได้!")
    hero.say("วิ่ง วิ่ง วิ่งงง!")
    hero.say("ใกล้ถึงแล้ว!")
    hero.say("อีกรอบ!")
