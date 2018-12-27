class PFx_Font:

   def __init__(self,bitmap,index,glyph):
     self.bitmap=bitmap
     self.index=index
     self.glyph=glyph
     self.current_char=0
     self.current_glyph=glyph[0]

   def setPosition(self, utf8_char):
       if  utf8_char in self.index:
          self.current_char=  self.index[utf8_char]
       else:
          self.current_char=  self.index[" "]
       self.current_glyph= self.glyph[self.current_char]
       self.position= self.current_glyph[0]*8

   def getBit(self, position):
       c_offset = (position // 8)
       c_bit =  128 >> (position % 8)
       c_flag = (self.bitmap[c_offset] & c_bit ) != 0
#       print("pos",position," off ",c_offset," bit ",c_bit," flag ",c_flag)
       return c_flag

   def getNext(self):
#       print("Position ",self.position)
       flag = self.getBit(self.position)
       self.position= self.position + 1
       return flag




