import random

description = ["Valve", "AntiSurge", "Pump", "Monitor", "Transformator", "Door", "Fan", "Turbin""Engine","Fuel","Gas","Oil","Temperatur","Heat","Pressure","Force"]
area = ["Area","Level","Floor","Housing","Smoke","Fire","Water","Ice", "Gate", "Low", "High"]

def generate_test_data():
    global description
    global area
    try:
        with open("testData.txt", "w") as f:
            for x in range(0,10000):
                random_desc = generate_random(description)
                random_area = generate_random(area)
                plant = ""
                if x < 2000:
                    plant = "System 1"
                elif x > 2001 and x < 4000:
                    plant = "System 2"
                elif x > 4001 and x < 6000:
                    plant = "System 3"
                else:
                    plant = "System 4"
                
                obj = "" + str(x) + ";" + "Item-" + str(x) + ";" + str(random_desc + " " + random_area + " " + str(x) + ";"+ plant + "\n")
                f.write(obj)
        print("Test data generated")
    except Exception as ex:
        print(ex)
    
def generate_random(list_data):
    ran = random.randint(0, len(list_data) -1)
    rv = list_data[ran]
    return rv

def main():
    generate_test_data()

if __name__ == "__main__":
    main()
