from pyrsistent import freeze
import warnings

def get_relation_class(M):
    class relation:

        origin = freeze(M)
        def __init__(self, setM):
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


        def union(self, relation1):
            tmp = set()
            for pair in relation1:
                if (pair[0] in self.origin and pair[1] in self.origin):
                    tmp.add(pair)
                else:
                    warnings.warn("Not able to union sets above different basic sets")
                    return self

            return relation(self.relations | tmp)


        def intersect(self, relation1):
            return relation(self.relations & relation1)


        def substract(self, relation1):
            return relation(self.relations - relation1)


        def inverse(self):
            tmp = set()
            for pair in self.relations:
                tmp.add((pair[1], pair[0]))
            return relation(tmp)


        def composition(self, relation1):
            tmp = set()
            for first, second1 in self.relations:
                for second2, third in relation1:
                    if second1 == second2 and third in self.origin:
                        tmp.add((first, third))
            return relation(tmp)


        def is_reflexive(self):
            non_reflexive = len(self.origin)
            for pair in self.relations:
                if pair[0] == pair[1]:
                    non_reflexive -= 1

            if non_reflexive == 0:
                return True
            else:
                return False


        def is_symmetric(self):
            for pair in self.relations:
                if (pair[1], pair[0]) not in self.relations:
                    return False
            return True


        def transitive_closure(self):
            closure = self.relations
            while True:
                new_relations = set((x, w) for x, y in closure for q, w in closure if q == y)

                closure_until_now = closure | new_relations

                if closure_until_now == closure:
                    break

                closure = closure_until_now

            return closure


        def is_transitive(self):
            if self.relations == self.transitive_closure():
                return True
            else:
                return False

        def reflexive_transitive_closure(self):
            reflexive = set()
            for element in self.origin:
                reflexive.add((element, element))
            return relation(self.transitive_closure() | reflexive)

    return relation



set1 = set((1, 4, 5, 5, 7))
print(set1)

print("Testin if get_relation_class returns a class")
test1 = get_relation_class(set1)
print(test1)
print(test1.origin)

print("Testing if it is possible to add element to set M")
test1.origin.add(12)
print(test1.origin)

print("Testing creating instance")
a = test1({(5,5), (7,7), (5, 4)})
print (a)

print()
print("Testing of functions:")
print()

print(a.relations)
print("Add (1, 7)")
b = a.add_pair((1, 7))
print(b.relations)
print("Add (4, 9)")
c = b.add_pair((4,9))
print(c.relations)
print("Add (4, 7)")
d = c.add_pair((4, 7))
print(d.relations)
print("Add (1, 7)")
e = d.add_pair((1, 7))
print(e.relations)
print("Remove (5, 5)")
f = e.remove_pair((5, 5))
print(f.relations)
print("Remove (5, 7)")
g = f.remove_pair((5, 7))
print(g.relations)
print()

print("Has pair (5,4)?")
print(g.has_pair((5, 4)))
print("Has pair (7, 4)?")
print(g.has_pair((7, 4)))
print()

print("Checking basic set")
print(g.origin)
print("Actual set G of relations")
print(g.relations)
print()


print("Union G with {(7, 7), (2, 4), (4, 7), (5, 5)}")
h = g.union({(7, 7), (2, 4), (4, 7), (5, 5)})
print(h.relations)
print()

print("Union G with {(7, 7), (4, 7), (5, 5)}")
i = g.union({(7, 7), (4, 7), (5, 5)})
print(i.relations)
print()

print("Intersect G with {(7, 7), (2, 4), (4, 7), (5, 5)}")
j = g.intersect({(7, 7), (2, 4), (4, 7), (5, 5)})
print(j.relations)
print()

print("Substract (5, 4) and (7, 5) from G")
k = g.substract({(5, 4), (7, 5)})
print(k.relations)
print()

print("Inverse G")
l = g.inverse()
print(l.relations)
print()

print("Composite G with {(4, 1), (7, 2), (7, 5)}")
n = g.composition({(4, 1), (7, 2), (7, 5)})
print(n.relations)
print()

print("Is this composition reflexive?")
print(n.relations)
print(n.is_reflexive())
print()

print("What about after adding all pairs needed?")
o = n.union({(1, 1), (4, 4), (5, 5), (7, 7)})
print(o.relations)
print(o.is_reflexive())
print()

print("Is this composition symmetric?")
print(n.relations)
print(n.is_symmetric())
print()

print("What about after adding all pairs needed?")
p = n.union({(5, 4), (5, 7)})
print(p.relations)
print(p.is_symmetric())
print()

print("Is this composition transitive?")
print(n.relations)
print(n.is_transitive())
print()

print("What about after adding all pairs needed?")
p = n.union({(4, 1), (1, 1), (5,5), (7,1)})
print(p.relations)
print(p.is_transitive())
print()

print("Reflexive-transitive closure of composition")
print(n.relations)
q = n.reflexive_transitive_closure()
print(q.relations)
print()
