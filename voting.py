films = ["f1", "f2", "f3", "f4",]

votes = [
  ("s01", "f2"),
  ("s02", "f1"),
  ("s01", "f2"),
  ("s01", "f1"),
  ("s03", "f1"),
  ("s04", "f2"),
  ("s02", "f3"),
  ("s05", "f2"),
]

rejected_vots = []
result = {}

for vote in votes:
  student_id, film_id = vote

  if film_id not in result:
    result[film_id] = []

  if student_id not in result[film_id]:
    result[film_id].append(student_id)
  else:
    rejected_vots.append(vote)

print("\n========== rejected vots ===========")
for vote in rejected_vots:
  print(vote)


print("\n========== voting result ===========")
for film_id in films:
  if film_id not in result:
    result[film_id] = []

result = dict(sorted(result.items(), key = lambda item: len(item[1]), reverse = True))
for film in result:

  print(f"film: {film} | votes: {len(result[film])}")


print("\n========== tastefull students ===========")
rank1 = list(result)[0]
rank1_votes = result[rank1]
rank2 = list(result)[1]
rank2_votes = result[rank2]
 
common = set(rank1_votes) & set(rank2_votes)
for student_id in common:
  print(student_id, " | ", end = "")