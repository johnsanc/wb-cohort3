from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        output = []
        counts = Counter()
        
        for domain in cpdomains:
            count, site = domain.split()
            temp = []
            site_list = site.split(".")
            site_list.reverse()
            for subd in site_list:
                temp.append(subd)
                temp.reverse()
                counts["".join(temp)] += int(count)
                temp.reverse()
                temp.append(".")
                
        for i,c in counts.items():
            item = str(c) + " " + i 
            output.append(item)
    
        return output