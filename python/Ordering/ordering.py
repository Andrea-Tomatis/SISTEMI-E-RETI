#list ordering

def selection(list):
    for k in range (len(list)):
        kmin = k
        for j in range (k+1,len(list)):
            if(int(list[kmin]) > int(list[j])):
                kmin = j
        if kmin != k:
            list[k],list[kmin] = list[kmin],list[k]

def createList():
    list = []
    k = input("insert the dimension of the list: ")
    for i in range (int(k)):
        list.append(input("insert an element: ")) 
    return list 


def main(list = createList()):
    print(f"la lista non invertita e' {list}")
    selection(list)
    print(f"la lista invertita e' {list}")


if __name__ == "__main__":
    main()
