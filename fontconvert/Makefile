all: fontconvert

CC     = gcc -g
CFLAGS = -Wall -I/usr/local/include/freetype2 -I/usr/include/freetype2 -I /usr/local/include/freetype2/freetype -I/usr/include
LIBS   = -lfreetype

fontconvert: fontconvert.c
	$(CC) $(CFLAGS) $< $(LIBS) -o $@
#	strip $@

fcv:    f.c
	$(CC) $(CFLAGS) $< $(LIBS) -o $@

clean:
	rm -f fontconvert
