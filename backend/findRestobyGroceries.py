dictionaryStore={"Marche Murugan":["pineapple","chicken","apple"]} #instead of accessing index, access store name
dictionaryResto={""}

def findRestobyGroceries(grocery):
    list=[]
    for resto in dictionaryStore:
        if grocery in dictionaryStore[resto]:
            list.append(resto)
    #test
    return list 
    
#[{name:restoName,latitude:number,longitude:numberTwo},{name:restoName,latitude:number,longitude:numberTwo}]

if __name__ == "__main__":
    print(findRestobyGroceries("pineapple"))