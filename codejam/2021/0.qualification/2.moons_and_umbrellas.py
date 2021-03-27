def get_cost(l_char, r_char, x, y):
    if l_char == "C" and r_char == "J":
        return x
    elif l_char == "J" and r_char == "C":
        return y
    return 0


def main():
    """ugly but works fine."""
    T = int(input())
    for i in range(T):
        # x = price for CJ, y = price for JC, s = str consisting of c/j/?
        x, y, s = input().split(" ")
        x = int(x)
        y = int(y)

        cost = 0
        leng = len(s)

        if "J" not in s or "C" not in s:
            pass
        else:
            l_idx = 0
            # Roll forward to first non-?
            while s[l_idx] == "?":
                if l_idx + 1 < leng:
                    l_idx += 1
            r_idx = l_idx + 1
            while r_idx < leng:
                if s[r_idx] != "?":
                    cost += get_cost(s[l_idx], s[r_idx], x, y)
                    l_idx += 1
                    r_idx += 1
                else:
                    # look ahead
                    next = None
                    if r_idx + 1 < leng:
                        idx2 = r_idx + 1
                        while idx2 < leng:
                            val = s[idx2]
                            if val != "?":
                                next = val
                                break
                            idx2 += 1
                        if next:
                            if s[l_idx] != next:
                                if s[l_idx] == "C":
                                    cost += x
                                else:
                                    cost += y
                        l_idx = idx2
                        r_idx = l_idx + 1
                    else:
                        # nothing because we can copy prev char and pay nothing
                        break

        print(f"Case #{i+1}: {cost}")


main()
