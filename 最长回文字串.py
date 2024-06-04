def func(s):
    maxLen = 1
    tmp = 1
    maxStart = 0
    for j in range(len(s)):
        left = j - 1
        right = j + 1
        while left >= 0 and s[left]==s[j]:
            left -= 1
            tmp += 1
        while right <= len(s)-1 and s[right]==s[j]:
            right += 1
            tmp += 1
        while left >= 0 and right <= len(s)-1 and s[right]==s[left]:
            tmp += 2
            right += 1
            left -= 1
        if tmp > maxLen:
            maxLen = tmp
            maxStart = left
        tmp = 1
    return s[maxStart+1:maxStart+maxLen+1]

