from collections import deque

def deepTraverse(begin, neighbors, f):
    visited = set()
    checklist = deque()

    checklist.append(begin) # SEED, thats gon sprout!
    while len(checklist) > 0:
        node = checklist.pop()

        if node not in visited:
            f(node)
        visited.add(node)

        checklist.extend(neighbors(node))

def shallowTraverse(begin, neighbors, f):
    visited = set()
    checklist = deque()

    checklist.append(begin) # SEED, thats gon sprout!
    while len(checklist) > 0:
        node = checklist.pop()

        if node not in visited:
            f(node)
        visited.add(node)

        checklist.extendleft(neighbors(node))

if __name__ == '__main__':

    '''
       A
      E B
    G F D C
    '''

    neighbors = {
        'A': 'EB',
        'E': 'GF',
        'B': 'DC',
        'G': '',
        'F': '',
        'D': '',
        'C': '',
    }

    order = []
    deepTraverse('A', lambda x: neighbors[x], lambda x: order.append(x))
    assert order == list('ABCDEFG')

    order = []
    shallowTraverse('A', lambda x: neighbors[x], lambda x: order.append(x))
    assert order == list('AEBGFDC')

    print(__file__ + ': Passed')
