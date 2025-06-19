def min_window(s, t):
    n = len(s)
    m = len(t)
    if n < m:
        return ""

    # Step 1: Build frequency map for t
    map_dict = dict()
    for ch in t:
        if ch in map_dict:
            map_dict[ch] += 1
        else:
            map_dict[ch] = 1

    count = m  # total characters needed
    l = 0
    min_len = float('inf')
    start = 0

    # Step 2: Sliding window
    for r in range(n):
        ch = s[r]
        if ch in map_dict:
            map_dict[ch] -= 1
            if map_dict[ch] >= 0:
                count -= 1

        # Step 3: When all characters are matched
        while count == 0:
            # Update minimum window
            if r - l + 1 < min_len:
                min_len = r - l + 1
                start = l

            # Try to shrink the window from the left
            left_ch = s[l]
            if left_ch in map_dict:
                map_dict[left_ch] += 1
                if map_dict[left_ch] > 0:
                    count += 1
            l += 1

    if min_len == float('inf'):
        return ""
    else:
        return s[start:start + min_len]
