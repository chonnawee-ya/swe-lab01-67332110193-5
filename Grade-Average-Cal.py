def calculate_grade(scores):
    # 1. ตรวจสอบว่าข้อมูลที่ส่งมาเป็น List หรือไม่
    if not isinstance(scores, list):
        return "Error: ข้อมูลต้องอยู่ในรูปแบบ list", None

    # 2. ตรวจสอบว่าลิสต์ว่างหรือไม่ (ป้องกัน ZeroDivisionError)
    if len(scores) == 0:
        return "Error: ไม่มีคะแนนในลิสต์", 0

    total = 0
    for score in scores:
        # 3. ตรวจสอบว่าสมาชิกแต่ละตัวเป็นตัวเลขหรือไม่ (ป้องกัน TypeError)
        if not isinstance(score, (int, float)):
            return f"Error: พบข้อมูลที่ไม่ใช่ตัวเลข ({score})", None
        
        # 4. ตรวจสอบว่าคะแนนอยู่ในช่วง 0-100 หรือไม่ (Logical Error)
        if score < 0 or score > 100:
            return f"Error: คะแนนต้องอยู่ระหว่าง 0-100 เท่านั้น ({score})", None
            
        total = total + score

    average = total / len(scores)

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    return grade, average

# --- ส่วนนี้เหมือนกับ code แรกที่คุณให้มา ---
scores = [85, 92, 78, 88, 95]
print(calculate_grade(scores))
