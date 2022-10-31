import os
import sys



"""

"""

def pb1():
    print(extensii("C:/"))

def extensii (director) :
    extensii_list = set([])
    files = os.listdir(director)
    
    for file in files :
        for poz in range(len(file) - 1 , 0, -1):
            if (file[poz] == '.') :
                extensii_list.add(file[poz + 1:])
                break

    return sorted( extensii_list )


"""

"""
def pb2():
    print(director_records("D:\work\\bd\Learning\Python\Lab 4", "D:\work\\bd\Learning\Python\Lab 4\_2_records.txt"))

def director_records(director, fisier) :
    files_in_dir = os.listdir(director)
    files_record = open(fisier, "w")

    for file_in_dir in files_in_dir :
        cale = os.path.join(director, file_in_dir)
        if os.path.isfile(cale) == True :
            files_record.write(cale)
            files_record.write("\n")

    return
            

"""

"""

def pb3():
    print ( fisier_file("D:\work\\bd\Learning\Python\Lab 4") )

def fisier_file(my_path) :
    if os.path.isfile (my_path) :
        input_file = open(my_path, "r")
        data = input_file.read()

        return data[-20:]
    
    elif os.path.isdir (my_path) :
        extensions_dict = dict([])

        for (root, director, files) in os.walk(my_path) :
            for file in files :
                for poz in range(len(file) - 1, 0, -1) :
                    if (file[poz] == '.') :
                        
                        if (file[poz:] in extensions_dict) == False :
                            extensions_dict[file[poz:]] = 1
                        else :
                            extensions_dict[file[poz:]] += 1
                        break
        
        return extensions_dict




"""

"""

def pb4():

dictionar_extensii = dict([])

for file in os.listdir( sys.argv[1] ) :
    
    if os.path.isfile(file) :
        for poz in range( len(file) - 1, 0, -1) :
            
            
            if (file[poz] == '.') :
                if (file[poz:] in dictionar_extensii) == False :
                    dictionar_extensii[file[poz:]] = 1
                else :
                    dictionar_extensii[file[poz:]]  += 1
                break
print(dictionar_extensii)



"""

"""

def pb5():
    print (search_in_target("D:\work\\bd\Learning\Python\Lab 4", "def"))

def search_in_target (target, to_search) :

    files_containing = []
    
    if os.path.isfile(target) :

        data = open(target).read()
        if (data.count(to_search) != 0) : files_containing.append(target)

    elif os.path.isdir(target) :
        
        for (root, director, fisiere) in os.walk(target) :
            for fisier in fisiere :
                if os.path.isfile(os.path.join(root, fisier)) :
                    
                    data = open(os.path.join(root, fisier)).read()
                    if (data.count(to_search) != 0) : files_containing.append(os.path.join(root, fisier))
    else :
        raise ValueError(target)

    return files_containing

"""

"""

def pb6():
    print (search_in_target("D:\work\\bd\Learning\Python\Lab 4", "def", handle_exception) )

def search_in_target (target, to_search, callback) :

    files_containing = []
    
    if os.path.isfile(target) :

        data = open(target).read()
        if (data.count(to_search) != 0) : files_containing.append(target)

    elif os.path.isdir(target) :
        
        for (root, director, fisiere) in os.walk(target) :
            for fisier in fisiere :
                if os.path.isfile(os.path.join(root, fisier)) :
                    
                    data = open(os.path.join(root, fisier)).read()
                    if (data.count(to_search) != 0) : files_containing.append(os.path.join(root, fisier))
    else :
        callback( ValueError(target) )

    return files_containing


def handle_exception(err) :
    try :
        raise err
    except ValueError as e :
        print (e)

"""

"""

def pb7():
    print(file_caracteristics("D:\work\\bd\Learning\Python\Lab 4\_2_records.txt"))

def file_caracteristics (file_path) :
    caracteristics_dict = dict([])

    caracteristics_dict["full_path"] = os.path.abspath(file_path)
    caracteristics_dict["file_size"] = os.path.getsize(file_path)
    caracteristics_dict["file_exteson"] = os.path.splitext(file_path)[1]
    caracteristics_dict["can_read"] = os.access(file_path, os.W_OK)
    caracteristics_dict["can_write"] = os.access(file_path, os.R_OK)

    return caracteristics_dict

"""

"""

def pb8():
    print ( absolute_paths("D:\work\\bd\Learning\Python\Lab 4") )

def absolute_paths (root_path) :

    absolute_paths_list = []

    for file in os.listdir(root_path) :
        if os.path.isfile(file) :
            absolute_paths_list.append(os.path.abspath( os.path.join(root_path, file) ) ) 

    return absolute_paths_list

if __name__ == '__main__':

  print()
  print()

  print(" ------ ------ Problem 1 ------ -----")
  pb1()
  print()

  print(" ------ ------ Problem 2 ------ -----")
  pb2()
  print()

  print(" ------ ------ Problem 3 ------ -----")
  pb3()
  print()

  print(" ------ ------ Problem 4 ------ -----")
  pb4()
  print()

  print(" ------ ------ Problem 5 ------ -----")
  pb5()
  print()

  print(" ------ ------ Problem 6 ------ -----")
  pb6()
  print()

  print(" ------ ------ Problem 7 ------ -----")
  pb7()
  print()

  print(" ------ ------ Problem 8 ------ -----")
  pb8()
  print()
