from cloudinary.uploader import rename

def photo_rename(bucket_link, photos):
	p = ""
	for photo in photos:
		p = photo.split("/")[3]
		p = p.split('#')[0].split('.')[0]
		rename(p, "%s/%s" % (bucket_link, p))
		
	if len(photos) == 1:
		return p