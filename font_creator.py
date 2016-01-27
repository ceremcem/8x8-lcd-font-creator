__author__ = 'ceremcem'

# -*- coding: utf-8 -*-
__author__ = 'ceremcem'

from aktos_dcs import *
from aktos_dcs_lib import Qt
Qt.initialize()

class MainWindow(Actor, Qt.QtGui.QMainWindow):
    def __init__(self):
        Qt.QtGui.QMainWindow.__init__(self)
        Actor.__init__(self)
        self.ui = Qt.loadUI('font-creator.ui')

        for i in self.get_pixels("pixel"):
            getattr(self.ui, i).clicked.connect(self.pixel_handler)

        self.ui.generate_font.clicked.connect(self.generate_font)
        self.ui.clear_all.clicked.connect(self.clear_all)

    def clear_all(self):
        for i in self.get_pixels("pixel"):
            getattr(self.ui, i).setCheckState(Qt.QtCore.Qt.CheckState.Unchecked)


    def pixel_handler(self):
        for i in self.get_pixels("pixel"):
            click_state = getattr(self.ui, i).checkState()
            if click_state == Qt.QtCore.Qt.CheckState.Checked:
                pass
            led = getattr(self.ui, i.replace("pixel", "led"))

    def get_pixels(self, prefix):
        return ["%s_%d_%d" % (prefix, i, j) for i in range(1, 9) for j in range(1, 9)]

    def generate_font(self):
        # Structure:
        # - each font is a list of 256 characters
        # - each character represented as an 8x8 binary bitmap:
        # - each character's data comprises an 8-byte list
        # - each byte represents one column of the character
        # - the bytes are in column order left-to-right
        # - the bits in each byte are in row order: MSB (bottom row)
        #     to LSB (top row)
        # - some fonts only have non-zero (ie non-blank) data for
        #     characters in the range 0x20 to 0x7F
        font_data = [0] * 8
        for i in self.get_pixels("pixel"):
            _, x, y = i.split("_")
            x = int(x) - 1
            y = int(y) - 1
            bit = 1 << y
            click_state = getattr(self.ui, i).checkState()
            if click_state == Qt.QtCore.Qt.CheckState.Checked:
                try:
                    font_data[x] |= bit
                except:
                    font_data[x] = bit

        print "result: ", font_data
        import json
        char_map = json.dumps(font_data)
        char_name = self.ui.char_input.text()
        self.ui.font_output.setPlainText("    \"%s\": %s," % (char_name, char_map))



if __name__ == "__main__":
    import sys
    app = Qt.QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.ui.show()
    Qt.greenlet_exec(app)
