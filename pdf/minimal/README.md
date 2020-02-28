# Minimal PDF

## File Format

Getting in touch with the PDF file format and to start with an easy example I took `https://brendanzagaeski.appspot.com/0004.html` and `https://brendanzagaeski.appspot.com/0005.html`.

```
$ hexdump -C file.pdf
00000000  25 50 44 46 2d 31 2e 31  0a 25 c2 a5 c2 b1 c3 ab  |%PDF-1.1.%......|
00000010  0a 0a 31 20 30 20 6f 62  6a 0a 20 20 3c 3c 20 2f  |..1 0 obj.  << /|
00000020  54 79 70 65 20 2f 43 61  74 61 6c 6f 67 0a 20 20  |Type /Catalog.  |
00000030  20 20 20 2f 50 61 67 65  73 20 32 20 30 20 52 0a  |   /Pages 2 0 R.|
00000040  20 20 3e 3e 0a 65 6e 64  6f 62 6a 0a 0a 32 20 30  |  >>.endobj..2 0|
00000050  20 6f 62 6a 0a 20 20 3c  3c 20 2f 54 79 70 65 20  | obj.  << /Type |
00000060  2f 50 61 67 65 73 0a 20  20 20 20 20 2f 4b 69 64  |/Pages.     /Kid|
00000070  73 20 5b 33 20 30 20 52  5d 0a 20 20 20 20 20 2f  |s [3 0 R].     /|
00000080  43 6f 75 6e 74 20 31 0a  20 20 20 20 20 2f 4d 65  |Count 1.     /Me|
00000090  64 69 61 42 6f 78 20 5b  30 20 30 20 33 30 30 20  |diaBox [0 0 300 |
000000a0  31 34 34 5d 0a 20 20 3e  3e 0a 65 6e 64 6f 62 6a  |144].  >>.endobj|
000000b0  0a 0a 33 20 30 20 6f 62  6a 0a 20 20 3c 3c 20 20  |..3 0 obj.  <<  |
000000c0  2f 54 79 70 65 20 2f 50  61 67 65 0a 20 20 20 20  |/Type /Page.    |
000000d0  20 20 2f 50 61 72 65 6e  74 20 32 20 30 20 52 0a  |  /Parent 2 0 R.|
000000e0  20 20 20 20 20 20 2f 52  65 73 6f 75 72 63 65 73  |      /Resources|
000000f0  0a 20 20 20 20 20 20 20  3c 3c 20 2f 46 6f 6e 74  |.       << /Font|
00000100  0a 20 20 20 20 20 20 20  20 20 20 20 3c 3c 20 2f  |.           << /|
00000110  46 31 0a 20 20 20 20 20  20 20 20 20 20 20 20 20  |F1.             |
00000120  20 20 3c 3c 20 2f 54 79  70 65 20 2f 46 6f 6e 74  |  << /Type /Font|
00000130  0a 20 20 20 20 20 20 20  20 20 20 20 20 20 20 20  |.               |
00000140  20 20 20 2f 53 75 62 74  79 70 65 20 2f 54 79 70  |   /Subtype /Typ|
00000150  65 31 0a 20 20 20 20 20  20 20 20 20 20 20 20 20  |e1.             |
00000160  20 20 20 20 20 2f 42 61  73 65 46 6f 6e 74 20 2f  |     /BaseFont /|
00000170  54 69 6d 65 73 2d 52 6f  6d 61 6e 0a 20 20 20 20  |Times-Roman.    |
00000180  20 20 20 20 20 20 20 20  20 20 20 3e 3e 0a 20 20  |           >>.  |
00000190  20 20 20 20 20 20 20 20  20 3e 3e 0a 20 20 20 20  |         >>.    |
000001a0  20 20 20 3e 3e 0a 20 20  20 20 20 20 2f 43 6f 6e  |   >>.      /Con|
000001b0  74 65 6e 74 73 20 34 20  30 20 52 0a 20 20 3e 3e  |tents 4 0 R.  >>|
000001c0  0a 65 6e 64 6f 62 6a 0a  0a 34 20 30 20 6f 62 6a  |.endobj..4 0 obj|
000001d0  0a 20 20 3c 3c 20 2f 4c  65 6e 67 74 68 20 35 35  |.  << /Length 55|
000001e0  20 3e 3e 0a 73 74 72 65  61 6d 0a 20 20 42 54 0a  | >>.stream.  BT.|
000001f0  20 20 20 20 2f 46 31 20  31 38 20 54 66 0a 20 20  |    /F1 18 Tf.  |
00000200  20 20 30 20 30 20 54 64  0a 20 20 20 20 28 48 65  |  0 0 Td.    (He|
00000210  6c 6c 6f 20 57 6f 72 6c  64 29 20 54 6a 0a 20 20  |llo World) Tj.  |
00000220  45 54 0a 65 6e 64 73 74  72 65 61 6d 0a 65 6e 64  |ET.endstream.end|
00000230  6f 62 6a 0a 0a 78 72 65  66 0a 30 20 35 0a 30 30  |obj..xref.0 5.00|
00000240  30 30 30 30 30 30 30 30  20 36 35 35 33 35 20 66  |00000000 65535 f|
00000250  20 0a 30 30 30 30 30 30  30 30 31 38 20 30 30 30  | .0000000018 000|
00000260  30 30 20 6e 20 0a 30 30  30 30 30 30 30 30 37 37  |00 n .0000000077|
00000270  20 30 30 30 30 30 20 6e  20 0a 30 30 30 30 30 30  | 00000 n .000000|
00000280  30 31 37 38 20 30 30 30  30 30 20 6e 20 0a 30 30  |0178 00000 n .00|
00000290  30 30 30 30 30 34 35 37  20 30 30 30 30 30 20 6e  |00000457 00000 n|
000002a0  20 0a 74 72 61 69 6c 65  72 0a 20 20 3c 3c 20 20  | .trailer.  <<  |
000002b0  2f 52 6f 6f 74 20 31 20  30 20 52 0a 20 20 20 20  |/Root 1 0 R.    |
000002c0  20 20 2f 53 69 7a 65 20  35 0a 20 20 3e 3e 0a 73  |  /Size 5.  >>.s|
000002d0  74 61 72 74 78 72 65 66  0a 35 36 35 0a 25 25 45  |tartxref.565.%%E|
000002e0  4f 46 0a                                          |OF.|
000002e3
```


### PDF Header

The header consists of the version string (`%PDF-1.1`) in the first line. Second line holds a comment (comments starting with `%` in the line) with at least four high bit characters (in this example there are 6 characters). High bit characters are bytes with most significatn bit set. They are used to determine whether to treat the file’s contents as text or as binary.

```
00000000  25 50 44 46 2d 31 2e 31  0a 25 c2 a5 c2 b1 c3 ab  |%PDF-1.1.%......|
00000010  0a 0a                                             |..              |
```

```
>>> [format(c, "08b") for c in bytes.fromhex("c2a5c2b1c3ab")]
['11000010', '10100101', '11000010', '10110001', '11000011', '10101011']
```

As far as I know the header must be within the first 1024 bytes of the document. For that reason it is okay to add some prefix in front of the PDF starting tag. However, some pdf readers may warn (like `zathura`) and some other information inside the PDF (like the xref table) musst be adjusted.


### PDF Body

The PDF body holds objects that may or may not referring to each other.


### Xref table

In addition there is the xref table, and an information about the beginning ot that PDF (which esentially is the beginning of the xref table). The xref table holds the offset of objects. The offset is stored as the number of bytes before the referenced object inside the complete file.

The xref table is not explicitly indexed but the order is important as the position inside the xref table determines the object id referring to (starting at 0). A `f` indicates a not used object, otherwise a `n` indicates a object beeing used somewhere.

And, according to Julia Wolf, the xref table is not actually as necessary as the spec says.


## File Format Requirements

The header must be withing the first 1024 bytes (citation needed). The xref table must hold valid offsets (by design), but most readers are okay when they are not valid, so the reader builds their own xref table reading the whole PDF.

######

When adding something as prefix of the minimal PDF the following elements have to be recomputed:
- xref entries
- byte offset stored after `startxref`

Removing objects require also removing the xref entry. All ids after that must be adjusted or this single entry must be set to unused (`f`) which probably is also okay except that it might be detectable...
