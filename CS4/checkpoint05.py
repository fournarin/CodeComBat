# while-loops จะทำไปเรื่อยๆ จนกว่าเงื่อนไขจะเป็นเท็จ

ordersGiven = 0
while ordersGiven < 5:
    # เลื่อนลงมา 10 เมตร
    hero.moveXY(hero.pos.x, hero.pos.y -10)
    # สั่งให้พันธมิตรของคุณ "Attack!" กับ hero.say
    # พวกเขาสามารถได้ยินคุณได้ก็ต่อเมื่อคุณอยู่บน X
    hero.say("Attack!")

    # อย่าลืมเพิ่มคำสั่ง ordersGiven!
    ordersGiven +=1

while True:
    enemy = hero.findNearestEnemy()
    # เมื่อคุณออกคำสั่งเสร็จแล้ว ให้เข้าร่วมการโจมตี
    hero.attack(enemy)