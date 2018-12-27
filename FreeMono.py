from PFx_Font import PFx_Font
class FreeMono12pt8b(PFx_Font):

    def __init__(self):
        super().__init__(self.bitmap,self.index,self.glyph)

    bitmap=bytes([
      0x03, 0x00, 0xC0, 0x30, 0x04, 0x00, 0x01, 0xFF, 0x90, 0x12, 0x02, 0x40,
      0x08, 0x01, 0x10, 0x3E, 0x04, 0x40, 0x80, 0x10, 0x02, 0x01, 0x40, 0x28,
      0x07, 0xFF, 0x80, 0x1E, 0x48, 0x74, 0x05, 0x01, 0x80, 0x20, 0x08, 0x02,
      0x00, 0x80, 0x20, 0x04, 0x01, 0x01, 0x30, 0x87, 0xC0, 0x49, 0x24, 0x92,
      0x48, 0x01, 0xF8, 0xE7, 0xE7, 0x67, 0x42, 0x42, 0x42, 0x42, 0x09, 0x02,
      0x41, 0x10, 0x44, 0x11, 0x1F, 0xF1, 0x10, 0x4C, 0x12, 0x3F, 0xE1, 0x20,
      0x48, 0x12, 0x04, 0x81, 0x20, 0x48, 0x04, 0x07, 0xA2, 0x19, 0x02, 0x40,
      0x10, 0x03, 0x00, 0x3C, 0x00, 0x80, 0x10, 0x06, 0x01, 0xE0, 0xA7, 0xC0,
      0x40, 0x10, 0x04, 0x00, 0x3C, 0x19, 0x84, 0x21, 0x08, 0x66, 0x0F, 0x00,
      0x0C, 0x1C, 0x78, 0x01, 0xE0, 0xCC, 0x21, 0x08, 0x43, 0x30, 0x78, 0x3E,
      0x30, 0x10, 0x08, 0x02, 0x03, 0x03, 0x47, 0x14, 0x8A, 0x43, 0x11, 0x8F,
      0x60, 0xFD, 0xA4, 0x90, 0x05, 0x25, 0x24, 0x92, 0x48, 0x92, 0x24, 0x11,
      0x24, 0x89, 0x24, 0x92, 0x92, 0x90, 0x00, 0x04, 0x02, 0x11, 0x07, 0xF0,
      0xC0, 0x50, 0x48, 0x42, 0x00, 0x08, 0x04, 0x02, 0x01, 0x00, 0x87, 0xFC,
      0x20, 0x10, 0x08, 0x04, 0x02, 0x00, 0x3B, 0x9C, 0xCE, 0x62, 0x00, 0xFF,
      0xE0, 0xFF, 0x80, 0x00, 0x80, 0xC0, 0x40, 0x20, 0x20, 0x10, 0x10, 0x08,
      0x08, 0x04, 0x04, 0x02, 0x02, 0x01, 0x01, 0x00, 0x80, 0x80, 0x40, 0x00,
      0x1C, 0x31, 0x90, 0x58, 0x38, 0x0C, 0x06, 0x03, 0x01, 0x80, 0xC0, 0x60,
      0x30, 0x34, 0x13, 0x18, 0x70, 0x30, 0xE1, 0x44, 0x81, 0x02, 0x04, 0x08,
      0x10, 0x20, 0x40, 0x81, 0x1F, 0xC0, 0x1E, 0x10, 0x90, 0x68, 0x10, 0x08,
      0x0C, 0x04, 0x04, 0x04, 0x06, 0x06, 0x06, 0x06, 0x0E, 0x07, 0xFE, 0x3E,
      0x10, 0x40, 0x08, 0x02, 0x00, 0x80, 0x40, 0xE0, 0x04, 0x00, 0x80, 0x10,
      0x04, 0x01, 0x00, 0xD8, 0x63, 0xE0, 0x06, 0x0A, 0x0A, 0x12, 0x22, 0x22,
      0x42, 0x42, 0x82, 0x82, 0xFF, 0x02, 0x02, 0x02, 0x0F, 0x7F, 0x20, 0x10,
      0x08, 0x04, 0x02, 0xF1, 0x8C, 0x03, 0x00, 0x80, 0x40, 0x20, 0x18, 0x16,
      0x18, 0xF0, 0x0F, 0x8C, 0x08, 0x08, 0x04, 0x04, 0x02, 0x79, 0x46, 0xC1,
      0xE0, 0x60, 0x28, 0x14, 0x19, 0x08, 0x78, 0xFF, 0x81, 0x81, 0x02, 0x02,
      0x02, 0x02, 0x04, 0x04, 0x04, 0x04, 0x08, 0x08, 0x08, 0x08, 0x3E, 0x31,
      0xB0, 0x70, 0x18, 0x0C, 0x05, 0x8C, 0x38, 0x63, 0x40, 0x60, 0x30, 0x18,
      0x1B, 0x18, 0xF8, 0x3C, 0x31, 0x30, 0x50, 0x28, 0x0C, 0x0F, 0x06, 0x85,
      0x3C, 0x80, 0x40, 0x40, 0x20, 0x20, 0x63, 0xE0, 0xFF, 0x80, 0x07, 0xFC,
      0x39, 0xCE, 0x00, 0x00, 0x06, 0x33, 0x98, 0xC4, 0x00, 0x00, 0xC0, 0x60,
      0x18, 0x0C, 0x06, 0x01, 0x80, 0x0C, 0x00, 0x60, 0x03, 0x00, 0x30, 0x01,
      0x00, 0xFF, 0xF0, 0x00, 0x00, 0x0F, 0xFF, 0xC0, 0x06, 0x00, 0x30, 0x01,
      0x80, 0x18, 0x01, 0x80, 0xC0, 0x30, 0x18, 0x0C, 0x02, 0x00, 0x00, 0x3E,
      0x60, 0xA0, 0x20, 0x10, 0x08, 0x08, 0x18, 0x10, 0x08, 0x00, 0x00, 0x00,
      0x01, 0xC0, 0xE0, 0x1C, 0x31, 0x10, 0x50, 0x28, 0x14, 0x3A, 0x25, 0x22,
      0x91, 0x4C, 0xA3, 0xF0, 0x08, 0x02, 0x01, 0x80, 0x7C, 0x3F, 0x00, 0x0C,
      0x00, 0x48, 0x01, 0x20, 0x04, 0x40, 0x21, 0x00, 0x84, 0x04, 0x08, 0x1F,
      0xE0, 0x40, 0x82, 0x01, 0x08, 0x04, 0x20, 0x13, 0xE1, 0xF0, 0xFF, 0x08,
      0x11, 0x01, 0x20, 0x24, 0x04, 0x81, 0x1F, 0xC2, 0x06, 0x40, 0x68, 0x05,
      0x00, 0xA0, 0x14, 0x05, 0xFF, 0x00, 0x1E, 0x48, 0x74, 0x05, 0x01, 0x80,
      0x20, 0x08, 0x02, 0x00, 0x80, 0x20, 0x04, 0x01, 0x01, 0x30, 0x87, 0xC0,
      0xFE, 0x10, 0x44, 0x09, 0x02, 0x40, 0x50, 0x14, 0x05, 0x01, 0x40, 0x50,
      0x14, 0x0D, 0x02, 0x41, 0x3F, 0x80, 0xFF, 0xC8, 0x09, 0x01, 0x20, 0x04,
      0x00, 0x88, 0x1F, 0x02, 0x20, 0x40, 0x08, 0x01, 0x00, 0xA0, 0x14, 0x03,
      0xFF, 0xC0, 0xFF, 0xE8, 0x05, 0x00, 0xA0, 0x04, 0x00, 0x88, 0x1F, 0x02,
      0x20, 0x40, 0x08, 0x01, 0x00, 0x20, 0x04, 0x01, 0xF0, 0x00, 0x1F, 0x46,
      0x19, 0x01, 0x60, 0x28, 0x01, 0x00, 0x20, 0x04, 0x00, 0x83, 0xF0, 0x0B,
      0x01, 0x20, 0x23, 0x0C, 0x3E, 0x00, 0xE1, 0xD0, 0x24, 0x09, 0x02, 0x40,
      0x90, 0x27, 0xF9, 0x02, 0x40, 0x90, 0x24, 0x09, 0x02, 0x40, 0xB8, 0x70,
      0xFE, 0x20, 0x40, 0x81, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x81, 0x1F,
      0xC0, 0x0F, 0xE0, 0x10, 0x02, 0x00, 0x40, 0x08, 0x01, 0x00, 0x20, 0x04,
      0x80, 0x90, 0x12, 0x02, 0x40, 0xC6, 0x30, 0x7C, 0x00, 0xF1, 0xE4, 0x0C,
      0x41, 0x04, 0x20, 0x44, 0x04, 0x80, 0x5C, 0x06, 0x60, 0x43, 0x04, 0x10,
      0x40, 0x84, 0x08, 0x40, 0xCF, 0x07, 0xF8, 0x04, 0x00, 0x80, 0x10, 0x02,
      0x00, 0x40, 0x08, 0x01, 0x00, 0x20, 0x04, 0x04, 0x80, 0x90, 0x12, 0x03,
      0xFF, 0xC0, 0xE0, 0x3B, 0x01, 0x94, 0x14, 0xA0, 0xA4, 0x89, 0x24, 0x49,
      0x14, 0x48, 0xA2, 0x45, 0x12, 0x10, 0x90, 0x04, 0x80, 0x24, 0x01, 0x78,
      0x3C, 0xE0, 0xF6, 0x02, 0x50, 0x25, 0x02, 0x48, 0x24, 0xC2, 0x44, 0x24,
      0x22, 0x43, 0x24, 0x12, 0x40, 0xA4, 0x0A, 0x40, 0x6F, 0x06, 0x0F, 0x03,
      0x0C, 0x60, 0x64, 0x02, 0x80, 0x18, 0x01, 0x80, 0x18, 0x01, 0x80, 0x18,
      0x01, 0x40, 0x26, 0x06, 0x30, 0xC0, 0xF0, 0xFF, 0x10, 0x64, 0x05, 0x01,
      0x40, 0x50, 0x34, 0x19, 0xFC, 0x40, 0x10, 0x04, 0x01, 0x00, 0x40, 0x3E,
      0x00, 0x0F, 0x03, 0x0C, 0x60, 0x64, 0x02, 0x80, 0x18, 0x01, 0x80, 0x18,
      0x01, 0x80, 0x18, 0x01, 0x40, 0x26, 0x06, 0x30, 0xC1, 0xF0, 0x0C, 0x01,
      0xF1, 0x30, 0xE0, 0xFF, 0x04, 0x18, 0x40, 0xC4, 0x04, 0x40, 0x44, 0x0C,
      0x41, 0x87, 0xE0, 0x43, 0x04, 0x10, 0x40, 0x84, 0x04, 0x40, 0x4F, 0x03,
      0x1F, 0x48, 0x34, 0x05, 0x01, 0x40, 0x08, 0x01, 0xC0, 0x0E, 0x00, 0x40,
      0x18, 0x06, 0x01, 0xE1, 0xA7, 0xC0, 0xFF, 0xF0, 0x86, 0x10, 0x82, 0x00,
      0x40, 0x08, 0x01, 0x00, 0x20, 0x04, 0x00, 0x80, 0x10, 0x02, 0x00, 0x40,
      0x7F, 0x00, 0xF0, 0xF4, 0x02, 0x40, 0x24, 0x02, 0x40, 0x24, 0x02, 0x40,
      0x24, 0x02, 0x40, 0x24, 0x02, 0x40, 0x22, 0x04, 0x30, 0xC0, 0xF0, 0xF8,
      0x7C, 0x80, 0x22, 0x01, 0x04, 0x04, 0x10, 0x20, 0x40, 0x80, 0x82, 0x02,
      0x10, 0x08, 0x40, 0x11, 0x00, 0x48, 0x01, 0xA0, 0x03, 0x00, 0x0C, 0x00,
      0xF8, 0x7C, 0x80, 0x22, 0x00, 0x88, 0xC2, 0x23, 0x10, 0x8E, 0x42, 0x29,
      0x09, 0x24, 0x24, 0x90, 0x91, 0x41, 0x85, 0x06, 0x14, 0x18, 0x70, 0x60,
      0x80, 0xF0, 0xF2, 0x06, 0x30, 0x41, 0x08, 0x09, 0x80, 0x50, 0x06, 0x00,
      0x60, 0x0D, 0x00, 0x88, 0x10, 0xC2, 0x04, 0x60, 0x2F, 0x0F, 0xF0, 0xF2,
      0x02, 0x10, 0x41, 0x04, 0x08, 0x80, 0x50, 0x05, 0x00, 0x20, 0x02, 0x00,
      0x20, 0x02, 0x00, 0x20, 0x02, 0x01, 0xFC, 0xFF, 0x40, 0xA0, 0x90, 0x40,
      0x40, 0x40, 0x20, 0x20, 0x20, 0x10, 0x50, 0x30, 0x18, 0x0F, 0xFC, 0xF2,
      0x49, 0x24, 0x92, 0x49, 0x24, 0x9C, 0x80, 0x60, 0x10, 0x08, 0x02, 0x01,
      0x00, 0x40, 0x20, 0x08, 0x04, 0x01, 0x00, 0x80, 0x20, 0x10, 0x04, 0x02,
      0x00, 0x80, 0x40, 0xE4, 0x92, 0x49, 0x24, 0x92, 0x49, 0x3C, 0x08, 0x0C,
      0x09, 0x0C, 0x4C, 0x14, 0x04, 0xFF, 0xFC, 0x84, 0x21, 0x3E, 0x00, 0x60,
      0x08, 0x02, 0x3F, 0x98, 0x28, 0x0A, 0x02, 0xC3, 0x9F, 0x30, 0xE0, 0x01,
      0x00, 0x08, 0x00, 0x40, 0x02, 0x00, 0x13, 0xE0, 0xA0, 0x86, 0x02, 0x20,
      0x09, 0x00, 0x48, 0x02, 0x40, 0x13, 0x01, 0x14, 0x1B, 0x9F, 0x00, 0x1F,
      0x4C, 0x19, 0x01, 0x40, 0x28, 0x01, 0x00, 0x20, 0x02, 0x00, 0x60, 0x43,
      0xF0, 0x00, 0xC0, 0x08, 0x01, 0x00, 0x20, 0x04, 0x3C, 0x98, 0x52, 0x06,
      0x80, 0x50, 0x0A, 0x01, 0x40, 0x24, 0x0C, 0xC2, 0x87, 0x98, 0x3F, 0x18,
      0x68, 0x06, 0x01, 0xFF, 0xE0, 0x08, 0x03, 0x00, 0x60, 0xC7, 0xC0, 0x0F,
      0x98, 0x08, 0x04, 0x02, 0x07, 0xF8, 0x80, 0x40, 0x20, 0x10, 0x08, 0x04,
      0x02, 0x01, 0x03, 0xF8, 0x1E, 0x6C, 0x39, 0x03, 0x40, 0x28, 0x05, 0x00,
      0xA0, 0x12, 0x06, 0x61, 0x43, 0xC8, 0x01, 0x00, 0x20, 0x08, 0x3E, 0x00,
      0xC0, 0x10, 0x04, 0x01, 0x00, 0x40, 0x13, 0x87, 0x11, 0x82, 0x40, 0x90,
      0x24, 0x09, 0x02, 0x40, 0x90, 0x2E, 0x1C, 0x08, 0x04, 0x02, 0x00, 0x00,
      0x03, 0xC0, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01, 0x00, 0x80, 0x43, 0xFE,
      0x04, 0x08, 0x10, 0x00, 0x1F, 0xC0, 0x81, 0x02, 0x04, 0x08, 0x10, 0x20,
      0x40, 0x81, 0x02, 0x0B, 0xE0, 0xE0, 0x02, 0x00, 0x20, 0x02, 0x00, 0x20,
      0x02, 0x3C, 0x21, 0x02, 0x60, 0x2C, 0x03, 0x80, 0x24, 0x02, 0x20, 0x21,
      0x02, 0x08, 0xE1, 0xF0, 0x78, 0x04, 0x02, 0x01, 0x00, 0x80, 0x40, 0x20,
      0x10, 0x08, 0x04, 0x02, 0x01, 0x00, 0x80, 0x43, 0xFE, 0xDC, 0xE3, 0x19,
      0x90, 0x84, 0x84, 0x24, 0x21, 0x21, 0x09, 0x08, 0x48, 0x42, 0x42, 0x17,
      0x18, 0xC0, 0x67, 0x83, 0x84, 0x20, 0x22, 0x02, 0x20, 0x22, 0x02, 0x20,
      0x22, 0x02, 0x20, 0x2F, 0x07, 0x1F, 0x04, 0x11, 0x01, 0x40, 0x18, 0x03,
      0x00, 0x60, 0x0A, 0x02, 0x20, 0x83, 0xE0, 0xCF, 0x85, 0x06, 0x60, 0x24,
      0x01, 0x40, 0x14, 0x01, 0x40, 0x16, 0x02, 0x50, 0x44, 0xF8, 0x40, 0x04,
      0x00, 0x40, 0x0F, 0x00, 0x1E, 0x6C, 0x3B, 0x03, 0x40, 0x28, 0x05, 0x00,
      0xA0, 0x12, 0x06, 0x61, 0x43, 0xC8, 0x01, 0x00, 0x20, 0x04, 0x03, 0xC0,
      0xE3, 0x8B, 0x13, 0x80, 0x80, 0x20, 0x08, 0x02, 0x00, 0x80, 0x20, 0x3F,
      0x80, 0x1F, 0x58, 0x34, 0x05, 0x80, 0x1E, 0x00, 0x60, 0x06, 0x01, 0xC0,
      0xAF, 0xC0, 0x20, 0x04, 0x00, 0x80, 0x10, 0x0F, 0xF0, 0x40, 0x08, 0x01,
      0x00, 0x20, 0x04, 0x00, 0x80, 0x10, 0x03, 0x04, 0x3F, 0x00, 0xC1, 0xC8,
      0x09, 0x01, 0x20, 0x24, 0x04, 0x80, 0x90, 0x12, 0x02, 0x61, 0xC7, 0xCC,
      0xF8, 0xF9, 0x01, 0x08, 0x10, 0x60, 0x81, 0x08, 0x08, 0x40, 0x22, 0x01,
      0x20, 0x05, 0x00, 0x30, 0x00, 0xF0, 0x7A, 0x01, 0x10, 0x08, 0x8C, 0x42,
      0x62, 0x12, 0x90, 0xA5, 0x05, 0x18, 0x28, 0xC0, 0x86, 0x00, 0x78, 0xF3,
      0x04, 0x18, 0x80, 0xD0, 0x06, 0x00, 0x70, 0x09, 0x81, 0x0C, 0x20, 0x6F,
      0x8F, 0xF0, 0xF2, 0x02, 0x20, 0x41, 0x04, 0x10, 0x80, 0x88, 0x09, 0x00,
      0x50, 0x06, 0x00, 0x20, 0x04, 0x00, 0x40, 0x08, 0x0F, 0xE0, 0xFF, 0x41,
      0x00, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x40, 0xBF, 0xC0, 0x19, 0x08,
      0x42, 0x10, 0x84, 0x64, 0x18, 0x42, 0x10, 0x84, 0x20, 0xC0, 0xFF, 0xFF,
      0xC0, 0xC1, 0x08, 0x42, 0x10, 0x84, 0x10, 0x4C, 0x42, 0x10, 0x84, 0x26,
      0x00, 0x38, 0x13, 0x38, 0x38, 0x30, 0x06, 0x00, 0xC0, 0x10, 0x00, 0x00,
      0x03, 0xE0, 0x06, 0x00, 0x80, 0x23, 0xF9, 0x82, 0x80, 0xA0, 0x2C, 0x39,
      0xF3, 0x0C, 0x00, 0x18, 0x00, 0x30, 0x00, 0x40, 0x00, 0x00, 0xFC, 0x00,
      0x30, 0x01, 0x20, 0x04, 0x80, 0x11, 0x00, 0x84, 0x02, 0x10, 0x10, 0x20,
      0x7F, 0x81, 0x02, 0x08, 0x04, 0x20, 0x10, 0x80, 0x4F, 0x87, 0xC0, 0x00,
      0x18, 0x60, 0x00, 0x00, 0x3E, 0x00, 0x60, 0x08, 0x02, 0x3F, 0x98, 0x28,
      0x0A, 0x02, 0xC3, 0x9F, 0x30, 0x18, 0x60, 0x00, 0x03, 0xF0, 0x00, 0xC0,
      0x04, 0x80, 0x12, 0x00, 0x44, 0x02, 0x10, 0x08, 0x40, 0x40, 0x81, 0xFE,
      0x04, 0x08, 0x20, 0x10, 0x80, 0x42, 0x01, 0x3E, 0x1F, 0x00, 0x03, 0x81,
      0x30, 0x86, 0x00, 0x00, 0x03, 0xE0, 0x06, 0x00, 0x80, 0x23, 0xF9, 0x82,
      0x80, 0xA0, 0x2C, 0x39, 0xF3, 0x01, 0x00, 0x0E, 0x00, 0x44, 0x02, 0x08,
      0x00, 0x00, 0xFC, 0x00, 0x30, 0x01, 0x20, 0x04, 0x80, 0x11, 0x00, 0x84,
      0x02, 0x10, 0x10, 0x20, 0x7F, 0x81, 0x02, 0x08, 0x04, 0x20, 0x10, 0x80,
      0x4F, 0x87, 0xC0, 0x01, 0x00, 0x80, 0x40, 0x20, 0x00, 0x00, 0x03, 0xF1,
      0x86, 0x80, 0x60, 0x1F, 0xFE, 0x00, 0x80, 0x30, 0x06, 0x0C, 0x7C, 0x03,
      0x00, 0xC0, 0x30, 0x04, 0x00, 0x01, 0xFF, 0x90, 0x12, 0x02, 0x40, 0x08,
      0x01, 0x10, 0x3E, 0x04, 0x40, 0x80, 0x10, 0x02, 0x01, 0x40, 0x28, 0x07,
      0xFF, 0x80, 0x10, 0x02, 0x00, 0x40, 0x08, 0x00, 0x00, 0x03, 0xF1, 0x86,
      0x80, 0x60, 0x1F, 0xFE, 0x00, 0x80, 0x30, 0x06, 0x0C, 0x7C, 0x10, 0x01,
      0x00, 0x10, 0x00, 0x00, 0x01, 0xFF, 0x90, 0x12, 0x02, 0x40, 0x08, 0x01,
      0x10, 0x3E, 0x04, 0x40, 0x80, 0x10, 0x02, 0x01, 0x40, 0x28, 0x07, 0xFF,
      0x80, 0x04, 0x03, 0x81, 0xB0, 0xC6, 0x00, 0x00, 0x03, 0xF1, 0x86, 0x80,
      0x60, 0x1F, 0xFE, 0x00, 0x80, 0x30, 0x06, 0x0C, 0x7C, 0x04, 0x01, 0xC0,
      0x4C, 0x10, 0xC0, 0x01, 0xFF, 0x90, 0x12, 0x02, 0x40, 0x08, 0x01, 0x10,
      0x3E, 0x04, 0x40, 0x80, 0x10, 0x02, 0x01, 0x40, 0x28, 0x07, 0xFF, 0x80,
      0x00, 0x18, 0x60, 0x00, 0x00, 0x3F, 0x18, 0x68, 0x06, 0x01, 0xFF, 0xE0,
      0x08, 0x03, 0x00, 0x60, 0xC7, 0xC0, 0x61, 0x88, 0x23, 0xFF, 0x20, 0x24,
      0x04, 0x80, 0x10, 0x02, 0x20, 0x7C, 0x08, 0x81, 0x00, 0x20, 0x04, 0x02,
      0x80, 0x50, 0x0F, 0xFF, 0x04, 0x01, 0xC0, 0x6C, 0x10, 0x40, 0x00, 0x00,
      0x07, 0xC1, 0x04, 0x40, 0x50, 0x06, 0x00, 0xC0, 0x18, 0x02, 0x80, 0x88,
      0x20, 0xF8, 0x02, 0x00, 0x70, 0x08, 0x81, 0x04, 0x00, 0x00, 0xF0, 0x30,
      0xC6, 0x06, 0x40, 0x28, 0x01, 0x80, 0x18, 0x01, 0x80, 0x18, 0x01, 0x80,
      0x14, 0x02, 0x60, 0x63, 0x0C, 0x0F, 0x00, 0x00, 0x0C, 0x30, 0x00, 0x00,
      0x01, 0xF0, 0x41, 0x10, 0x14, 0x01, 0x80, 0x30, 0x06, 0x00, 0xA0, 0x22,
      0x08, 0x3E, 0x00, 0x30, 0xC1, 0x04, 0x0F, 0x03, 0x0C, 0x60, 0x64, 0x02,
      0x80, 0x18, 0x01, 0x80, 0x18, 0x01, 0x80, 0x18, 0x01, 0x40, 0x26, 0x06,
      0x30, 0xC0, 0xF0, 0x00, 0x0C, 0x09, 0x08, 0x40, 0x00, 0x01, 0xE0, 0x10,
      0x08, 0x04, 0x02, 0x01, 0x00, 0x80, 0x40, 0x21, 0xFF, 0x10, 0x71, 0x14,
      0x10, 0x1F, 0xC4, 0x08, 0x10, 0x20, 0x40, 0x81, 0x02, 0x04, 0x08, 0x10,
      0x23, 0xF8, 0x1F, 0x48, 0x34, 0x06, 0x01, 0x80, 0x20, 0x08, 0x01, 0x00,
      0x60, 0xC7, 0xC0, 0x40, 0x18, 0x02, 0x07, 0x80, 0x1F, 0x4C, 0x74, 0x05,
      0x01, 0x80, 0x20, 0x08, 0x02, 0x00, 0x80, 0x20, 0x04, 0x01, 0x81, 0x30,
      0xC3, 0xC0, 0x40, 0x18, 0x02, 0x07, 0x80, 0x08, 0x23, 0x08, 0xC2, 0x30,
      0xCC, 0x31, 0x86, 0x18, 0x61, 0x84, 0x18, 0x41, 0x04, 0x84, 0x18, 0x41,
      0x84, 0x18, 0xC1, 0x8C, 0x31, 0x8C, 0x63, 0x08, 0xC2, 0x10, 0x80, 0xC1,
      0xC8, 0x09, 0x01, 0x20, 0x24, 0x04, 0x80, 0x90, 0x12, 0x02, 0x61, 0xCF,
      0xCD, 0x00, 0x20, 0x04, 0x00, 0x80, 0x00, 0x07, 0xC0, 0x60, 0x82, 0x01,
      0x11, 0xF2, 0xC4, 0x4E, 0x21, 0x18, 0x80, 0x62, 0x01, 0x88, 0x05, 0x11,
      0x34, 0x38, 0x88, 0x04, 0x18, 0x20, 0x1F, 0x00, 0x0C, 0x00, 0x18, 0x00,
      0x30, 0x00, 0x40, 0x00, 0x00, 0xFC, 0x00, 0x30, 0x01, 0x20, 0x04, 0x80,
      0x11, 0x00, 0x84, 0x02, 0x10, 0x10, 0x20, 0x7F, 0x81, 0x02, 0x08, 0x04,
      0x20, 0x10, 0x80, 0x4F, 0x87, 0xC0, 0x00, 0xC0, 0x08, 0x01, 0x00, 0x20,
      0x04, 0x3C, 0x98, 0x52, 0x06, 0x80, 0x50, 0x0A, 0x01, 0x40, 0x24, 0x0C,
      0xC2, 0x87, 0x98, 0x3F, 0x18, 0x68, 0x06, 0x01, 0xFF, 0xE0, 0x08, 0x03,
      0x00, 0x60, 0xC7, 0xC0, 0x84, 0x21, 0x0C, 0x01, 0x80, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x3F, 0xF8, 0x00, 0x00, 0x00, 0x00, 0x30, 0x06, 0x00, 0x08,
      0x04, 0x02, 0x01, 0x0F, 0xF8, 0x40, 0x20, 0x10, 0x08, 0x00, 0x00, 0x1F,
      0xF0, 0x38, 0x8A, 0x0C, 0x18, 0x28, 0x8E, 0x00, 0x00, 0x80, 0x10, 0x06,
      0x00, 0x40, 0x00, 0x0F, 0x0F, 0x40, 0x24, 0x02, 0x40, 0x24, 0x02, 0x40,
      0x24, 0x02, 0x40, 0x24, 0x02, 0x40, 0x24, 0x02, 0x20, 0x43, 0x0C, 0x0F,
      0x00, 0x00, 0xC0, 0x60, 0x18, 0x0C, 0x06, 0x01, 0x80, 0x0C, 0x00, 0x60,
      0x03, 0x00, 0x30, 0x01, 0x00, 0x78, 0x04, 0x02, 0x01, 0x00, 0x80, 0x40,
      0x20, 0x10, 0x08, 0x04, 0x02, 0x01, 0x00, 0x80, 0x43, 0xFE, 0xE0, 0x02,
      0x00, 0x20, 0x02, 0x00, 0x20, 0x02, 0x3C, 0x21, 0x02, 0x60, 0x2C, 0x03,
      0x80, 0x24, 0x02, 0x20, 0x21, 0x02, 0x08, 0xE1, 0xF0, 0x04, 0x08, 0x10,
      0x00, 0x1F, 0xC0, 0x81, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x81, 0x02,
      0x0B, 0xE0, 0x08, 0x04, 0x02, 0x00, 0x00, 0x03, 0xC0, 0x20, 0x10, 0x08,
      0x04, 0x02, 0x01, 0x00, 0x80, 0x43, 0xFE, 0xC0, 0x10, 0x04, 0x01, 0x00,
      0x40, 0x13, 0x87, 0x11, 0x82, 0x40, 0x90, 0x24, 0x09, 0x02, 0x40, 0x90,
      0x2E, 0x1C, 0x1E, 0x6C, 0x39, 0x03, 0x40, 0x28, 0x05, 0x00, 0xA0, 0x12,
      0x06, 0x61, 0x43, 0xC8, 0x01, 0x00, 0x20, 0x08, 0x3E, 0x00, 0x0F, 0x98,
      0x08, 0x04, 0x02, 0x07, 0xF8, 0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02,
      0x01, 0x03, 0xF8, 0x3F, 0x18, 0x68, 0x06, 0x01, 0xFF, 0xE0, 0x08, 0x03,
      0x00, 0x60, 0xC7, 0xC0, 0x00, 0xC0, 0x08, 0x01, 0x00, 0x20, 0x04, 0x3C,
      0x98, 0x52, 0x06, 0x80, 0x50, 0x0A, 0x01, 0x40, 0x24, 0x0C, 0xC2, 0x87,
      0x98, 0x1F, 0x4C, 0x19, 0x01, 0x40, 0x28, 0x01, 0x00, 0x20, 0x02, 0x00,
      0x60, 0x43, 0xF0, 0xE0, 0x01, 0x00, 0x08, 0x00, 0x40, 0x02, 0x00, 0x13,
      0xE0, 0xA0, 0x86, 0x02, 0x20, 0x09, 0x00, 0x48, 0x02, 0x40, 0x13, 0x01,
      0x14, 0x1B, 0x9F, 0x00, 0x3E, 0x00, 0x60, 0x08, 0x02, 0x3F, 0x98, 0x28,
      0x0A, 0x02, 0xC3, 0x9F, 0x30, 0x84, 0x21, 0xFF, 0xFC, 0x08, 0x0C, 0x09,
      0x0C, 0x4C, 0x14, 0x04, 0xE4, 0x92, 0x49, 0x24, 0x92, 0x49, 0x3C, 0x80,
      0x60, 0x10, 0x08, 0x02, 0x01, 0x00, 0x40, 0x20, 0x08, 0x04, 0x01, 0x00,
      0x80, 0x20, 0x10, 0x04, 0x02, 0x00, 0x80, 0x40, 0xF2, 0x49, 0x24, 0x92,
      0x49, 0x24, 0x9C, 0xFF, 0x40, 0xA0, 0x90, 0x40, 0x40, 0x40, 0x20, 0x20,
      0x20, 0x10, 0x50, 0x30, 0x18, 0x0F, 0xFC, 0xF0, 0xF2, 0x02, 0x10, 0x41,
      0x04, 0x08, 0x80, 0x50, 0x05, 0x00, 0x20, 0x02, 0x00, 0x20, 0x02, 0x00,
      0x20, 0x02, 0x01, 0xFC, 0xF0, 0xF2, 0x06, 0x30, 0x41, 0x08, 0x09, 0x80,
      0x50, 0x06, 0x00, 0x60, 0x0D, 0x00, 0x88, 0x10, 0xC2, 0x04, 0x60, 0x2F,
      0x0F, 0xF8, 0x7C, 0x80, 0x22, 0x00, 0x88, 0xC2, 0x23, 0x10, 0x8E, 0x42,
      0x29, 0x09, 0x24, 0x24, 0x90, 0x91, 0x41, 0x85, 0x06, 0x14, 0x18, 0x70,
      0x60, 0x80, 0xF8, 0x7C, 0x80, 0x22, 0x01, 0x04, 0x04, 0x10, 0x20, 0x40,
      0x80, 0x82, 0x02, 0x10, 0x08, 0x40, 0x11, 0x00, 0x48, 0x01, 0xA0, 0x03,
      0x00, 0x0C, 0x00, 0xF0, 0xF4, 0x02, 0x40, 0x24, 0x02, 0x40, 0x24, 0x02,
      0x40, 0x24, 0x02, 0x40, 0x24, 0x02, 0x40, 0x22, 0x04, 0x30, 0xC0, 0xF0,
      0xFF, 0xF0, 0x86, 0x10, 0x82, 0x00, 0x40, 0x08, 0x01, 0x00, 0x20, 0x04,
      0x00, 0x80, 0x10, 0x02, 0x00, 0x40, 0x7F, 0x00, 0x1F, 0x48, 0x34, 0x05,
      0x01, 0x40, 0x08, 0x01, 0xC0, 0x0E, 0x00, 0x40, 0x18, 0x06, 0x01, 0xE1,
      0xA7, 0xC0, 0xFF, 0x04, 0x18, 0x40, 0xC4, 0x04, 0x40, 0x44, 0x0C, 0x41,
      0x87, 0xE0, 0x43, 0x04, 0x10, 0x40, 0x84, 0x04, 0x40, 0x4F, 0x03, 0x0F,
      0x03, 0x0C, 0x60, 0x64, 0x02, 0x80, 0x18, 0x01, 0x80, 0x18, 0x01, 0x80,
      0x18, 0x01, 0x40, 0x26, 0x06, 0x30, 0xC1, 0xF0, 0x0C, 0x01, 0xF1, 0x30,
      0xE0, 0xFF, 0x10, 0x64, 0x05, 0x01, 0x40, 0x50, 0x34, 0x19, 0xFC, 0x40,
      0x10, 0x04, 0x01, 0x00, 0x40, 0x3E, 0x00, 0x00, 0xC0, 0x60, 0x18, 0x0C,
      0x06, 0x01, 0x80, 0x0C, 0x00, 0x60, 0x03, 0x00, 0x30, 0x01, 0x00, 0x06,
      0x0A, 0x0A, 0x12, 0x22, 0x22, 0x42, 0x42, 0x82, 0x82, 0xFF, 0x02, 0x02,
      0x02, 0x0F, 0x06, 0x0A, 0x0A, 0x12, 0x22, 0x22, 0x42, 0x42, 0x82, 0x82,
      0xFF, 0x02, 0x02, 0x02, 0x0F, 0x3B, 0x9C, 0xCE, 0x62, 0x00, 0x04, 0x07,
      0xA2, 0x19, 0x02, 0x40, 0x10, 0x03, 0x00, 0x3C, 0x00, 0x80, 0x10, 0x06,
      0x01, 0xE0, 0xA7, 0xC0, 0x40, 0x10, 0x04, 0x00, 0xFF, 0xFC, 0x00, 0x63,
      0xE3, 0x60, 0x9A, 0x02, 0xC0, 0x16, 0x00, 0xB0, 0x09, 0x81, 0x8C, 0x10,
      0x60, 0x83, 0x00, 0x18, 0x00, 0xC0, 0x06, 0x1C, 0x30, 0xE1, 0x80, 0x0F,
      0xFF, 0xC0, 0xFF, 0xFC, 0x00, 0x63, 0xE3, 0x60, 0x9A, 0x02, 0xC0, 0x16,
      0x00, 0xB0, 0x09, 0x81, 0x8C, 0x10, 0x60, 0x83, 0x00, 0x18, 0x00, 0xC0,
      0x06, 0x1C, 0x30, 0xE1, 0x80, 0x0F, 0xFF, 0xC0, 0xFF, 0xFC, 0x00, 0x63,
      0xE3, 0x60, 0x9A, 0x02, 0xC0, 0x16, 0x00, 0xB0, 0x09, 0x81, 0x8C, 0x10,
      0x60, 0x83, 0x00, 0x18, 0x00, 0xC0, 0x06, 0x1C, 0x30, 0xE1, 0x80, 0x0F,
      0xFF, 0xC0, 0xFF, 0xFC, 0x00, 0x63, 0xE3, 0x60, 0x9A, 0x02, 0xC0, 0x16,
      0x00, 0xB0, 0x09, 0x81, 0x8C, 0x10, 0x60, 0x83, 0x00, 0x18, 0x00, 0xC0,
      0x06, 0x1C, 0x30, 0xE1, 0x80, 0x0F, 0xFF, 0xC0, 0xFF, 0xFC, 0x00, 0x63,
      0xE3, 0x60, 0x9A, 0x02, 0xC0, 0x16, 0x00, 0xB0, 0x09, 0x81, 0x8C, 0x10,
      0x60, 0x83, 0x00, 0x18, 0x00, 0xC0, 0x06, 0x1C, 0x30, 0xE1, 0x80, 0x0F,
      0xFF, 0xC0, 0xFF, 0xFC, 0x00, 0x63, 0xE3, 0x60, 0x9A, 0x02, 0xC0, 0x16,
      0x00, 0xB0, 0x09, 0x81, 0x8C, 0x10, 0x60, 0x83, 0x00, 0x18, 0x00, 0xC0,
      0x06, 0x1C, 0x30, 0xE1, 0x80, 0x0F, 0xFF, 0xC0, 0xFF, 0xFC, 0x00, 0x63,
      0xE3, 0x60, 0x9A, 0x02, 0xC0, 0x16, 0x00, 0xB0, 0x09, 0x81, 0x8C, 0x10,
      0x60, 0x83, 0x00, 0x18, 0x00, 0xC0, 0x06, 0x1C, 0x30, 0xE1, 0x80, 0x0F,
      0xFF, 0xC0, 0xFF, 0xFC, 0x00, 0x63, 0xE3, 0x60, 0x9A, 0x02, 0xC0, 0x16,
      0x00, 0xB0, 0x09, 0x81, 0x8C, 0x10, 0x60, 0x83, 0x00, 0x18, 0x00, 0xC0,
      0x06, 0x1C, 0x30, 0xE1, 0x80, 0x0F, 0xFF, 0xC0, 0xFF, 0xFC, 0x00, 0x63,
      0xE3, 0x60, 0x9A, 0x02, 0xC0, 0x16, 0x00, 0xB0, 0x09, 0x81, 0x8C, 0x10,
      0x60, 0x83, 0x00, 0x18, 0x00, 0xC0, 0x06, 0x1C, 0x30, 0xE1, 0x80, 0x0F,
      0xFF, 0xC0, 0xFF, 0xFC, 0x00, 0x63, 0xE3, 0x60, 0x9A, 0x02, 0xC0, 0x16,
      0x00, 0xB0, 0x09, 0x81, 0x8C, 0x10, 0x60, 0x83, 0x00, 0x18, 0x00, 0xC0,
      0x06, 0x1C, 0x30, 0xE1, 0x80, 0x0F, 0xFF, 0xC0, 0xFF, 0xFC, 0x00, 0x63,
      0xE3, 0x60, 0x9A, 0x02, 0xC0, 0x16, 0x00, 0xB0, 0x09, 0x81, 0x8C, 0x10,
      0x60, 0x83, 0x00, 0x18, 0x00, 0xC0, 0x06, 0x1C, 0x30, 0xE1, 0x80, 0x0F,
      0xFF, 0xC0, 0xFF, 0xFC, 0x00, 0x63, 0xE3, 0x60, 0x9A, 0x02, 0xC0, 0x16,
      0x00, 0xB0, 0x09, 0x81, 0x8C, 0x10, 0x60, 0x83, 0x00, 0x18, 0x00, 0xC0,
      0x06, 0x1C, 0x30, 0xE1, 0x80, 0x0F, 0xFF, 0xC0, 0xFF, 0xC0, 0x10, 0x04,
      0x01, 0x00, 0x40, 0x10, 0x3C, 0xCD, 0x08, 0x10, 0x43, 0x0C, 0x30, 0xFE,
      0x38, 0x8A, 0x0C, 0x18, 0x28, 0x8E, 0x00, 0xFE, 0x20, 0x07, 0x00, 0x08,
      0x00, 0x40, 0xC2, 0x04, 0x10, 0x40, 0x84, 0x04, 0x66, 0xFA, 0x30, 0x22,
      0x82, 0x24, 0x21, 0x23, 0x0F, 0x90, 0x08, 0x00, 0xE0, 0x18, 0x60, 0x00,
      0x03, 0xF0, 0x00, 0xC0, 0x04, 0x80, 0x12, 0x00, 0x44, 0x02, 0x10, 0x08,
      0x40, 0x40, 0x81, 0xFE, 0x04, 0x08, 0x20, 0x10, 0x80, 0x42, 0x01, 0x3E,
      0x1F, 0xFC, 0x00, 0x49, 0x24, 0x92, 0x48, 0xFF, 0xFC, 0x00, 0x63, 0xE3,
      0x60, 0x9A, 0x02, 0xC0, 0x16, 0x00, 0xB0, 0x09, 0x81, 0x8C, 0x10, 0x60,
      0x83, 0x00, 0x18, 0x00, 0xC0, 0x06, 0x1C, 0x30, 0xE1, 0x80, 0x0F, 0xFF,
      0xC0, 0xFF, 0xFC, 0x00, 0x63, 0xE3, 0x60, 0x9A, 0x02, 0xC0, 0x16, 0x00,
      0xB0, 0x09, 0x81, 0x8C, 0x10, 0x60, 0x83, 0x00, 0x18, 0x00, 0xC0, 0x06,
      0x1C, 0x30, 0xE1, 0x80, 0x0F, 0xFF, 0xC0, 0xFF, 0xFC, 0x00, 0x63, 0xE3,
      0x60, 0x9A, 0x02, 0xC0, 0x16, 0x00, 0xB0, 0x09, 0x81, 0x8C, 0x10, 0x60,
      0x83, 0x00, 0x18, 0x00, 0xC0, 0x06, 0x1C, 0x30, 0xE1, 0x80, 0x0F, 0xFF,
      0xC0, 0xFF, 0xFC, 0x00, 0x63, 0xE3, 0x60, 0x9A, 0x02, 0xC0, 0x16, 0x00,
      0xB0, 0x09, 0x81, 0x8C, 0x10, 0x60, 0x83, 0x00, 0x18, 0x00, 0xC0, 0x06,
      0x1C, 0x30, 0xE1, 0x80, 0x0F, 0xFF, 0xC0, 0xFF, 0xFC, 0x00, 0x63, 0xE3,
      0x60, 0x9A, 0x02, 0xC0, 0x16, 0x00, 0xB0, 0x09, 0x81, 0x8C, 0x10, 0x60,
      0x83, 0x00, 0x18, 0x00, 0xC0, 0x06, 0x1C, 0x30, 0xE1, 0x80, 0x0F, 0xFF,
      0xC0, 0x18, 0x60, 0x00, 0x03, 0xF0, 0x00, 0xC0, 0x04, 0x80, 0x12, 0x00,
      0x44, 0x02, 0x10, 0x08, 0x40, 0x40, 0x81, 0xFE, 0x04, 0x08, 0x20, 0x10,
      0x80, 0x42, 0x01, 0x3E, 0x1F, 0xFF, 0xFC, 0x00, 0x63, 0xE3, 0x60, 0x9A,
      0x02, 0xC0, 0x16, 0x00, 0xB0, 0x09, 0x81, 0x8C, 0x10, 0x60, 0x83, 0x00,
      0x18, 0x00, 0xC0, 0x06, 0x1C, 0x30, 0xE1, 0x80, 0x0F, 0xFF, 0xC0])

    index = {
        "É":0,
        "C":1,
        " ":2,
        "!":3,
        '"':4,
        "#":5,
        "$":6,
        "%":7,
        "&":8,
        "'":9,
        "(":10,
        ")":11,
        "*":12,
        "+":13,
        ",":14,
        "-":15,
        ".":16,
        "/":17,
        "0":18,
        "1":19,
        "2":20,
        "3":21,
        "4":22,
        "5":23,
        "6":24,
        "7":25,
        "8":26,
        "9":27,
        ":":28,
        ";":29,
        "<":30,
        "=":31,
        ">":32,
        "?":33,
        "@":34,
        "A":35,
        "B":36,
        "C":37,
        "D":38,
        "E":39,
        "F":40,
        "G":41,
        "H":42,
        "I":43,
        "J":44,
        "K":45,
        "L":46,
        "M":47,
        "N":48,
        "O":49,
        "P":50,
        "Q":51,
        "R":52,
        "S":53,
        "T":54,
        "U":55,
        "V":56,
        "W":57,
        "X":58,
        "Y":59,
        "Z":60,
        "[":61,
        "\\":62,
        "]":63,
        "^":64,
        "_":65,
        "`":66,
        "a":67,
        "b":68,
        "c":69,
        "d":70,
        "e":71,
        "f":72,
        "g":73,
        "h":74,
        "i":75,
        "j":76,
        "k":77,
        "l":78,
        "m":79,
        "n":80,
        "o":81,
        "p":82,
        "q":83,
        "r":84,
        "s":85,
        "t":86,
        "u":87,
        "v":88,
        "w":89,
        "x":90,
        "y":91,
        "z":92,
        "{":93,
        "|":94,
        "}":95,
        "~":96,
        "à":97,
        "À":98,
        "ä":99,
        "Ä":100,
        "â":101,
        "Â":102,
        "é":103,
        "É":104,
        "è":105,
        "È":106,
        "ê":107,
        "Ê":108,
        "ë":109,
        "Ë":110,
        "ô":111,
        "Ô":112,
        "ö":113,
        "Ö":114,
        "î":115,
        "Î":116,
        "ç":117,
        "Ç":118,
        "«":119,
        "»":120,
        "µ":121,
        "Ω":122,
        "π":123,
        "≤":124,
        "≥":125,
        "≠":126,
        "÷":127,
        "±":128,
        "°":129,
        "˚":130,
        "☼":131,
        "╬":132,
        "╫":133,
        "╪":134,
        "╩":135,
        "╨":136,
        "╧":137,
        "╦":138,
        "╥":139,
        "╤":140,
        "╣":141,
        "╢":142,
        "╡":143,
        "╠":144,
        "╟":145,
        "╞":146,
        "╝":147,
        "\\":148,
        "╛":149,
        "╚":150,
        "╙":151,
        "╘":152,
        "╗":153,
        "╖":154,
        "╕":155,
        "╔":156,
        "╓":157,
        "╒":158,
        "║":159,
        "═":160,
        "┼":161,
        "┴":162,
        "┴":163,
        "┬":164,
        "┤":165,
        "├":166,
        "┘":167,
        "└":168,
        "┐":169,
        "┌":170,
        "│":171,
        "─":172,
        "▀":173,
        "▄":174,
        "█":175,
        "▌":176,
        "▐":177,
        "▬":178,
        "▲":179,
        "►":180,
        "▼":181,
        "◄":182,
        "□":183,
        "←":184,
        "↑":185,
        "→":186,
        "↓":187,
        "↔":188,
        "◄":189}


    glyph=[
        [     0,  11,  19,  14,    2,  -18 ],   # idx=0  C3, 89 'É'
        [    27,  10,  14,  14,    2,  -13 ],   # idx=1  43 'C'
        [    45,   0,   0,  14,    0,    1 ],   # idx=2  20 ' '
        [    45,   3,  15,  14,    6,  -14 ],   # idx=3  21 '!'
        [    51,   8,   7,  14,    3,  -14 ],   # idx=4  22 '"'
        [    58,  10,  16,  14,    2,  -14 ],   # idx=5  23 '#'
        [    78,  10,  17,  14,    2,  -14 ],   # idx=6  24 '$'
        [   100,  10,  15,  14,    2,  -14 ],   # idx=7  25 '%'
        [   119,   9,  12,  14,    3,  -11 ],   # idx=8  26 '&'
        [   133,   3,   7,  14,    5,  -14 ],   # idx=9  27 '''
        [   136,   3,  18,  14,    7,  -14 ],   # idx=10  28 '('
        [   143,   3,  18,  14,    4,  -14 ],   # idx=11  29 ')'
        [   150,   9,   9,  14,    3,  -14 ],   # idx=12  2A '*'
        [   161,   9,  11,  14,    3,  -11 ],   # idx=13  2B '+'
        [   174,   5,   7,  14,    3,   -3 ],   # idx=14  2C ','
        [   179,  11,   1,  14,    2,   -6 ],   # idx=15  2D '-'
        [   181,   3,   3,  14,    5,   -2 ],   # idx=16  2E '.'
        [   183,   9,  18,  14,    3,  -15 ],   # idx=17  2F '/'
        [   204,   9,  15,  14,    3,  -14 ],   # idx=18  30 '0'
        [   221,   7,  14,  14,    4,  -13 ],   # idx=19  31 '1'
        [   234,   9,  15,  14,    2,  -14 ],   # idx=20  32 '2'
        [   251,  10,  15,  14,    2,  -14 ],   # idx=21  33 '3'
        [   270,   8,  15,  14,    3,  -14 ],   # idx=22  34 '4'
        [   285,   9,  15,  14,    3,  -14 ],   # idx=23  35 '5'
        [   302,   9,  15,  14,    3,  -14 ],   # idx=24  36 '6'
        [   319,   8,  15,  14,    3,  -14 ],   # idx=25  37 '7'
        [   334,   9,  15,  14,    3,  -14 ],   # idx=26  38 '8'
        [   351,   9,  15,  14,    3,  -14 ],   # idx=27  39 '9'
        [   368,   3,  10,  14,    5,   -9 ],   # idx=28  3A ':'
        [   372,   5,  13,  14,    3,   -9 ],   # idx=29  3B ';'
        [   381,  11,  11,  14,    2,  -11 ],   # idx=30  3C '<'
        [   397,  12,   4,  14,    1,   -8 ],   # idx=31  3D '='
        [   403,  11,  11,  14,    2,  -11 ],   # idx=32  3E '>'
        [   419,   9,  14,  14,    3,  -13 ],   # idx=33  3F '?'
        [   435,   9,  16,  14,    3,  -14 ],   # idx=34  40 '@'
        [   453,  14,  14,  14,    0,  -13 ],   # idx=35  41 'A'
        [   478,  11,  14,  14,    2,  -13 ],   # idx=36  42 'B'
        [   498,  10,  14,  14,    2,  -13 ],   # idx=37  43 'C'
        [   516,  10,  14,  14,    2,  -13 ],   # idx=38  44 'D'
        [   534,  11,  14,  14,    2,  -13 ],   # idx=39  45 'E'
        [   554,  11,  14,  14,    2,  -13 ],   # idx=40  46 'F'
        [   574,  11,  14,  14,    2,  -13 ],   # idx=41  47 'G'
        [   594,  10,  14,  14,    2,  -13 ],   # idx=42  48 'H'
        [   612,   7,  14,  14,    4,  -13 ],   # idx=43  49 'I'
        [   625,  11,  14,  14,    2,  -13 ],   # idx=44  4A 'J'
        [   645,  12,  14,  14,    2,  -13 ],   # idx=45  4B 'K'
        [   666,  11,  14,  14,    2,  -13 ],   # idx=46  4C 'L'
        [   686,  13,  14,  14,    1,  -13 ],   # idx=47  4D 'M'
        [   709,  12,  14,  14,    1,  -13 ],   # idx=48  4E 'N'
        [   730,  12,  14,  14,    1,  -13 ],   # idx=49  4F 'O'
        [   751,  10,  14,  14,    2,  -13 ],   # idx=50  50 'P'
        [   769,  12,  17,  14,    1,  -13 ],   # idx=51  51 'Q'
        [   795,  12,  14,  14,    2,  -13 ],   # idx=52  52 'R'
        [   816,  10,  14,  14,    2,  -13 ],   # idx=53  53 'S'
        [   834,  11,  14,  14,    2,  -13 ],   # idx=54  54 'T'
        [   854,  12,  14,  14,    1,  -13 ],   # idx=55  55 'U'
        [   875,  14,  14,  14,    0,  -13 ],   # idx=56  56 'V'
        [   900,  14,  14,  14,    0,  -13 ],   # idx=57  57 'W'
        [   925,  12,  14,  14,    1,  -13 ],   # idx=58  58 'X'
        [   946,  12,  14,  14,    1,  -13 ],   # idx=59  59 'Y'
        [   967,   9,  14,  14,    3,  -13 ],   # idx=60  5A 'Z'
        [   983,   3,  18,  14,    7,  -14 ],   # idx=61  5B '['
        [   990,   9,  18,  14,    3,  -15 ],   # idx=62  5C '\'
        [  1011,   3,  18,  14,    5,  -14 ],   # idx=63  5D ']'
        [  1018,   9,   6,  14,    3,  -14 ],   # idx=64  5E '^'
        [  1025,  14,   1,  14,    0,    3 ],   # idx=65  5F '_'
        [  1027,   4,   4,  14,    4,  -15 ],   # idx=66  60 '`'
        [  1029,  10,  10,  14,    2,   -9 ],   # idx=67  61 'a'
        [  1042,  13,  15,  14,    0,  -14 ],   # idx=68  62 'b'
        [  1067,  11,  10,  14,    2,   -9 ],   # idx=69  63 'c'
        [  1081,  11,  15,  14,    2,  -14 ],   # idx=70  64 'd'
        [  1102,  10,  10,  14,    2,   -9 ],   # idx=71  65 'e'
        [  1115,   9,  15,  14,    4,  -14 ],   # idx=72  66 'f'
        [  1132,  11,  14,  14,    2,   -9 ],   # idx=73  67 'g'
        [  1152,  10,  15,  14,    2,  -14 ],   # idx=74  68 'h'
        [  1171,   9,  15,  14,    3,  -14 ],   # idx=75  69 'i'
        [  1188,   7,  19,  14,    3,  -14 ],   # idx=76  6A 'j'
        [  1205,  12,  15,  14,    1,  -14 ],   # idx=77  6B 'k'
        [  1228,   9,  15,  14,    3,  -14 ],   # idx=78  6C 'l'
        [  1245,  13,  10,  14,    1,   -9 ],   # idx=79  6D 'm'
        [  1262,  12,  10,  14,    1,   -9 ],   # idx=80  6E 'n'
        [  1277,  11,  10,  14,    2,   -9 ],   # idx=81  6F 'o'
        [  1291,  12,  14,  14,    1,   -9 ],   # idx=82  70 'p'
        [  1312,  11,  14,  14,    2,   -9 ],   # idx=83  71 'q'
        [  1332,  10,  10,  14,    3,   -9 ],   # idx=84  72 'r'
        [  1345,  10,  10,  14,    2,   -9 ],   # idx=85  73 's'
        [  1358,  11,  14,  14,    1,  -13 ],   # idx=86  74 't'
        [  1378,  11,  10,  14,    2,   -9 ],   # idx=87  75 'u'
        [  1392,  13,  10,  14,    1,   -9 ],   # idx=88  76 'v'
        [  1409,  13,  10,  14,    1,   -9 ],   # idx=89  77 'w'
        [  1426,  12,  10,  14,    1,   -9 ],   # idx=90  78 'x'
        [  1441,  12,  14,  14,    1,   -9 ],   # idx=91  79 'y'
        [  1462,   9,  10,  14,    3,   -9 ],   # idx=92  7A 'z'
        [  1474,   5,  18,  14,    5,  -14 ],   # idx=93  7B '{'
        [  1486,   1,  18,  14,    7,  -14 ],   # idx=94  7C '|'
        [  1489,   5,  18,  14,    5,  -14 ],   # idx=95  7D '}'
        [  1501,  10,   3,  14,    2,   -7 ],   # idx=96  7E '~'
        [  1505,  10,  16,  14,    2,  -15 ],   # idx=97  C3, A0 'à'
        [  1525,  14,  19,  14,    0,  -18 ],   # idx=98  C3, 80 'À'
        [  1559,  10,  14,  14,    2,  -13 ],   # idx=99  C3, A4 'ä'
        [  1577,  14,  16,  14,    0,  -15 ],   # idx=100  C3, 84 'Ä'
        [  1605,  10,  16,  14,    2,  -15 ],   # idx=101  C3, A2 'â'
        [  1625,  14,  19,  14,    0,  -18 ],   # idx=102  C3, 82 'Â'
        [  1659,  10,  16,  14,    2,  -15 ],   # idx=103  C3, A9 'é'
        [  1679,  11,  19,  14,    2,  -18 ],   # idx=104  C3, 89 'É'
        [  1706,  10,  16,  14,    2,  -15 ],   # idx=105  C3, A8 'è'
        [  1726,  11,  19,  14,    2,  -18 ],   # idx=106  C3, 88 'È'
        [  1753,  10,  16,  14,    2,  -15 ],   # idx=107  C3, AA 'ê'
        [  1773,  11,  19,  14,    2,  -18 ],   # idx=108  C3, 8A 'Ê'
        [  1800,  10,  14,  14,    2,  -13 ],   # idx=109  C3, AB 'ë'
        [  1818,  11,  16,  14,    2,  -15 ],   # idx=110  C3, 8B 'Ë'
        [  1840,  11,  16,  14,    2,  -15 ],   # idx=111  C3, B4 'ô'
        [  1862,  12,  19,  14,    1,  -18 ],   # idx=112  C3, 94 'Ô'
        [  1891,  11,  14,  14,    2,  -13 ],   # idx=113  C3, B6 'ö'
        [  1911,  12,  16,  14,    1,  -15 ],   # idx=114  C3, 96 'Ö'
        [  1935,   9,  16,  14,    3,  -15 ],   # idx=115  C3, AE 'î'
        [  1953,   7,  19,  14,    4,  -18 ],   # idx=116  C3, 8E 'Î'
        [  1970,  10,  14,  14,    2,   -9 ],   # idx=117  C3, A7 'ç'
        [  1988,  10,  18,  14,    2,  -13 ],   # idx=118  C3, 87 'Ç'
        [  2011,  11,  10,  14,    2,   -9 ],   # idx=119  C2, AB '«'
        [  2025,  11,  10,  14,    2,   -9 ],   # idx=120  C2, BB '»'
        [  2039,  11,  14,  14,    2,   -9 ],   # idx=121  C2, B5 'µ'
        [  2059,  14,  14,  14,    0,  -13 ],   # idx=122  CE, A9 'Ω'
        [  2084,  14,  19,  14,    0,  -18 ],   # idx=123  CF, 80 'π'
        [  2118,  11,  15,  14,    2,  -14 ],   # idx=124  E2, 89, A4 '≤'
        [  2139,  10,  10,  14,    2,   -9 ],   # idx=125  E2, 89, A5 '≥'
        [  2152,   4,   4,  14,    4,  -15 ],   # idx=126  E2, 89, A0 '≠'
        [  2154,  11,  12,  14,    2,  -12 ],   # idx=127  C3, B7 '÷'
        [  2171,   9,  12,  14,    3,  -11 ],   # idx=128  C2, B1 '±'
        [  2185,   7,   7,  14,    4,  -14 ],   # idx=129  C2, B0 '°'
        [  2192,  12,  19,  14,    1,  -18 ],   # idx=130  CB, 9A '˚'
        [  2221,  11,  11,  14,    2,  -11 ],   # idx=131  E2, 98, BC '☼'
        [  2237,   9,  15,  14,    3,  -14 ],   # idx=132  E2, 95, AC '╬'
        [  2254,  12,  15,  14,    1,  -14 ],   # idx=133  E2, 95, AB '╫'
        [  2277,   7,  19,  14,    3,  -14 ],   # idx=134  E2, 95, AA '╪'
        [  2294,   9,  15,  14,    3,  -14 ],   # idx=135  E2, 95, A9 '╩'
        [  2311,  10,  15,  14,    2,  -14 ],   # idx=136  E2, 95, A8 '╨'
        [  2330,  11,  14,  14,    2,   -9 ],   # idx=137  E2, 95, A7 '╧'
        [  2350,   9,  15,  14,    4,  -14 ],   # idx=138  E2, 95, A6 '╦'
        [  2367,  10,  10,  14,    2,   -9 ],   # idx=139  E2, 95, A5 '╥'
        [  2380,  11,  15,  14,    2,  -14 ],   # idx=140  E2, 95, A4 '╤'
        [  2401,  11,  10,  14,    2,   -9 ],   # idx=141  E2, 95, A3 '╣'
        [  2415,  13,  15,  14,    0,  -14 ],   # idx=142  E2, 95, A2 '╢'
        [  2440,  10,  10,  14,    2,   -9 ],   # idx=143  E2, 95, A1 '╡'
        [  2453,   4,   4,  14,    4,  -15 ],   # idx=144  E2, 95, A0 '╠'
        [  2455,  14,   1,  14,    0,    3 ],   # idx=145  E2, 95, 9F '╟'
        [  2457,   9,   6,  14,    3,  -14 ],   # idx=146  E2, 95, 9E '╞'
        [  2464,   3,  18,  14,    5,  -14 ],   # idx=147  E2, 95, 9D '╝'
        [  2471,   9,  18,  14,    3,  -15 ],   # idx=148  E2, 95, 9C '╜'
        [  2492,   3,  18,  14,    7,  -14 ],   # idx=149  E2, 95, 9B '╛'
        [  2499,   9,  14,  14,    3,  -13 ],   # idx=150  E2, 95, 9A '╚'
        [  2515,  12,  14,  14,    1,  -13 ],   # idx=151  E2, 95, 99 '╙'
        [  2536,  12,  14,  14,    1,  -13 ],   # idx=152  E2, 95, 98 '╘'
        [  2557,  14,  14,  14,    0,  -13 ],   # idx=153  E2, 95, 97 '╗'
        [  2582,  14,  14,  14,    0,  -13 ],   # idx=154  E2, 95, 96 '╖'
        [  2607,  12,  14,  14,    1,  -13 ],   # idx=155  E2, 95, 95 '╕'
        [  2628,  11,  14,  14,    2,  -13 ],   # idx=156  E2, 95, 94 '╔'
        [  2648,  10,  14,  14,    2,  -13 ],   # idx=157  E2, 95, 93 '╓'
        [  2666,  12,  14,  14,    2,  -13 ],   # idx=158  E2, 95, 92 '╒'
        [  2687,  12,  17,  14,    1,  -13 ],   # idx=159  E2, 95, 91 '║'
        [  2713,  10,  14,  14,    2,  -13 ],   # idx=160  E2, 95, 90 '═'
        [  2731,  11,  11,  14,    2,  -11 ],   # idx=161  E2, 94, BC '┼'
        [  2747,   8,  15,  14,    3,  -14 ],   # idx=162  E2, 94, B4 '┴'
        [  2762,   8,  15,  14,    3,  -14 ],   # idx=163  E2, 94, B4 '┴'
        [  2777,   5,   7,  14,    3,   -3 ],   # idx=164  E2, 94, AC '┬'
        [  2782,  10,  17,  14,    2,  -14 ],   # idx=165  E2, 94, A4 '┤'
        [  2804,  13,  18,  14,    1,  -15 ],   # idx=166  E2, 94, 9C '├'
        [  2834,  13,  18,  14,    1,  -15 ],   # idx=167  E2, 94, 98 '┘'
        [  2864,  13,  18,  14,    1,  -15 ],   # idx=168  E2, 94, 94 '└'
        [  2894,  13,  18,  14,    1,  -15 ],   # idx=169  E2, 94, 90 '┐'
        [  2924,  13,  18,  14,    1,  -15 ],   # idx=170  E2, 94, 8C '┌'
        [  2954,  13,  18,  14,    1,  -15 ],   # idx=171  E2, 94, 82 '│'
        [  2984,  13,  18,  14,    1,  -15 ],   # idx=172  E2, 94, 80 '─'
        [  3014,  13,  18,  14,    1,  -15 ],   # idx=173  E2, 96, 80 '▀'
        [  3044,  13,  18,  14,    1,  -15 ],   # idx=174  E2, 96, 84 '▄'
        [  3074,  13,  18,  14,    1,  -15 ],   # idx=175  E2, 96, 88 '█'
        [  3104,  13,  18,  14,    1,  -15 ],   # idx=176  E2, 96, 8C '▌'
        [  3134,  13,  18,  14,    1,  -15 ],   # idx=177  E2, 96, 90 '▐'
        [  3164,  10,   6,  14,    3,  -10 ],   # idx=178  E2, 96, AC '▬'
        [  3172,   7,   9,  14,    3,  -17 ],   # idx=179  E2, 96, B2 '▲'
        [  3180,   7,   9,  14,    4,  -13 ],   # idx=180  E2, 96, BA '►'
        [  3188,  13,  15,  14,    1,  -14 ],   # idx=181  E2, 96, BC '▼'
        [  3213,  14,  16,  14,    0,  -15 ],   # idx=182  E2, 97, 84 '◄'
        [  3241,   3,  15,  15,    6,  -10 ],   # idx=183  E2, 96, A1 '□'
        [  3247,  13,  18,  14,    1,  -15 ],   # idx=184  E2, 86, 90 '←'
        [  3277,  13,  18,  14,    1,  -15 ],   # idx=185  E2, 86, 91 '↑'
        [  3307,  13,  18,  14,    1,  -15 ],   # idx=186  E2, 86, 92 '→'
        [  3337,  13,  18,  14,    1,  -15 ],   # idx=187  E2, 86, 93 '↓'
        [  3367,  13,  18,  14,    1,  -15 ],   # idx=188  E2, 86, 94 '↔'
        [  3397,  14,  16,  14,    0,  -15 ],   # idx=189  E2, 97, 84 '◄'
        [  3425,  13,  18,  14,    1,  -15 ]]

# Approx. 4799 bytes
