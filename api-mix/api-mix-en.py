from blend import calculate_blend


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

            elif selection == 2:
                watermix_2()

            elif selection == 3:
                watermix_3()

            elif selection == 4:
                break
            else:
                print("Type a number from 1 to 4.")

        except ValueError:
                print("Invalid input: use finite numbers, nonnegative volumes, and a positive combined volume.")

def watermix_1():
    tank1_volume = float(input("<Tank1> put volume of crudeoil : "))
    tank1_api = float(input("<Tank1> put API : "))

    tank2_volume = float(input("<Tank2> put volume of crudeoil : "))
    tank2_api = float(input("<Tank2> put API : "))

    _, api_mix_total = calculate_blend([(tank1_volume, tank1_api), (tank2_volume, tank2_api)])

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

    _, api_mix_total = calculate_blend([(tank1_volume, tank1_api), (tank2_volume, tank2_api), (tank3_volume, tank3_api)])

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

    _, api_mix_total = calculate_blend([(tank1_volume, tank1_api), (tank2_volume, tank2_api), (tank3_volume, tank3_api), (tank4_volume, tank4_api)])

    print(f"Total of API to mix is {api_mix_total} ")

mainMenu()
