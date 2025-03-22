import json


file_path = "C:/Apps_and_more/KBTU_1курс_2семестр/Programming/Lab_04/tasks/json/sample-data.json"


with open(file_path) as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes["mtu"]
    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<6}")
