def sort_asc(n:int):
    return int(''.join(sorted(str(n))))

def sort_desc(n):
    return int(''.join(sorted(str(n), reverse=True)))


def kaprekar_times(n):
    count = 0
    last = n
    while True:
        print(last)
        smaller = sort_asc(last)
        bigger = sort_desc(last)
        answer = bigger - smaller
        count += 1

        if answer==6174:
            return count
        else:
            last = answer

print(kaprekar_times(1907))
