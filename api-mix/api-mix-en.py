def mainMenu():
    print("--------------------------------------------")
    print("-------   API mix program  V.1.0  ----------")
    print("-----------   for Panorient   --------------")
    print("--------------------------------------------")
    print("1. mix crudeoil 2 well")
    print("2. mix crudeoil 3 well")
    print("3. mix crudeoil 4 well")
    print("4. exit")
    print("--------------------------------------------")
    print("*use to mix api measurement crudeoil to sell")
    print("Develop by Jirayu B.")
    print("--------------------------------------------")

    while True:
        try:
            selection=int(input("choose menu: "))

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
                print("Type number 1-3 only !")
                mainMenu()
                mainMenu()
            
        except ValueError:
                print("Type number 1-3 only !")

def watermix_1():
    tank1_volume = float(input("<Tank1> put volume of crudeoil : "))
    tank1_api = float(input("<Tank1> put API : "))

    tank2_volume = float(input("<Tank2> put volume of crudeoil : "))
    tank2_api = float(input("<Tank2> put API : "))

    cal_1 = tank1_volume * tank1_api
    cal_2 = tank2_volume * tank2_api

    cal1_2 = cal_1+cal_2
    water_mix = tank1_volume + tank2_volume
    api_mix_total = cal1_2 / water_mix

    print(f"Total of API to mix is {api_mix_total}  ")
    anykey=input("Anykey to homepage")


def watermix_2():
    #for mix 3 well
    tank1_volume = float(input("<Tank1> put volume of crudeoil : "))
    tank1_api = float(input("<Tank1> put API : "))

    tank2_volume = float(input("<Tank2> put volume of crudeoil : "))
    tank2_api = float(input("<Tank2> put API : "))

    tank3_volume = float(input("<Tank3> put volume of crudeoil : "))
    tank3_api = float(input("<Tank3> put API : "))

    cal_1 = tank1_volume * tank1_api
    cal_2 = tank2_volume * tank2_api
    cal_3 = tank3_volume * tank3_api

    cal_mix = cal_1+cal_2+cal_3
    water_mix = tank1_volume + tank2_volume
    api_mix_total = cal_mix / water_mix

    print(f"Total of API to mix is {api_mix_total}  ")
    anykey=input("Anykey to homepage")

def watermix_3():
    #for mix 4 well
    tank1_volume = float(input("<Tank1> put volume of crudeoil : "))
    tank1_api = float(input("<Tank1> put API : "))

    tank2_volume = float(input("<Tank2> put volume of crudeoil : "))
    tank2_api = float(input("<Tank2> put API : "))

    tank3_volume = float(input("<Tank3> put volume of crudeoil : "))
    tank3_api = float(input("<Tank3> put API : "))

    tank4_volume = float(input("<Tank4> put volume of crudeoil : "))
    tank4_api = float(input("<Tank4> put API : "))

    cal_1 = tank1_volume * tank1_api
    cal_2 = tank2_volume * tank2_api
    cal_3 = tank3_volume * tank3_api
    cal_4 = tank4_volume * tank4_api

    cal_mix = cal_1+cal_2+cal_3+cal_4
    water_mix = tank1_volume + tank2_volume
    api_mix_total = cal_mix / water_mix

    print(f"Total of API to mix is {api_mix_total} ")

mainMenu()