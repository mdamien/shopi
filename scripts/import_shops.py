from django.utils.text import slugify 
import json

from shops.models import Shop

def run():
    Shop.objects.all().delete()

    easy = "title->name site->website adresse->address tel->phone horaires->timetable content->description category->categories private_mail->email"
    easy = list(s.split("->") for s in easy.split())

    shops = json.load(open('scripts/shops.json'))
    for shop in shops:
        data = { dest:shop.get(src,'') for src,dest in easy }
        if len(shop.get('latitude','')) > 1:
            data['lat'] = float(shop['latitude'])
        if len(shop.get('longitude','')) > 1:
            data['lng'] = float(shop['longitude'])
        try:
            data['slug'] = slugify(data['name'])
        except:
            import pdb;pdb.set_trace()
        Shop(**data).save()
        print("%s OK" % data['name'])
