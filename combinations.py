def generateSelections(states, n, unique=False, order=True):
    if n < 0:
        raise Exception('Aw fuck off, mate.')
    if n == 0:
        return []
    if n == 1:
        return [[state] for state in states]
    selections = []
    for i, state in enumerate(states):
        substates = []
        if order:
            substates.extend(states[:i])
        if not unique:
            substates.append(states[i])
        substates.extend(states[i + 1:])
        for subselection in generateSelections(substates, n - 1, unique, order):
            selections.append([state] + subselection)
    return selections
