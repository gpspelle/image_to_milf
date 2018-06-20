import sys
from PIL import Image

if len(sys.argv) > 2:
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    im = Image.open(input_filename)

    f = open(output_filename, 'w');

    print("> Image size: ")
    print(im.size)
    print("")
    w = im.size[0]
    h = im.size[1]

    print("> Writing to file: "+ output_filename)

    f.write("DEPTH = %d;" % (w * h))
    f.write("WIDTH = 3;")
    f.write("ADDRESS_RADIX = HEX;")
    f.write("DATA_RADIX = BIN;")
    f.write("CONTENT")
    f.write("BEGIN\n")

    index = 0;
    for x in range(0, w):
        for y in range(0, h):
            r = int(im.getpixel((x, y))[0]/128)
            g = int(im.getpixel((x, y))[1]/128)
            b = int(im.getpixel((x, y))[2]/128)

            f.write(hex(index)[2:] + ":\t"+ str(r) + str(g) + str(b) +";\n")
            index += 1
                

    f.write("END;")
    print(">>> DONE");

else:
    print("NEED MOAR INFO")
