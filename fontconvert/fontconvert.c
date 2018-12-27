/* TrueType to Adafruit_GFX font converter.  Derived from Peter Jakobs' Adafruit_ftGFX fork & makefont tool, and Paul Kourany's Adafruit_mfGFX.


D.J.P.  Dec 2018
        Modified for python3 micropython code
        Add UTF-8 character code.
        Create python module instead of c Header




NOT AN ARDUINO SKETCH.  This is a command-line tool for preprocessing
fonts to be used with the Adafruit_GFX Arduino library.

For UNIX-like systems.  Outputs to stdout; redirect to header file, e.g.:
  ./fontconvert ~/Library/Fonts/FreeSans.ttf 18 > FreeSans18pt7b.py

REQUIRES FREETYPE LIBRARY.  www.freetype.org

Currently this only extracts the printable 7-bit ASCII chars of a font.
Will eventually extend with some int'l chars a la ftGFX, not there yet.
Keep 7-bit fonts around as an option in that case, more compact.

See notes at end for glyph nomenclature & other tidbits.



*/

#ifndef ARDUINO

#include <stdio.h>
#include <ctype.h>
#include <stdint.h>
#include <ft2build.h>
#include FT_GLYPH_H
#include "../gfxfont.h" // Adafruit_GFX font structures
#include <stdlib.h>
#include <stdint.h>
#include <ftdriver.h>
#include <locale.h>

#define DPI 141 // Approximate res. of Adafruit 2.8" TFT


// table of font to convert
char *List = "ÉC !\"#$%&'()*+,-./0123456789:;<=>?@"\
          "ABCDEFGHIJKLMNOPQRSTUVWXYZ"\
          "[\\]^_`"\
          "abcdefghijklmnopqrstuvwxyz"\
          "{|}~"\
          "àÀäÄâÂéÉèÈêÊëËôÔöÖîÎçÇ«»"\
          "µΩπ≤≥≠÷±°˚☼"\
          "╬╫╪╩╨╧╦╥╤╣╢╡╠╟╞╝╜╛╚╙╘╗╖╕╔╓╒║═┼┴┴┬┤├┘└┐┌│─"\
          "▀▄█▌▐▬▲►▼◄□←↑→↓↔◄\0";

typedef uint8_t  utf8_char[5];

utf8_char * utf8_List=NULL;


/*
Number
of bytes        Bits for
code point      First
code point      Last
code point      Byte 1  Byte 2   Byte 3 Byte 4
1       7       U+0000  U+007F   0xxxxxxx
2       11      U+0080  U+07FF   110xxxxx       10xxxxxx
3       16      U+0800  U+FFFF   1110xxxx       10xxxxxx        10xxxxxx
4       21      U+10000 U+10FFFF 11110xxx       10xxxxxx        10xxxxxx        10xxxxxx
*/



uint8_t myUtf8Char[5]={0,0,0,0,0};


// utf8_strlen and utf8_to_utf32 
//took from https://codereview.stackexchange.com/questions/197548/convert-utf8-string-to-utf32-string-in-c

size_t utf8_strlen(uint8_t* text) {
    size_t i = 0;
    size_t num_chars = 0;

    while (text[i] != 0) {
        num_chars++;

        if ((text[i] & 0b10000000) == 0) {
            // 1 byte code point, ASCII
            i += 1;
        }
        else if ((text[i] & 0b11100000) == 0b11000000) {
            // 2 byte code point
            i += 2;
        }
        else if ((text[i] & 0b11110000) == 0b11100000) {
            // 3 byte code point
            i += 3;
        }
        else {
            // 4 byte code point
            i += 4;
        }
    }

    return num_chars;
}


uint32_t utf8_to_utf32(uint8_t* text) {
    size_t num_chars = utf8_strlen(text);
    uint32_t utf32V=0;
    uint8_t* c = (uint8_t *) &utf32V;
    size_t i = 0;

    for (size_t n = 0; n < num_chars; n++) {
        if ((text[i] & 0b10000000) == 0) {
            // 1 byte code point, ASCII
            c[n] = (text[i] & 0b01111111);
            i += 1;
        }
        else if ((text[i] & 0b11100000) == 0b11000000) {
            // 2 byte code point
            c[n] = (text[i] & 0b00011111) << 6 | (text[i + 1] & 0b00111111);
            i += 2;
        }
        else if ((text[i] & 0b11110000) == 0b11100000) {
            // 3 byte code point
            c[n] = (text[i] & 0b00001111) << 12 | (text[i + 1] & 0b00111111) << 6 | (text[i + 2] & 0b00111111);
            i += 3;
        }
        else {
            // 4 byte code point
            c[n] = (text[i] & 0b00000111) << 18 | (text[i + 1] & 0b00111111) << 12 | (text[i + 2] & 0b00111111) << 6 | (text[i + 3] & 0b00111111);
            i += 4;
        }
    }

    return utf32V;
}



// extract each utf-8 character from * char
// return next utf-8 character pointer
// unicodeTable contains the utf-8 string representing the character 
char * decodeunicode(char *pt, uint8_t *unicodeTable)
{
   int i;
   int index=0;
   int nbByte=1;
   int invalid=1;
    do
   {

    if(invalid)
     {
       for(i=0;i<5;i++)
          unicodeTable[i]=0;
       index=0;
       invalid=0;
     }

     unicodeTable[index]=*pt;
     if(index == 0)
       {
           // first character
               if((*pt & 0x80)==0) // only one character
                   return ++pt;
               if((*pt &  0xE0) == 0xC0) //ok 2 bytes
                    nbByte=1;
               else if((*pt &  0xF0) == 0xE0) // ok 3bytes
                    nbByte = 2;
               else if((*pt & 0xF8) ==  0xF0) // ok 4 bytes
                    nbByte = 3;
               else
                  invalid= 1;
        }
      else
        {
            if((*pt & 0xC0) == 0x80) // ok valid
              {
                if(nbByte == index)
                  return ++pt;
              }
            else
                invalid=1;
        }
     index++;
   }while(*(++pt));
       for(i=0;i<4;i++)
          unicodeTable[i]=0;

 return pt;
}

// indexUtf8Char
// convert the char pointer KList to a array of utf8 character
// return the number of utf8 character

int   indexUtf8Char(char * src , utf8_char * utf8Table)
{
   int i;

   for(i=0;;i++)
   {
    src = decodeunicode(src,utf8Table[i]);
    if(*src==0) break;
   }
  return i+1;
}


void printUtf8Char(utf8_char value)
{
   char * pt = (char *) &value[0];
   printf(" %02X",*pt);

    while(*(++pt))
   {
     printf(", %02X",*pt);
   }

   printf(" '%s'",&value[0]);
}



// Accumulate bits for output, with periodic hexadecimal byte write
void enbit(uint8_t value) {
	static uint8_t row = 0, sum = 0, bit = 0x80, firstCall = 1;
	if(value) sum |= bit;    // Set bit if needed
	if(!(bit >>= 1)) {       // Advance to next bit, end of byte reached?
		if(!firstCall) { // Format output table nicely
			if(++row >= 12) {        // Last entry on line?
				printf(",\n      "); //   Newline format output
				row = 0;         //   Reset row counter
			} else {                 // Not end of line
				printf(", ");    //   Simple comma delim
			}
		}
		printf("0x%02X", sum); // Write byte value
		sum       = 0;         // Clear for next byte
		bit       = 0x80;      // Reset bit counter
		firstCall = 0;         // Formatting flag
	}
}

int main(int argc, char *argv[]) {
	int                i, j, err, size, first=' ', last='~',
	                   bitmapOffset = 0, x, y, byte;
	char              *fontName, c, *ptr;
	FT_Library         library;
	FT_Face            face;
	FT_Glyph           glyph;
	FT_Bitmap         *bitmap;
	FT_BitmapGlyphRec *g;
	GFXglyph          *table;
	uint8_t            bit;




	// Parse command line.  Valid syntaxes are:
	//   fontconvert [filename] [size]
	//   fontconvert [filename] [size] [last char]
	//   fontconvert [filename] [size] [first char] [last char]
	// Unless overridden, default first and last chars are
	// ' ' (space) and '~', respectively

	if(argc < 3) {
		fprintf(stderr, "Usage: %s fontfile size \n",
		  argv[0]);
		return 1;
	}


        setlocale(LC_ALL, "");

        if (!setlocale(LC_CTYPE, ""))
         {
           fprintf(stderr, "Locale not specified. Check LANG, LC_CTYPE, LC_ALL\n");
          return 2;
         }



       // calculate the number of character
       // assume that the list is the maximum of character possible
       // convert char * to  array of utf8_char

       utf8_List = (utf8_char *) malloc(sizeof(utf8_char) * strlen(List));
       first = 0;
       last  =  indexUtf8Char(List,utf8_List);



	size = atoi(argv[2]);

	ptr = strrchr(argv[1], '/'); // Find last slash in filename
	if(ptr) ptr++;         // First character of filename (path stripped)
	else    ptr = argv[1]; // No path; font in local dir.

	// Allocate space for font name and glyph table
	if((!(fontName = malloc(strlen(ptr) + 20))) ||
	   (!(table = (GFXglyph *)malloc((last - first + 1) *
	    sizeof(GFXglyph))))) {
		fprintf(stderr, "Malloc error\n");
		return 1;
	}

	// Derive font table names from filename.  Period (filename
	// extension) is truncated and replaced with the font size & bits.
	strcpy(fontName, ptr);
	ptr = strrchr(fontName, '.'); // Find last period (file ext)
	if(!ptr) ptr = &fontName[strlen(fontName)]; // If none, append
	// Insert font size and 7/8 bit.  fontName was alloc'd w/extra
	// space to allow this, we're not sprintfing into Forbidden Zone.
	sprintf(ptr, "%dpt%db", size, (last > 127) ? 8 : 7);
	// Space and punctuation chars in name replaced w/ underscores.  
	for(i=0; (c=fontName[i]); i++) {
		if(isspace(c) || ispunct(c)) fontName[i] = '_';
	}

	// Init FreeType lib, load font
	if((err = FT_Init_FreeType(&library))) {
		fprintf(stderr, "FreeType init error: %d", err);
		return err;
	}


	// Use TrueType engine version 35, without subpixel rendering.
	// This improves clarity of fonts since this library does not
	// support rendering multiple levels of gray in a glyph.
	// See https://github.com/adafruit/Adafruit-GFX-Library/issues/103
	FT_UInt interpreter_version = TT_INTERPRETER_VERSION_35;
	FT_Property_Set( library, "truetype",
                                  "interpreter-version",
                                  &interpreter_version );

	if((err = FT_New_Face(library, argv[1], 0, &face))) {
		fprintf(stderr, "Font load error: %d", err);
		FT_Done_FreeType(library);
		return err;
	}

	// << 6 because '26dot6' fixed-point format
	FT_Set_Char_Size(face, size << 6, 0, DPI, 0);
        FT_Select_Charmap(face , ft_encoding_unicode);

	// Currently all symbols from 'first' to 'last' are processed.
	// Fonts may contain WAY more glyphs than that, but this code
	// will need to handle encoding stuff to deal with extracting
	// the right symbols, and that's not done yet.
	// fprintf(stderr, "%ld glyphs\n", face->num_glyphs);
        printf("from PFx_Font import PFx_Font\n");
	printf("class %s(PFx_Font):\n\n", fontName);

        printf("    def __init__(self):\n");
        printf("        super().__init__(self.bitmap,self.index,self.glyph)\n\n");

        printf("    bitmap=bytes([\n      ");

	// Process glyphs and output huge bitmap data array
	for(i=first,j=0;i<=last ; i++,j++) {
		// MONO renderer provides clean image with perfect crop
		// (no wasted pixels) via bitmap struct.



		if((err = FT_Load_Char(face,utf8_to_utf32(&utf8_List[i][0]), FT_LOAD_TARGET_MONO))) {
//		if((err = FT_Load_Char(face,utf8_List[i][0], FT_LOAD_TARGET_MONO))) {
			fprintf(stderr, "Error %d loading char '%c'\n",
			  err, i);
			continue;
		}

		if((err = FT_Render_Glyph(face->glyph,
		  FT_RENDER_MODE_MONO))) {
			fprintf(stderr, "Error %d rendering char '%c'\n",
			  err, i);
			continue;
		}

		if((err = FT_Get_Glyph(face->glyph, &glyph))) {
			fprintf(stderr, "Error %d getting glyph '%c'\n",
			  err, i);
			continue;
		}

		bitmap = &face->glyph->bitmap;
		g      = (FT_BitmapGlyphRec *)glyph;

		// Minimal font and per-glyph information is stored to
		// reduce flash space requirements.  Glyph bitmaps are
		// fully bit-packed; no per-scanline pad, though end of
		// each character may be padded to next byte boundary
		// when needed.  16-bit offset means 64K max for bitmaps,
		// code currently doesn't check for overflow.  (Doesn't
		// check that size & offsets are within bounds either for
		// that matter...please convert fonts responsibly.)
		table[j].bitmapOffset = bitmapOffset;
		table[j].width        = bitmap->width;
		table[j].height       = bitmap->rows;
		table[j].xAdvance     = face->glyph->advance.x >> 6;
		table[j].xOffset      = g->left;
		table[j].yOffset      = 1 - g->top;

		for(y=0; y < bitmap->rows; y++) {
			for(x=0;x < bitmap->width; x++) {
				byte = x / 8;
				bit  = 0x80 >> (x & 7);
				enbit(bitmap->buffer[
				  y * bitmap->pitch + byte] & bit);
			}
		}

		// Pad end of char bitmap to next byte boundary if needed
		int n = (bitmap->width * bitmap->rows) & 7;
		if(n) { // Pixel count not an even multiple of 8?
			n = 8 - n; // # bits to next multiple
			while(n--) enbit(0);
		}
		bitmapOffset += (bitmap->width * bitmap->rows + 7) / 8;

		FT_Done_Glyph(glyph);
	}

	printf("])\n\n"); // End bitmap array



        // utf8 to index 
       printf("    index = {\n");

       for(i=first ; i<last;i++) 
         {
          // deal with " character
          if(utf8_to_utf32(&utf8_List[i][0]) == '"')
            printf("        '\"':%d",i);
          else
           {
            // deal with \ character
              if(utf8_to_utf32(&utf8_List[i][0]) == '\\')
            printf("        \"\\\\\":%d",i);
            else
            printf("        \"%s\":%d",&utf8_List[i][0],i);
           }
          if(i < (last-1))
            printf(",");
          else
            printf("}");
          printf("\n");
         }
         printf("\n\n");


	// Output glyph attributes table (one per character)
	printf("    glyph=[\n");
	for(i=first, j=0; i<=last; i++, j++) {
		printf("        [ %5d, %3d, %3d, %3d, %4d, %4d ]",
		  table[j].bitmapOffset,
		  table[j].width,
		  table[j].height,
		  table[j].xAdvance,
		  table[j].xOffset,
		  table[j].yOffset);
		if(i < last) {
                        printf(",   # idx=%d ",i);
                        printUtf8Char(utf8_List[i]);
			putchar('\n');
		}
	}
	printf("]");
//	if((last >= ' ') && (last <= '~')) printf(" '%c'", last);
	printf("\n\n");
/*
	// Output font structure
	printf("const GFXfont %s PROGMEM = {\n", fontName);
	printf("  (uint8_t  *)%sBitmaps,\n", fontName);
	printf("  (GFXglyph *)%sGlyphs,\n", fontName);
	if (face->size->metrics.height == 0) {
      // No face height info, assume fixed width and get from a glyph.
		printf("  0x%02X, 0x%02X, %d };\n\n",
			first, last, table[0].height);
	} else {
		printf("  0x%02X, 0x%02X, %ld };\n\n",
			first, last, face->size->metrics.height >> 6);
	}
*/	printf("# Approx. %d bytes\n",
	  bitmapOffset + (last - first + 1) * 7 + 7);
	// Size estimate is based on AVR struct and pointer sizes;
	// actual size may vary.

	FT_Done_FreeType(library);

	return 0;
}

/* -------------------------------------------------------------------------

Character metrics are slightly different from classic GFX & ftGFX.
In classic GFX: cursor position is the upper-left pixel of each 5x7
character; lower extent of most glyphs (except those w/descenders)
is +6 pixels in Y direction.
W/new GFX fonts: cursor position is on baseline, where baseline is
'inclusive' (containing the bottom-most row of pixels in most symbols,
except those with descenders; ftGFX is one pixel lower).

Cursor Y will be moved automatically when switching between classic
and new fonts.  If you switch fonts, any print() calls will continue
along the same baseline.

                    ...........#####.. -- yOffset
                    ..........######..
                    ..........######..
                    .........#######..
                    ........#########.
   * = Cursor pos.  ........#########.
                    .......##########.
                    ......#####..####.
                    ......#####..####.
       *.#..        .....#####...####.
       .#.#.        ....##############
       #...#        ...###############
       #...#        ...###############
       #####        ..#####......#####
       #...#        .#####.......#####
====== #...# ====== #*###.........#### ======= Baseline
                    || xOffset

glyph->xOffset and yOffset are pixel offsets, in GFX coordinate space
(+Y is down), from the cursor position to the top-left pixel of the
glyph bitmap.  i.e. yOffset is typically negative, xOffset is typically
zero but a few glyphs will have other values (even negative xOffsets
sometimes, totally normal).  glyph->xAdvance is the distance to move
the cursor on the X axis after drawing the corresponding symbol.

There's also some changes with regard to 'background' color and new GFX
fonts (classic fonts unchanged).  See Adafruit_GFX.cpp for explanation.
*/

#endif /* !ARDUINO */
