
def get_volume_data(json_data):

    vols = json_data.get("volumes" , [])

    names = [
        v.get("name")
        for v in vols
        if (v.get("status") == "online") or (v.get("online") is True)
    ]

    return names

if __name__ == "__main__":

    sample = {"volumes":[{"name":"v1","status":"online"},{"name":"v2","status":"offline"},{"name":"v3","online":True}]}

    print(get_volume_data(sample))