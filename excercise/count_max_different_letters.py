
def lengthOfLongestSubstring(s: str) -> int:
    idx = 0
    max_length = 0
    chars = set()
    cur_length = 0
    cur_idx = 0
    while idx < len(s):
        if cur_idx == len(s) - 1:
            if s[cur_idx] not in chars:
                cur_length += 1
            if cur_length > max_length:
                max_length = cur_length
            chars = set()
            cur_length = 0
            idx += 1
            cur_idx = idx
        elif s[cur_idx] not in chars:
            chars.add(s[cur_idx])
            cur_length += 1
            cur_idx += 1
        else:
            if cur_length > max_length:
                max_length = cur_length
            chars = set()
            cur_length = 0
            idx += 1
            cur_idx = idx
    return max_length


print(lengthOfLongestSubstring('abcaddsbcbb'))