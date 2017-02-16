# Find original (or bigger size) images with extend=True

import haul
import urllib.request

url = 'https://pixabay.com/en/photos/?q=computer&image_type=&cat=&min_width=&min_height='
result = haul.find_images(url, extend=True)

urls = result.image_urls

# print(urls[1])

for url in urls:
    if url.endswith('.jpg'):
        filename = url.split('/')[-1].split('.')[0]
        f = open(filename+'.jpg', 'wb')
        f.write(urllib.request.urlopen(url).read())
        f.close()
    elif url.endswith('.png'):
        filename = url.split('/')[-1].split('.')[0]
        f = open(filename + '.png', 'wb')
        f.write(urllib.request.urlopen(url).read())
        f.close()

print('Done with Extend = True')
