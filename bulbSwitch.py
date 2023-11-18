def stateFinder(arr):
    len_arr = len(arr)
    states = ["On"] * len_arr
    
    for i in range(len_arr):
        j = arr[i] - 1
        while j < len_arr:
            newState = "Off"
            if states[j] == "Off":
                newState = "On"
            states[j] = newState
            j += arr[i]
    print(states)
    return (states)

stateFinder([1, 2, 3])
