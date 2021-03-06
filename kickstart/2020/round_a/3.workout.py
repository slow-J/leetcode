from collections import defaultdict
from heapq import nlargest

# WIP, still only passes first test case :(
# V2: much more efficient, but still TLE for test set 2
def get_diffs_and_max(exercise_mins):
    diffs = defaultdict(int)
    max = 0
    prev = int(exercise_mins[0])
    for mins in exercise_mins[1:]:
        mins = int(mins)
        diff = mins - prev
        diffs[diff] += 1
        if diff > max:
            max = diff
        prev = mins
    return diffs, max


def main():
    T = int(input())
    for i in range(T):
        # N, K
        session_count, K = input().split(" ")
        session_count = int(session_count)
        K = int(K)
        # M
        exercise_mins = input().split(" ")
        diffs, max_key = get_diffs_and_max(exercise_mins)

        while K > 0 and diffs:
            if max_key <= 1:
                break
            occurances = diffs[max_key]
            K -= occurances
            if K >= 0:
                del diffs[max_key]

                left_diff = max_key // 2
                diffs[left_diff] += occurances
                # New diffs, right
                right_diff = max_key - left_diff
                diffs[right_diff] += occurances

                # max_key = max(diffs)
                max_key = nlargest(1, diffs)[0]

        # ANS is the biggest diff between consecutive numbers
        print(f"Case #{i+1}: {max_key}")


main()
