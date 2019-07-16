class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []
        
        ranges = {}
        counts = []
        
        for i in range(len(S)):
            if S[i] not in ranges:
                ranges[S[i]] = [i,i]
            else:
                ranges[S[i]][-1] = i
        
        values = sorted(ranges.values())
        
        for item in values:
            start, end = item
            
            if len(counts) == 0:
                counts.append(item)
                
            else:
                if counts[-1][1] > start:
                    counts[-1][1] = max(end, counts[-1][1])
                else:
                    counts.append(item)
        
        return [(dist[1] - dist[0])+1 for dist in counts]