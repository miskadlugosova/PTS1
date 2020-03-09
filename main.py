from pyrsistent import freeze

def get_relation_class(M):
    class relation:

        origin = freeze(M)
        def __init__(self, setM):

            self.relations = freeze(setM)


        def has_pair(self, pair):
            if pair[0] in self.origin and pair[1] in self.origin:
                return pair in set
            else:
                return False

        def add_pair(self, pair):
            tmp = set(self.relations)
            if pair[0] in self.origin and pair[1] in self.origin:
                tmp.add(pair)
            return relation(self.origin, tmp)

        def remove_pair(self, pair):
            tmp = set(self.relations)
            if pair[0] in self.origin and pair[1] in self.origin:
                tmp.remove(pair)
            return relation(self.origin, tmp)

        def union(self, relation1):
            tmp = set(self.relations) | relation1
            return relation(self.origin, tmp)

        def intersect(self, relation1):
            tmp = set(self.relations) & relation1
            return relation(self.origin, tmp)

        def substract(self, relation1):
            tmp = set(self.relations) - relation1
            return relation(self.origin, tmp)

        def inverse(self):
            tmp = set()
            for pair in self.relations:
                tmp.add((pair[1], pair[0]))
            return relation(self.origin, tmp)

        def composition(self):
            closure = set(self.set)
            while True:
                new_relations = set((x, w) for x, y in closure for q, w in closure if q == y)

                closure_until_now = closure | new_relations

                if closure_until_now == closure:
                    break

                closure = closure_until_now

            return closure

        def is_reflexive(self):
            non_reflexive = len(self.origin)
            for pair in self.set:
                if pair[0] == pair[1]:
                    non_reflexive -= 1

            if non_reflexive == 0:
                return True
            else:
                return False

        def is_symmetric(self):
            for pair in set:
                if (pair[1], pair[0]) not in set:
                    return False

            return True

        def is_transitive(self):
            if self.set == self.composition():
                return True
            else:
                return False

        def reflexive_transitive_closure(self):
            reflexive = set()
            for element in self.origin:
                reflexive.add((element, element))
            return self.composition() | reflexive

    return relation

set1 = set((1, 4, 5, 5, 7))
set2 = {1, 4, 4, 9, 5, 5, 7}

print(set1)
print(set2)

test1 = get_relation_class(set1)
# test2 = get_relation_class(set2)


print(test1.origin)

print(test1)
test1.origin.add(12)
print(test1.origin)
# a = test1(())
# print (a)

