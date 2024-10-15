# อาร์เรย์นี้มีเพื่อนและยักษ์ผสมกนอยู่
# เอลเลมนท์คู่คือยักษ์ แต่ที่ต่างคือเพื่อน
everybody = ['Yetu', 'Tabitha', 'Rasha', 'Max', 'Yazul',  'Todd']
enemyIndex = 0

while enemyIndex < len(everybody):
    # ใช้วงเล็บเหลี่ยมเพื่อรับชื่อยักษ์จากอาร์เรย์
    ogreName = everybody[enemyIndex]
    # โจมตีโดยใช้ตัวแปรที่ถือชื่อยักษ์
    hero.say("I will attack " + ogreName)
    hero.attack(ogreName)
    # เพิ่มขึ้น 2 เพื่อข้ามผ่านเพื่อน
    enemyIndex += 2

# หลังจากเอาชนะยักษ์ได้แล้ว ให้ย้ายไปที่โอเอซิส
hero.moveXY(36, 42)