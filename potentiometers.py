def print_cases(cases):
    for i, case in enumerate(cases):
        print('Case {}:'.format(i + 1))
        for value in case:
            print(value)
        # Blank line between cases
        if i < len(cases) - 1:
            print('')
    exit()


potmeters = list()
cases = []
N = None
while True:
    while True:
        # Initial input
        N = input()
        if N == 'END':
            break
        if N == '0':
            print_cases(cases)

        # Read potentiometers values
        potmeters = []
        for potmeter in range(int(N)):
            potmeters.append(int(input()))

        # Cases
        intermediaryCases = []
        while True:
            try:
                op, value1, value2 = input().split()
                value1 = int(value1)
                value2 = int(value2)
                # print(op, value1, value2)
                if op == 'S': # Set
                    potmeters[value1 - 1] = value2
                else: # Measure
                    intermediaryCases.append(sum(potmeters[(value1 - 1):value2]))
                    # print(intermediaryCases)
            except: break
        cases.append(intermediaryCases)
    # print('Potmeters:', potmeters)
