from pyrsistent import pset, s
import warnings

def get_relation_class(M):
    class relation:

        origin = pset(M)

        def __init__(self, setM = s()):
            self.relations = pset(setM)


        def has_pair(self, pair):
            return pair in self.relations


        def add_pair(self, pair):
            if pair[0] in self.origin and pair[1] in self.origin:
                return relation(self.relations.add(pair))
            return self


        def remove_pair(self, pair):
            return relation(self.relations.discard(pair))


        def union(self, relation1):
            if not relation1.origin.issubset(self.origin):
                warnings.warn("Not able to union above unmatchable basic sets")
                return self
            return relation(self.relations | relation1.relations)


        def intersect(self, relation1):
            return relation(self.relations & relation1.relations)


        def substract(self, relation1):
            return relation(self.relations - relation1.relations)


        def inverse(self):
            tmp = set()
            for pair in self.relations:
                tmp.add((pair[1], pair[0]))
            return relation(tmp)


        def composition(self, relation1):
            if not relation1.origin.issubset(self.origin):
                warnings.warn("Would not get an instance of class above current basic set")
                return self
            tmp = set()
            for first, second1 in relation1.relations:
                for second2, third in self.relations:
                    if second1 == second2:
                        tmp.add((first, third))
            return relation(tmp)


        def is_reflexive(self):
            return all(self.has_pair((a,a)) for a in self.origin)


        def is_symmetric(self):
            return all(self.has_pair((b, a)) for (a, b) in self.relations)


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
            return self.relations == self.transitive_closure()


        def reflexive_transitive_closure(self):
            reflexive = set((a,a) for a in self.origin)
            return relation(self.transitive_closure() | reflexive)

    return relation



set1 = set((1, 4, 5, 5, 7))
print(set1)

print("Testing if get_relation_class returns a class")
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


print("Union G with Relation class above set {2, 4, 5, 7}")
test2 = get_relation_class({2, 4, 5, 7})
h1 = test2({(5, 5), (4, 7), (2, 4), (7, 7)})
h = g.union(h1)
print(h.relations)
print()

print("Union G with Relation class above set {4, 5, 7}")
test3 = get_relation_class({4, 5, 7})
i1 = test3({(4, 5), (7, 7)})
i = g.union(i1)
print(i.relations)
print()

print("Intersect G with {(7, 7), (2, 4), (4, 7), (5, 5)}")
test4 = get_relation_class({2, 4, 5, 7})
j1 = test4({(7, 7), (2, 4), (4, 7), (5, 5)})
j = g.intersect(j1)
print(j.relations)
print()

print("Substract (5, 4) and (7, 5) from G")
test5 = get_relation_class(g.origin)
k1 = test5({(5, 4), (7, 5)})
k = g.substract(k1)
print(k.relations)
print()

print("Inverse G")
l = g.inverse()
print(l.relations)
print()

print("Composite G with {(4, 1), (7, 2), (7, 5)}")
test6 = get_relation_class({1, 2, 4, 5, 7})
n1 = test6({(4, 1), (7, 2), (7, 5)})
n = g.composition(n1)
print(n.relations)
print()

print("Composite G with {(4, 1), (7, 2), (7, 5)}")
test7 = get_relation_class({1, 4, 5, 7})
n2 = test6({(4, 1), (7, 5)})
n = g.composition(n2)
print(n.relations)
print()

print("Is this composition reflexive?")
print(n.relations)
print(n.is_reflexive())
print()

print("What about after adding all pairs needed?")
test8 = get_relation_class(g.origin)
o1 = test8({(1, 1), (4, 4), (5, 5), (7, 7)})
o = n.union(o1)
print(o.relations)
print(o.is_reflexive())
print()

print("Is this composition symmetric?")
print(n.relations)
print(n.is_symmetric())
print()

print("What about after adding all pairs needed?")
test9 = get_relation_class({4, 5, 7})
p1 = test9({(4, 5), (7, 4), (7, 1)})
p = n.union(p1)
print(p.relations)
print(p.is_symmetric())
print()

print("Is this composition transitive?")
print(n.relations)
print(n.is_transitive())
print()

print("What about after adding all pairs needed?")
test10 = get_relation_class(g.origin)
r1 = test10({ (1, 1), (5,5), (5, 7)})
r = n.union(r1)
print(r.relations)
print(r.is_transitive())
print()

print("Reflexive-transitive closure of composition")
print(n.relations)
q = n.reflexive_transitive_closure()
print(q.relations)
print()
