from pygal.maps.world import World

wm = World()
wm.title = "North, Central and South america"

wm.add("North America", ['ca', 'mx', 'us'])
wm.add("Central America", ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add("South America", ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file("americas.svg")

https://hst-api.wialon.com/wialon/ajax.html?svc=token/login&params={“token”:”35249e720beadfe05758af363ebcacef62FA3F9A2B06C9A10C91F0B70DECB537520A40A3”}



https://hst-api.wialon.com/wialon/ajax.html?svc=core/search_items&params={"spec":{"itemsType":"avl_unit","propName":"sys_name","propValueMask":"*","sortType":"sys_name"},"force":”1”,"flags":”1024”,"from":”0”,"to":”0”}&sid=