def sort_asc(n):
    return int("".join(sorted([i for i in str(n)])))

def sort_desc(n):
    return int("".join(sorted([i for i in str(n)], reverse=True)))


def kaprekar_times(n):

    count = 

    last = n

    while True:

        smaller = sort_asc(last)

        bigger = sort_desc(last)

        answer = bigger - smaller

        count += 1

        if answer==last:
            return count
        else:

            last = answer

    return count
print(kaprekar_times(9272))
