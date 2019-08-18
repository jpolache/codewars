def partlist(arr):
    s = " "
    for i, word in enumerate(arr):
        print(s.join(arr[:i+1]), s.join(arr[i+1:]))

partlist(["I", "wish", "I", "hadn't", "come"])
partlist(["cdIw", "tzIy", "xDu", "rThG"])
partlist(["vJQ", "anj", "mQDq", "sOZ"])
