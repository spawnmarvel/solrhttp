def generate_test_data():
    try:
        with open("testData.txt", "w") as f:
            for x in range(0,2000):
                plant = ""
                if x < 500:
                    plant = "System 1"
                elif x > 501 and x < 1000:
                    plant = "System 2"
                elif x > 1001 and x < 1500:
                    plant = "System 3"
                else:
                    plant = "System 4"
                
                obj = "" + str(x) + ";" + "Item-" + str(x) + ";" + str("Description of " + str(x) + ";"+ plant + "\n")
                f.write(obj)
        print("Test data generated")
    except Exception as ex:
        print(ex)
    


generate_test_data()