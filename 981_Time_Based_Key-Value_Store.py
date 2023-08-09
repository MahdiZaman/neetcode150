class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.hash_map:
            # print('not found')
            return res
                            
        values = self.hash_map[key]
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res

if __name__ == '__main__':
    time_map = TimeMap()
    # time_map.set("foo", "bar", 1)
    # time_map.set("goo", "baz", 2)
    # time_map.set("foo", "qux", 3)
    # print(time_map.hash_map)
    # print(time_map.get("foo", 1))
    # ["TimeMap","set","set","get","set","get","get"]
    # [[],["a","bar",1],["x","b",3],["b",3],["foo","bar2",4],["foo",4],["foo",5]]
    time_map.set("a","bar",1)
    time_map.set("x","b",3)    
    print(time_map.hash_map)
    print(time_map.get("x",3))
    