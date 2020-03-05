from home import *

code = input('enter insta post code to continue : ')

list_view(Insta(shortcode).get_images())
print(Insta(shortcode).get_desc())
list_view(Insta(shortcode).get_videos())
