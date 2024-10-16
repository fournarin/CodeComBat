# คุณไม่สามารถช่วยชาวบ้านข้ามแม่น้ำได้
# แต่มีแค่สัตว์เลี้ยงของคุณเท่าที่ทำได้!
# สอนหมาป่าของคุณให้เป็นสุนัขอารักขา

def onSpawn(event):
    while True:
        # สัตว์เลี้ยงสามารถหาศัตรูได้เช่นกัน
        enemy = pet.findNearestEnemy()
        # หากมีศัตรู
        if enemy:
            # ให้สัตว์เลี้ยงพูดอะไรบางอย่าง
            pet.say("run bitch RUNNNN")

pet.on("spawn", onSpawn);
