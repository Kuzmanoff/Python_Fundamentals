# On the first line, you will receive a number n. On the following n lines, you will receive integers. You should create and print two lists:

# · One with all the positives (including 0) numbers

# · One with all the negatives numbers

# Finally, print the following message:

# "Count of positives: {count_positives}

# Sum of negatives: {sum_of_negatives}" 

n = int(input())
positive_list = []
negative_list = []

for _ in range(n):

    n1 = int(input())

    if n1 >= 0:
        positive_list.append(n1)
    else:
        negative_list.append(n1)
print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")