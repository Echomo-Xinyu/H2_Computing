class a():
    def x(self):
        return "a.x"

    def y(self):
        return "a.y"

    def z(self):
        return "a.z"


class b(a):
    def y(self):
        return "b.y"

    def z(self):
        return super().z()


class c(b):
    def x(self):
        return "c.x"

    def z(self):
        super().z()


aaa = a()
bbb = b()
ccc = c()
print(bbb.z())
