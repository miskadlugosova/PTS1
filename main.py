from pyrsistent import freeze, thaw


def get_relation_class(M):
    class relation:

        origin = freeze(M)
        def __init__(self, setM):

            # co ak dostanem setM ako pset? co sa s nim stane?
            self.relations = freeze(setM)


        def has_pair(self, pair):
            if pair[0] in self.origin and pair[1] in self.origin:
                return pair in self.relations
            else:
                return False

        def add_pair(self, pair):
            if pair[0] in self.origin and pair[1] in self.origin:
                return relation(self.relations.add(pair))
            else:
                return self

        def remove_pair(self, pair):
            if pair in self.relations:
                return relation(self.relations.remove(pair))
            else:
                return self

        # co ak relation1 nie je pset?
        def union(self, relation1):
            return relation(self.relations | relation1)

        def intersect(self, relation1):
            return relation(self.relations & relation1)

        def substract(self, relation1):
            return relation(self.relations - relation1)

        def inverse(self):
            tmp = set()
            for pair in self.relations:
                tmp.add((pair[1], pair[0]))
            return relation(tmp)

        def composition(self):
            closure = self.set
            while True:
                new_relations = set((x, w) for x, y in closure for q, w in closure if q == y)

                closure_until_now = closure | new_relations

                if closure_until_now == closure:
                    break

                closure = closure_until_now

            return relation(closure)

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
            if self.relations == self.composition():
                return True
            else:
                return False

        def reflexive_transitive_closure(self):
            reflexive = set()
            for element in self.origin:
                reflexive.add((element, element))
            return relation(self.composition() | reflexive)

    return relation

set1 = set((1, 4, 5, 5, 7))
print(set1)

test1 = get_relation_class(set1)

print(test1)
print(test1.origin)
test1.origin.add(12)
print(test1.origin)
a = test1({(5,5), (7,7), (5, 4)})
print (a)

print("zaciatok")
print(a.relations)
b = a.add_pair((1, 7))
print(b.relations)
c = b.add_pair((4,9))
print(c.relations)
d = c.add_pair((4, 7))
print(d.relations)
e = d.add_pair((1, 7))
print(e.relations)
f = e.remove_pair((5, 5))
print(f.relations)
g = f.remove_pair((5, 7))
print(g)
print(g.relations)
print(g.origin)


