# ไปที่ 'Zsofia' และรับหมายเลขลับจากเธอ
hero.moveXY(18, 20)
zso = hero.findNearestFriend().getSecret()

# หารตัวเลขของ 'Zsofia' ด้วย 4 เพื่อให้ได้ หมายเลขของ 'Mihaly'
# ไปที่ 'Mihaly' และพูดหมายเลขวิเศษของเขา
mih = zso / 4
hero.moveXY(30, 15)
hero.say(mih)

# หาร 'หมายเลขของ 'Mihaly' ด้วย 5 เพื่อรับ หมายเลขของ 'Beata'
Be = mih/5
# ไปที่ 'Beata' และพูดหมายเลขวิเศษของเธอ
hero.moveXY(42, 20)
hero.say(Be)
# ลบหมายเลข 'Beata' ออกจาก 'Mihaly' เพื่อรับหมายเลขของ Sandor
San = mih - Be
# ไปที่ 'Sandor' และพูดเลขวิเศษของเขา
hero.moveXY(38, 37)
hero.say(San)
