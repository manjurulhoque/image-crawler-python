from haul import Haul
from haul.compat import str
import json


def img_data_src_finder(pipeline_index,
                        soup,
                        finder_image_urls=[],
                        *args, **kwargs):
    """
    Find image URL in <img>'s data-src attribute
    """

    now_finder_image_urls = []

    for img in soup.find_all('img'):
        src = img.get('data-src', None)
        if src:
            src = str(src)
            now_finder_image_urls.append(src)

    output = {}
    output['finder_image_urls'] = finder_image_urls + now_finder_image_urls

    return output


MY_FINDER_PIPELINE = (
    'haul.finders.pipeline.html.img_src_finder',
    'haul.finders.pipeline.css.background_image_finder',
    img_data_src_finder,
)

GOOGLE_SITES_EXTENDER_PIEPLINE = (
    'haul.extenders.pipeline.google.blogspot_s1600_extender',
    'haul.extenders.pipeline.google.ggpht_s1600_extender',
    'haul.extenders.pipeline.google.googleusercontent_s1600_extender',
)

url = 'https://pixabay.com/en/photos/?q=computer&image_type=&cat=&min_width=&min_height='
h = Haul(parser='lxml', finder_pipeline=MY_FINDER_PIPELINE, extender_pipeline=GOOGLE_SITES_EXTENDER_PIEPLINE)
result = h.find_images(url, extend=True)
print(result)
