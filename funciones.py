def stock_marca(productos,stock,marca):
    e=False
    t=0
    for n,i in productos.items():
        for p,v in stock.items():
            if marca==i[0] and p==n:
                e=True
                t+=v[1]
    if not e:
        print("No existe esa marca")
    else:
        print(f"El total de stock de la marca {marca} es {t}")
def busqueda_precio(productos,stock,p1,p2):
    t=[]
    e=False
    for n,i in productos.items():
        for p,v in stock.items():
            if p1 <= v[0] <= p2 and v[1] !=0 and n==p:
                e=True
                t.append((n,i))
    orden=sorted(t,key= lambda x:x[1][0])
    if not e:
        print("No hay notebooks en ese rango de precios")
    else:
        for n,i in orden:
            print(f"{i[0]}|{n}")
def actualizar_precio(productos,stock,modelo,precio):
    e=False
    for n,i in productos.items():
        for p,v in stock.items():
            if modelo==n:
                e=True
                stock[modelo][0]=precio
    if not e:
        print("El modelo no existe")
        return False
    else:
        print("Precio Actualizado")
        return True
    
                
                
                
                
                
                
                
                
    
        
                
        
    
        
        
    
    
