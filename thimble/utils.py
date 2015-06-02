from cloudinary.uploader import rename

def photo_rename(bucket_link, photos):
	p = ""
	paths = []
	for photo in photos:
		p = photo.split("/")[3]
		p = p.split('#')[0].split('.')[0]
		path = "%s/%s" % (bucket_link, p)
		rename(p, path)
		paths.append(path)
	return paths

	