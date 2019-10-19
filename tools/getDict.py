arcaea_url_list = {
    'Arcaea': 'https://vignette.wikia.nocookie.net/iowiro/images/7/7d/Pack-arcaea.png/',
    'Adverse Prelude': 'https://vignette.wikia.nocookie.net/iowiro/images/2/23/Pack_AP.png/',
    'Luminous Sky': 'https://vignette.wikia.nocookie.net/iowiro/images/e/e9/Luminous_sky.png/',
    'Vicious Labyrinth': 'https://vignette.wikia.nocookie.net/iowiro/images/3/34/Pack-viciouslabyrinth.png/',
    'Eternal Core': 'https://vignette.wikia.nocookie.net/iowiro/images/1/17/Pack-eternalcore.png/',
    'Sunset Radiance': 'https://vignette.wikia.nocookie.net/iowiro/images/e/ed/Pack-sunsetradiance.png/',
    'Absolute Reason': 'https://vignette.wikia.nocookie.net/iowiro/images/2/21/Pack-absolutereason.png/',
    'Binary Enfold': 'https://vignette.wikia.nocookie.net/iowiro/images/8/86/Pack-binaryenfold.png/',
    'Ambivalent Vision': 'https://vignette.wikia.nocookie.net/iowiro/images/9/99/Pack-ambivalentvision.png/',
    'Crimson Solace': 'https://vignette.wikia.nocookie.net/iowiro/images/2/2e/Pack-crimsonsolace.png/',
    'CHUNITHM Collaboration': 'https://vignette.wikia.nocookie.net/iowiro/images/a/a0/Pack_CHUNITHM.png/',
    'Groove Coaster Collaboration': 'https://vignette.wikia.nocookie.net/iowiro/images/2/23/Pack_groove_coaster.png/',
    'Tone Sphere Collaboration': 'https://vignette.wikia.nocookie.net/iowiro/images/e/e4/Tone_sphere_collaboration_pack.jpg/',
    'Lanota Collaboration': 'https://vignette.wikia.nocookie.net/iowiro/images/8/80/Pack-lanota.png/',
    'Stellights Collaboration': 'https://vignette.wikia.nocookie.net/iowiro/images/9/9d/Pack-stellights.png/',
    'Dynamix Collaboration': 'https://vignette.wikia.nocookie.net/iowiro/images/c/c6/Pack-dynamix.png',
    'Memory Archive': 'https://vignette.wikia.nocookie.net/iowiro/images/6/66/Pack-memoryarchive.png/'
    }

cytus2_url_list = {
    'Paff': 'https://vignette.wikia.nocookie.net/cytus/images/9/96/Paff_Logo.png/revision/latest/scale-to-width-down/100?cb=20190701061057',
    'NEKO#ΦωΦ': 'https://vignette.wikia.nocookie.net/cytus/images/0/00/Neko_Logo.png/revision/latest/scale-to-width-down/100?cb=20180121105714',
    'ROBO_Head': 'https://vignette.wikia.nocookie.net/cytus/images/2/24/ROBO_Head_Logo.png/revision/latest/scale-to-width-down/100?cb=20180121105714',
    'Ivy': 'https://vignette.wikia.nocookie.net/cytus/images/4/4d/Ivy%27s_logo.png/revision/latest/scale-to-width-down/100?cb=20190113100008',
    'Miku': 'https://vignette.wikia.nocookie.net/cytus/images/c/ca/Miku_Logo.png/revision/latest/scale-to-width-down/100?cb=20190531143142',
    'Xenon': 'https://vignette.wikia.nocookie.net/cytus/images/6/65/Xenon_Logo.png/revision/latest?cb=20180121105713',
    'ConneR': 'https://vignette.wikia.nocookie.net/cytus/images/6/61/ConneR_Logo.png/revision/latest/scale-to-width-down/100?cb=20180121105714',
    'Cherry': 'https://vignette.wikia.nocookie.net/cytus/images/7/72/Cherry_Logo.png/revision/latest/scale-to-width-down/180?cb=20180309162205',
    'Joe': 'https://vignette.wikia.nocookie.net/cytus/images/5/52/68d7232784f8f125afde723b8c698bea1adc97bacb45e55abb0e2f63e35772c4046c9c191a95878cb6252683c58ab450628c2038fb89af4a9954fcf31395d29a6e9139c4e44e8968643edd639a142ee3.png/revision/latest?cb=20181007133420',
    'Aroma': 'https://vignette.wikia.nocookie.net/cytus/images/e/e3/Aroma_Logo.png/revision/latest?cb=20181007160910',
    'Nora': 'https://vignette.wikia.nocookie.net/cytus/images/f/fb/Nora_Logo.png/revision/latest?cb=20181101015219',
    'Neko': 'https://vignette.wikia.nocookie.net/cytus/images/e/e0/Neko_Logo2.png/revision/latest?cb=20190701045301'
    }

err_msg = {
    'no_result': "No search results found. Please search correct song name.",
    'unknown': "Unknown error occured.",
    'out_of_index': "Out of index. Input existing list number.",
    'value_error': "Input existing level.",
    'usage_random': "Usage: random [arcaea/cytus2/dynamix] (level)",
    'usage_songlist': "Usage: songlist [arcaea/cytus2/dynamix] [listnumber]"
    }

def arcaea():
    return arcaea_url_list
def cytus2():
    return cytus2_url_list
def err():
    return err_msg
