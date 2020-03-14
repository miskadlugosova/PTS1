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
