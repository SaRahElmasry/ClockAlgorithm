def clock_page_replacement(n, pages):
    page_frames = [None] * n
    reference_bits = [0] * n
    page_faults = 0
    clock = 0

    for page in pages:
        page = int(page)
        if page not in page_frames:
            page_faults += 1
            while True:
                # if its bit ref = 1
                if reference_bits[clock] == 1:
                    # Set its bit ref to 0
                    reference_bits[clock] = 0
                    # move the clock to the next page
                    clock = (clock + 1) % n
                # if its bit ref = 0
                else:
                    page_frames[clock] = page
                    # Set its bit ref to 1
                    reference_bits[clock] = 1
                    # move the clock to the next page
                    clock = (clock + 1) % n
                    break
        # if the page already exist in page_frames
        else:
            index = page_frames.index(page)
            # Set its bit ref to 1
            reference_bits[index] = 1

    print("Page faults =", page_faults)
    print("[" + ", ".join([f"{page}->{bit}" for page, bit in zip(page_frames, reference_bits)]) + "]")


if __name__ == '__main__':
    print("Enter The Number of Page Frames :")
    n = int(input())
    print("Enter The Pages :")
    pages = input().split()
    print("----------------------------------")
    clock_page_replacement(n, pages)





# Test Case 1
# 5
# 1 2 6 5 7 8 9 1 2 3 4 5 6

