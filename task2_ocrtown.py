candidates = {
    "A" : 0,
    "B" : 0,
    "C" : 0,
}

def main():
    choice = str(input("END or vote candidate: A, B, or C"))

    if choice == "END":
        print(candidates)

        tot = 0
        for candidate in candidates:
            votes = candidates[candidate]
            tot += votes
        print("Total: ", tot)

    elif choice in candidates:
        candidates[choice] += 1
    else:
        print("Invalid choice")

while True:
    main()