max = 0
min = 0

nums = []
for i in range(10):
  nums.append(float(input(f"number {i + 1}: ")))

#print("max is:" , max(nums))
for i in range(len(nums)):
  if nums[i] > max:
    max = nums[i]

#print("min is:" , min(nums))
for i in range(len(nums)):
  if nums[i] < min:
    min = nums[i]

print("========================================")
print("max is:" , max)
print("min is:" , min)
