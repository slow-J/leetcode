# WIP, passes only first test case :(
def get_diffs_and_max(exercise_mins):
    diffs = {}
    max = 0
    prev = exercise_mins[0]
    for mins in exercise_mins[1:]:
        diff = mins - prev
        if diff in diffs:
            diffs[diff] += 1
        else:
            diffs[diff] = 1
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
        exercise_mins = [int(x) for x in exercise_mins]

        diffs, max_key = get_diffs_and_max(exercise_mins)

        while K > 0 and diffs:
            occurances = diffs[max_key]
            del diffs[max_key]
            # scnd_max_key = max(diffs)
            K -= occurances
            if K >= 0:
                prev, prev_pos = exercise_mins[0], 0
                for i2, current_exercise in enumerate(exercise_mins[1:]):
                    if current_exercise - prev == max_key:
                        mid_val = current_exercise - (current_exercise - prev) // 2
                        exercise_mins.insert(prev_pos + 1, mid_val)

                        # New diffs, left
                        left_diff = mid_val - prev
                        if left_diff in diffs:
                            diffs[left_diff] += 1
                        else:
                            diffs[left_diff] = 1
                        # New diffs, right
                        right_diff = current_exercise - mid_val
                        if right_diff in diffs:
                            diffs[right_diff] += 1
                        else:
                            diffs[right_diff] = 1

                        i2 += 1
                        occurances -= 1
                        if occurances == 0:
                            break
                        prev_pos = prev_pos + 1
                        prev = mid_val
                    else:
                        prev, prev_pos = current_exercise, i2 + 1

                max_key = max(diffs)

        # ANS is the biggest diff between consecutive numbers
        print(f"Case #{i+1}: {max_key}")


main()
