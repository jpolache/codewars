import json

def partlist(arr):
    op = []
    for i, word in enumerate(arr):
        if i < len(arr)-1:
            op.append([(" ".join(arr[:i+1])), (" ".join(arr[i+1:]))])
    print(json.dumps(op))

partlist(["I", "wish", "I", "hadn't", "come"])
#partlist(["cdIw", "tzIy", "xDu", "rThG"])
#partlist(["vJQ", "anj", "mQDq", "sOZ"])

#def partlist(arr):
#    return [(' '.join(arr[:i]), ' '.join(arr[i:])) for i in range(1, len(arr))]
