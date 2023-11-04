import csv


def Show(file, parameter = "top", quantity = 5, separator = ","):
    reader = list(csv.reader(file))
    header = reader.pop(0)
    print(f'{separator} '.join(header))
    
    
    if quantity < 5:
        
        if parameter == "top":        
            for row in reader:
                print(f'{separator} '.join(row))     
                  
        elif parameter == "bottom":
            for row in reversed(reader):
                print(f'{separator} '.join(row))
                
        elif parameter == "random":
            import random
            random_list = reader
            random.shuffle(random_list)
            for row in random_list: 
                print(f'{separator} '.join(row))
        print("Было указано недостаточное кол-во строк, вывел все.")
        exit() 
        
           
    i = 0    
    
    if parameter == "top":        
        for row in reader:
            print(f'{separator} '.join(row))
            i += 1
            if i == quantity:
                break 
                  
    elif parameter == "bottom":
        for row in reversed(reader):
            print(f'{separator} '.join(row))
            i += 1
            if i == quantity:
                break
            
    elif parameter == "random":
        import random
        for row in random.sample(reader, quantity):
            print(f'{separator} '.join(row))
            i += 1
            if i == quantity:
                break
    else:
        print(f'Параметр {parameter} не распознан')


def Info(file):
    rows = list(csv.reader(file))
    header = rows.pop(0)
    non_empty_rows = list(x for x in rows if x != [])
    count_of_non_empty_rows = len(non_empty_rows)
    print("Количество строк с данными на количество столбцов:")
    print(f"{count_of_non_empty_rows}x{len(header)}")   
        
        
    
csvfile = open("final_1_stage/data.csv", "r", encoding = "utf-8")
#csvfile = open("final_1_stage/data.csv", "r", encoding = "utf-8")
Show(csvfile, parameter = "random", quantity = 5, separator = ",")
Info(csvfile)