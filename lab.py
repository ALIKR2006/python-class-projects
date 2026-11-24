"""equipment = {
  ("Lab-A", "sensor"): ["S1", "S2"],
  ("Lab-B", "sensor"): ["S3",]
}

report_9 = equipment.copy() 
این یه کپی سطحیه پس دیکشنری جدیدی که ساخته میشه هم به همون لیست هایی که دیکشنری قبلی اشاره میکرد اشاره میکنه
و در واقع محتواش مستقل نیست از دیکشنری قبلی


equipment[("Lab-A", "sensor")].append("S4") 
چون خود لیستی که دیکشنری بهش اشاره میکنه تغییر میکنه تغییر در داخل دیکشنری جدید هم دیده میشه
equipment[("Lab-B", "sensor")] = ["S5"]
اینجا یک لیست جدید ساخته میشه برای دیگشنری قدیمی پس رفرنسش عوض میشه ولی رفرنس دیکشنری قبلی تغییر نمیکنه پس 
تغییر در اون مشاهده نمیشه
"""

equipment = {
  ("Lab-A", "sensor"): ["S1", "S2"],
  ("Lab-B", "sensor"): ["S3",]
}

def make_copy(equipment):
  copy = {}
  for key, serials in equipment.items():
    copy[key] = tuple(serials)

  return copy

report_9 = make_copy(equipment)

equipment[("Lab-A", "sensor")].append("S4")
equipment[("Lab-B", "sensor")] = ["S5"]

report_10 = make_copy(equipment)

all_keys = set(report_9) | set(report_10)
for key in all_keys:
  old = set(report_9.get(key, ()))
  new = set(report_10.get(key, ()))

  added = new - old
  removed = old - new

  print(f"\nkey => {key} :")
  print(f"added: {list(added)}")
  print(f"removed: {list(removed)}")


print("\n", report_9)
print(report_10)