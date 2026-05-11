from backend.accounts.models import Inventory
import os

if not hasattr(Inventory, "image"):
    print("Inventory has no image field; nothing to update.")
    raise SystemExit(0)

for inv in Inventory.objects.all():
    if inv.image:
        inv.image = os.path.basename(inv.image)
        inv.save()

exit()