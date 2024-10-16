# ชาวนาและคนธรรมดากำลังรวมตัวกันอยู่ในป่า
# สั่งให้ชาวนาสู้รบและคนอื่นๆ หนีไป!

while True:
    friend = hero.findNearestFriend()
    if friend:
        hero.say("ไปต่อสู้, " + friend.id + "!")
    # ตอนนี้หาศัตรูที่ใกล้ที่สุดและบอกให้พวกเขาหนีออกไป
    enemy = hero.findNearestEnemy()