# scrieti o clasa Shape

# care are o metoda arie

# scrieti o clasa Circle care mosteneste Shape si suprascrie metoda arie

# scrieti o clasa Square care mosteneste Shape si suprascrie metoda arie


class Shape:

    def aria():
        pass

class Circle(Shape):

    def aria(raza):
        print("Raza: ", end="")
        print(3.14 * raza ** 2)

class Square(Circle):

    def aria(latura):
        print("Latura: ", end="")
        print( latura ** 2)

sh = Shape
sq = Square
ci = Circle

print(sq.mro())

sh.aria()
ci.aria(15)
sq.aria(10)