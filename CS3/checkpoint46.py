# ให้ไปขอความช่วยเหลือจากผู้รักษาเมื่อคุณมีพลังชีวิตต่ำกว่าครึ่งหนึ่ง

while True:
    currentHealth = hero.health
    healingThreshold = hero.maxHealth / 2
    # หากพลังชีวิตปัจจุบันของคุณต่ำกว่าเกณฑ์
    # ไปยังจุดรักษาและพูดว่า "heal me".
    # มิฉะนั้นโจมตี คุณจะต้องต่อสู้อย่างหนัก!
    if hero.health < healingThreshold:
        hero.moveXY(65, 46)
        hero.say("Heal, please!")