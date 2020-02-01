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
                mainMenu()

            elif selection == 2:
                watermix_2()
                mainMenu()
                
            if selection == 3:
                watermix_3()
                mainMenu()

            elif selection == 4:
                break
            else:
                print("ใส่ตัวเลข 1-3 เท่านั้น")
                mainMenu()
                mainMenu()
            
        except ValueError:
                print("ใส่ตัวเลข 1-3 เท่านั้น")

def watermix_1():
    tank1_volume = float(input("เเท้งที่1 ใส่จำนวนบาเรลในนี้: "))
    tank1_api = float(input("เเท้งที่ 1 ใส่ค่า API : "))

    tank2_volume = float(input("เเท้งที่2 ใส่จำนวนบาเรลในนี้: "))
    tank2_api = float(input("เเท้งที่2 ใส่ค่า API : "))

    cal_1 = tank1_volume * tank1_api
    cal_2 = tank2_volume * tank2_api

    cal1_2 = cal_1+cal_2
    water_mix = tank1_volume + tank2_volume
    api_mix_total = cal1_2 / water_mix

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

    cal_1 = tank1_volume * tank1_api
    cal_2 = tank2_volume * tank2_api
    cal_3 = tank3_volume * tank3_api

    cal_mix = cal_1+cal_2+cal_3
    water_mix = tank1_volume + tank2_volume
    api_mix_total = cal_mix / water_mix

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

    cal_1 = tank1_volume * tank1_api
    cal_2 = tank2_volume * tank2_api
    cal_3 = tank3_volume * tank3_api
    cal_4 = tank4_volume * tank4_api

    cal_mix = cal_1+cal_2+cal_3+cal_4
    water_mix = tank1_volume + tank2_volume
    api_mix_total = cal_mix / water_mix

    print(f"ค่า API ที่ผสมกันได้เท่ากับ {api_mix_total}  นะจ๊ะ")

mainMenu()