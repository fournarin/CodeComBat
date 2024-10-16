# สัตว์เลี้ยงจะต้องชนะการแข่งขันเท่านั้น
# นักแข่งควรแตะเครื่องหมายของทีมแล้ววิ่งกลับ

def onHear(event):
    referee = pet.findNearestByType("wizard")
    # หากผู้ตัดสินเป็นผู้พูดและข้อความคือ "Start"
    if event.speaker == referee and event.message == "Start":
        # ให้สัตว์เลี้ยงวิ่งไปที่เครื่องหมายสีแดง
        pet.moveXY(54, 27)
        # จากนั้นให้วิ่งกลับ
        pet.moveXY(6, 27)

# กำหนดฟังก์ชัน onHear เพื่อจัดการอีเวนท์ "hear"
pet.on("hear", onHear)
