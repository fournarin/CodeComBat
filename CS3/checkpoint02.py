# คุณสามารถเพิ่มสตริงเข้าด้วยกันและเพิ่มตัวเลขลงในสตริงได้
# ร้องตามโดยใช้การต่อสตริง:
# X potions of health on the wall!
# X potions of health!
# Take Y down, pass it around!
# X-Y potions of health on the wall.

potionsOnTheWall = 10
numToTakeDown = 1
while True:
    hero.say(potionsOnTheWall + " potions of health on the wall!")
    # ร้องเพลงในบรรทัดถัดไป
    hero.say(potionsOnTheWall + " potions of health!")
    # ร้องเพลงในบรรทัดถัดไป
    hero.say("Take " + numToTakeDown + " down, pass it around")
    potionsOnTheWall -= numToTakeDown
    # ร้องเพลงบรรทัดสุดท้าย
    hero.say(potionsOnTheWall + " potions of health on the wall")