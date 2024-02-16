import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sales_project.settings")
django.setup()

# from sales_rest.models import AutomobileVO

# def get_sales():
# url = "http://project-beta-inventory-api-1:8000/api/automobiles/"
# response = requests.get(url)
# print(response.status_code)
# content = json.loads(response.content)

# for auto in content["autos"]:
# AutomobileVO.objects.update_or_create(
# import_href=auto["href"],
# defaults={
# "color":auto["color"],
# "year":auto["year"],
# "vin":auto["vin"],
# "model":auto["model"]["name"],
# "picture_url":auto["model"]["picture_url"],
# "manufacturer":auto["model"]["manufacturer"]["name"],
# }
# )


def poll():
    while True:
        print('Sales poller polling for data')
        try:
            get_sales()

        except Exception as e:
            print(e, file=sys.stderr)

        time.sleep(60)


if __name__ == "__main__":
    poll()
