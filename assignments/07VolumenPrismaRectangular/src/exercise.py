# Escribe aquí tus funciones...
def area_rectangulo(base,altura):
    return base*altura
def volumen_prisma(area,profundidad):
    return area*profundidad
def main():
    #escribe tu código abajo de esta línea
    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))
    p = float(input("Dame la profundidad: "))

    r = volumen_prisma(area_rectangulo(b,a),p)

    print("El volumen del prisma es:",r)

if __name__=='__main__':
    main()
