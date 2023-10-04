# Downloads images used by bubbles_2.py.

import urllib.request

images = [
	("natalie.jpg", "http://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Natalie_Nicholson_at_the_2010_Winter_Olympics.jpg/320px-Natalie_Nicholson_at_the_2010_Winter_Olympics.jpg"),
	("cauldron.jpg", "http://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Olympic_Cauldron_lit_at_2010_Winter_Olympics_opening_ceremony_2.jpg/320px-Olympic_Cauldron_lit_at_2010_Winter_Olympics_opening_ceremony_2.jpg"),
	("canoeing.jpg", "http://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Slalom_canoeing_2012_Olympics_C2_GBR_Timothy_Baillie_and_Etienne_Stott_3.jpg/320px-Slalom_canoeing_2012_Olympics_C2_GBR_Timothy_Baillie_and_Etienne_Stott_3.jpg"),
	("torch.jpg", "http://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Seoul_Olympic_torch.jpg/320px-Seoul_Olympic_torch.jpg")]

for (file, url) in images:
	urllib.request.urlretrieve(url, "bubbles_image_" + file)
