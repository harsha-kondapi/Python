class Student:
    def __init__(self,m1,m2):
        """
        docstrings
        :param m1:
        :param m2:
        """
        self._m1 = m1
        self._m2 = m2



    def __add__(self,other):
        """
        method overlading

        :param other:
        :return:
        """
        _t1 = self._m1 + other._m1
        _t2 = self._m2 + other._m2
        s3 = Student(_t1,_t2)
        return s3

    def __str__(self):
        """

        :return:
        """
        return f"({self._m1},{self._m2})"


s1 = Student(29,59)
s2 = Student(20,30)

s3 = s1 + s2

print(s3)




