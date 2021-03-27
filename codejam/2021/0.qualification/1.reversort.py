"""Probably a bad idea to start codejam with 7 hours left..."""


def main():
    T = int(input())
    for i in range(T):
        count = 0
        length = int(input())
        str_list = input().split(" ")
        int_list = [int(s) for s in str_list]
        idx = 0
        while idx < length - 1:
            j_elem = min(int_list[idx:])
            j_pos = int_list.index(j_elem, idx) + 1
            int_list[idx:j_pos] = int_list[idx:j_pos][::-1]
            idx += 1
            count += j_pos + 1 - idx

        print(f"Case #{i+1}: {count}")


main()
