
def free_capacity(pool):

    out= []
    for p in pool:
        cap = p.get("capacity_gb", 0)
        used = p.get("used_gb", 0)
        free = cap-used
        if free < 0:
            free = 0
        out.append({"name": p.get("name"), "free_gb": free})
    return out

pools = [
    {"name": "poolA", "capacity_gb": 10000, "used_gb": 4200},
    {"name": "poolB", "capacity_gb": 5000, "used_gb": 5000},
]
print(free_capacity(pools))