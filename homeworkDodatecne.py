def sequences(line_a, line_b, line_c):
    # prazdny slovnik pro results
    result = {}
    
    # cyklem prochazim a zaznamenavam
    for sequence, label in [(line_a, 'A'), (line_b, 'B'), (line_c, 'C')]:
        for id, count in sequence:
            # kdyz neexistuje = prazdny seznam
            if id not in result:
                result[id] = [0, 0, 0]
            # pridam hodnotu count na misto v seznamu podle label.
            if label == 'A':
                result[id][0] = count;
            elif label == 'B':
                result[id][1] = count;
            elif label == 'C':
                result[id][2] = count;
    
    return result
line_a = ((1, 3), (3, 4), (10, 2));
line_b = ((1, 2), (2, 4), (5, 2));
line_c = ((1, 5), (3, 2), (7, 3));
# volam fci
result = sequences(line_a, line_b, line_c);
print(result)