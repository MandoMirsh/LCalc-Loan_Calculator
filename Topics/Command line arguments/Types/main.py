args = sys.argv

# further code of the script "add_four_numbers.py"
sum_ = 0
for i in range(4):
    sum_ += int(args[i + 1])
# instead of the three previous: sum_ = sum(map(int, args[1:]))
print(sum_)
