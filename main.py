def get_relation_class(M):
    class relation:
        origin = frozenset(M)
        relations = ()

        def __init__(self, setM):
            self.relations = frozenset(setM)


        def has_element(element):
            return element in set

        def add_element(self, element):
            tmp = set(self.relations)
            tmp.add(element)
            return relation(self.origin, tmp)

        def remove_element(self, element):
            tmp = set(self.relations)
            tmp.remove(element)
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


# engineers = Set(['John', 'Jane', 'Jack', 'Janice'])
# programmers = Set(['Jack', 'Sam', 'Susan', 'Janice'])
# managers = Set(['Jane', 'Jack', 'Susan', 'Zack'])
# employees = engineers | programmers | managers           # union
# engineering_management = engineers & managers            # intersection
# fulltime_management = managers - engineers - programmers # difference
# engineers.add('Marvin')                                  # add element
