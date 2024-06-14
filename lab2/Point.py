# ^^^Implement class and functionality above (remember to include docstrings!)
# vvvImplement tests below
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __lt__(self, other):
        return self.dist_from_origin() < other.dist_from_origin()
        
    def __gt__(self, other ):
       return self.dist_from_origin() > other.dist_from_origin()
    
    def __eq__(self, other):
        return self.dist_from_origin() ==  other.dist_from_origin()
    
    def __str__(self):
        return 'Point(' + str(self.x) + ', ' + str(self.y) + ')'
    
    def dist_from_origin(self):
        return ((self.x**2)+(self.y**2))**.5


if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(5, 4)
    
    # p3 = Point(3, 3)
    # p4 = Point(3, 3)

    # All tests should use `assert`, not `print`
    
    ##### test init #####
    # assert correct x
    # assert correct y
    assert p1.x == 3
    assert p1.y == 4

    ##### test lt #####
    # Expected True (e.g `p1 < p2`)
    # Expected False (e.g. `not p1 < p2`)
    assert p1.x < p2.x
    assert not p1.y < p2.y

    ##### test gt #####
    # Expected True (e.g `p1 > p2`)
    # Expected False (e.g. `not p1 > p2`)
    assert p2.x > p1.x
    assert not p2.y > p1.y

    ##### test eq #####
    # Expected True (e.g `p1 == p2`)
    # Expected False (e.g. `not p1 == p2`)
    # p1 = Point(5, 3)
    assert p1.y == p2.y
    assert not p1.x == p2.x

    ##### test str #####
    # assert str(some_point) == expected_string
    expected_str = '(3, 4)'
    # expected_str = '3, 4'
    assert str(p1) == expected_str

    ##### test dist_from_origin() #####
    assert p1.dist_from_origin() == (25**0.5)


   