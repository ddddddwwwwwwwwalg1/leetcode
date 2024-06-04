"""
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
"""
def func(intervals):
    intervals = sorted(intervals)
    merged = [intervals[0]]
    for i in intervals[1:]:
        if i[0]>merged[-1][1]:
            merged.append(i)
        else:
            merged[-1][1] = max(i[1],merged[-1][1])
    return merged
