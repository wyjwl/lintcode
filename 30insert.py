def insert(intervals, newInterval):
    results = []
    insertPos = 0
    for interval in intervals:
        if interval.end < newInterval.start:
            results.append(interval)
            insertPos += 1
        elif interval.start > newInterval.end:
            results.append(interval)
        else:
            newInterval.start = min(interval.start, newInterval.start)
            newInterval.end = max(interval.end, newInterval.end)
    results.insert(insertPos, newInterval)
    return results


