def main():
    # Done
    T = int(input())
    for i in range(T):
        # N, B
        n_houses, budget = input().split(' ')
        n_houses = int(n_houses)
        budget = int(budget)
        house_costs = input().split(' ')
        house_costs = [int(i) for i in house_costs]
        house_costs.sort()
        total = 0
        count = 0
        for house in house_costs:
            if house + total <= budget:
                total += house
                count += 1
            else:
                break
        print(f"Case #{i+1}: {count}")


main()
