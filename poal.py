def partlist(arr):
    #s = " "
    for i, word in enumerate(arr):
        if i < len(arr)-1:

            print([[" ".join(arr[:i+1])], [" ".join(arr[i+1:])]])

partlist(["I", "wish", "I", "hadn't", "come"])
#partlist(["cdIw", "tzIy", "xDu", "rThG"])
#partlist(["vJQ", "anj", "mQDq", "sOZ"])
