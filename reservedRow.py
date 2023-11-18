def solution(S):
    rows = [[0] * 9] * 5
    
    # mark rows in rows list
    track = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
  
    # loop through reserved seats
    i = 0
    while i < len(S):
        reservedRow = track[S[i]]
        reservedRowSeat = int(S[i+1]) - 1
        
        newReserved = list(rows[reservedRow])
        newReserved[reservedRowSeat] = 1
        rows[reservedRow] = newReserved
        
        i += 2

    longest = 0
    for arr in rows:
        count = 0
        for el in arr:
            if el == 0:
                count += 1
            else:
                longest = max(longest, count)
                count = 0
        longest = max(longest, count)
    
    print(longest)

solution('B3A4C7E6')
solution('A7B5C5D5E5A9A1')
solution('A5B5C5D5E5')


