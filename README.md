# Usage

$ python3 image_parser.py <path_to_mif> <path_to_output/output_name.format>

Note that .format = {.png, .jpg, etc}.
Also, you may need to change image resolution, the hardcoded default value is 
DEPTH = 640 x 480 = 307200.
You need to change it to:
DEPTH = x_res * y_res.

Where x_res and y_res are the resolution of your image. 

# Troubles

If your output image is inverted and repeated over the screen, you may be using this mif file in reversed order,
you're reading it collum by collum and you perhaps should read it row by row. 
