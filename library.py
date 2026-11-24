events = [
  ("borrow", "s01", "python", 1),
  ("borrow", "s01", "python", 2),
  ("return", "s01", "python", 1),
  ("borrow", "s02", "python", 1),
  ("return", "s03", "python", 2),
  ("borrow", "s01", "python", 1),
]

history = {}
borrowed = {}
rejected = []

for event in events:
  action, student_id, title, copy_number = event

  copy_key = (title, copy_number)

  if action == "borrow":
    if copy_key not in borrowed:
      borrowed[copy_key] = student_id

      if title not in history:
        history[title] = set()
      
      history[title].add(student_id)

    else:
      rejected.append(event)

  elif action == "return":
    if borrowed.get(copy_key) == student_id:
      del borrowed[copy_key]

    else:
      rejected.append(event)

print("\n============ firt report ===========")
print("currently borowed copies: ")
for copy_key, student_id in borrowed.items():
  print(f"title: {copy_key[0]} | copy: {copy_key[1]} | student: {student_id}")

print("\n============ second report ===========")
print("borrowing history: ")
for title, students in history.items():
  print(f"title: {title} | students: {students}")

print("\n============ third report ===========")
print("rejected events: ")
for event in rejected:
  print(event)