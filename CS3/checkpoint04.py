# ย้ายไปที่ 'Laszlo' และรับหมายเลขลับของเขา
hero.moveXY(30, 13)
las = hero.findNearestFriend().getSecret()

# เพิ่ม 7 ไปที่หมายเลข 'Laszlo' เพื่อรับหมายเลข 'Erzsebet'
# ไปที่ 'Erzsebet' และพูดหมายเลขวิเศษของเธอ
erz = las + 7
hero.moveXY(17, 26)
hero.say(erz)

# หารจำนวน 'Erzsebet' ด้วย 4 เพื่อรับ หมายเลขของ 'Simonyi'
# ไปที่ 'Simonyi' และบอกหมายเลขของเขา
hero.moveXY(30, 39)
Si = erz /4
hero.say(Si)
# คูณหมายเลขของ 'Simonyi' ด้วย 'Laszlo's เพื่อรับ หมายเลขของ 'Agata'
Aga = Si * las
# ไปที่ 'Agata' และบอกหมายเลขของเธอ
hero.moveXY(43, 26)
hero.say(Aga)