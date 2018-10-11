# This class is used to create grid layout
# 
# You can visit my repository at
# https://github.com/nutchun/PyCalculator
# 
# This project is a part of Software Development Practice 1 course
#
# Developed by Nuttakan Chuntra
# Computer Engineering student at KMUTNB
# Student ID: 5901012630032
# Bangkok, Thailand
# Email: nut.ch40@gmail.com


class GridLayout:
    """Create grid layout"""

    def __init__(self, objectlist, rect, spacing=0, merge=True):
        self.obj = objectlist
        self.rect = rect
        self.spacing = spacing
        self.merge = merge
        self.i = 0
        self.j = 0

    def getIndex(self):
        """Return pair of indexes of elements in generate method"""
        return self.i, self.j
    
    def generate(self):
        """Generate grids"""

        col = len(self.obj[0])
        row = len(self.obj)
        btn_width = (self.rect[2] - self.rect[0] - self.spacing * (col + 1)) / col
        btn_height = (self.rect[3] - self.rect[1] - self.spacing * (row + 1)) / row

        # generate grids
        self.i = 0
        while self.i < row:
            self.j = 0
            while self.j < col:
                
                b = self.obj[self.i][self.j]

                if self.i > 0 and self.obj[self.i - 1][self.j] == b and self.merge:
                    self.j += 1
                    yield None
                    continue
                
                xstep = self.spacing + (btn_width + self.spacing) * self.j
                ystep = self.spacing + (btn_height + self.spacing) * self.i
                rowspan = 1
                colspan = 1

                if self.merge:
                    for csp in range(self.j + 1, col):
                        if self.obj[self.i][csp] != b:
                            break
                        colspan += 1
                    
                    for rsp in range(self.i + 1, row):
                        if self.obj[rsp][self.j] != b:
                            break
                        rowspan += 1
                
                new_btn_width = btn_width * colspan + self.spacing * (colspan - 1)
                new_btn_height = btn_height * rowspan + self.spacing * (rowspan - 1)

                yield self.rect[0] + xstep, self.rect[1] + ystep, new_btn_width, new_btn_height

                self.j += colspan
                
            self.i += 1
