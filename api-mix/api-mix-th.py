from blend import calculate_blend


def mainMenu():
    print("-----------------------------------------")
    print("-------   โปรเเกรม มิกซ์น้ำมัน V.1.0  -------")
    print("-----------   for Panorient   -----------")
    print("-----------------------------------------")
    print("1. มิกซ์น้ำมัน 2 หลุม")
    print("2. มิกซ์น้ำมัน 3 หลุม")
    print("3. มิกซ์น้ำมัน 4 หลุม")
    print("4. ออกจากโปรเเกรม")
    print("-----------------------------------------")
    print("*ใช้สำหรับ ผสมน้ำมันเพื่อหาสัดส่วน API เพื่อขาย")
    print("Develop by Jirayu B.")
    print("-----------------------------------------")

    while True:
        try:
            selection=int(input("เลือกเมนู: "))

            if selection == 1:
                watermix_1()

            elif selection == 2:
                watermix_2()

            elif selection == 3:
                watermix_3()

            elif selection == 4:
                break
            else:
                print("ใส่ตัวเลข 1-4 เท่านั้น")

        except ValueError:
                print("ข้อมูลไม่ถูกต้อง: กรอกตัวเลขที่มีค่าจำกัด ปริมาตรไม่ติดลบ และปริมาตรรวมมากกว่า 0")

def watermix_1():
    tank1_volume = float(input("เเท้งที่1 ใส่จำนวนบาเรลในนี้: "))
    tank1_api = float(input("เเท้งที่ 1 ใส่ค่า API : "))

    tank2_volume = float(input("เเท้งที่2 ใส่จำนวนบาเรลในนี้: "))
    tank2_api = float(input("เเท้งที่2 ใส่ค่า API : "))

    _, api_mix_total = calculate_blend([(tank1_volume, tank1_api), (tank2_volume, tank2_api)])

    print(f"ค่า API ที่ผสมกันได้เท่ากับ {api_mix_total}  นะจ๊ะ")
    anykey=input("กด enter เพื่อไปหน้าเเรก")


def watermix_2():
    #for mix 3 well
    tank1_volume = float(input("เเท้งที่1 ใส่จำนวนบาเรลในนี้: "))
    tank1_api = float(input("เเท้งที่ 1 ใส่ค่า API: "))

    tank2_volume = float(input("เเท้งที่2 ใส่จำนวนบาเรลในนี้: "))
    tank2_api = float(input("เเท้งที่2 ใส่ค่า API: "))

    tank3_volume = float(input("เเท้งที่3 ใส่จำนวนบาเรลในนี้: "))
    tank3_api = float(input("เเท้งที่3 ใส่ค่า API: "))

    _, api_mix_total = calculate_blend([(tank1_volume, tank1_api), (tank2_volume, tank2_api), (tank3_volume, tank3_api)])

    print(f"ค่า API ที่ผสมกันได้เท่ากับ {api_mix_total}  นะจ๊ะ")
    anykey=input("กด enter เพื่อไปหน้าเเรก")

def watermix_3():
    #for mix 4 well
    tank1_volume = float(input("เเท้งที่1 ใส่จำนวนบาเรลในนี้: "))
    tank1_api = float(input("เเท้งที่ 1 ใส่ค่า API : "))

    tank2_volume = float(input("เเท้งที่2 ใส่จำนวนบาเรลในนี้: "))
    tank2_api = float(input("เเท้งที่2 ใส่ค่า API : "))

    tank3_volume = float(input("เเท้งที่3 ใส่จำนวนบาเรลในนี้"))
    tank3_api = float(input("เเท้งที่3 ใส่ค่า API : "))

    tank4_volume = float(input("เเท้งที่4 ใส่จำนวนบาเรลในนี้"))
    tank4_api = float(input("เเท้งที่4 ใส่ค่า API : "))

    _, api_mix_total = calculate_blend([(tank1_volume, tank1_api), (tank2_volume, tank2_api), (tank3_volume, tank3_api), (tank4_volume, tank4_api)])

    print(f"ค่า API ที่ผสมกันได้เท่ากับ {api_mix_total}  นะจ๊ะ")

mainMenu()
