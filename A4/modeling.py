# Copyright 2017 Sihan Wang shwang95@bu.edu
class Polynomial():

    def __init__(self, cof=[0]):
        cof = list(cof)
        self.cof = {idx: cof for idx, cof in enumerate(cof[::-1]) if cof != 0}

    def __setitem__(self, key, value):
        self.cof[key] = value

    def __getitem__(self, key):
        if key in self.cof:
            return self.cof[key]
        else:
            return 0

    def __add__(self, value):
        sol_dic = {
            idx: self.cof.get(
                idx,
                0) +
            value.cof.get(
                idx,
                0) for idx in set(
                self.cof) | set(
                    value.cof) if self.cof.get(
                        idx,
                        0) +
            value.cof.get(
                idx,
                0) != 0}
        sol = Polynomial()
        for each in sol_dic:
            sol[each] = sol_dic[each]
        return sol

    def __sub__(self, value):
        sol_dic = {
            idx: self.cof.get(
                idx,
                0) -
            value.cof.get(
                idx,
                0) for idx in set(
                self.cof) | set(
                    value.cof) if self.cof.get(
                        idx,
                        0) -
            value.cof.get(
                idx,
                0) != 0}
        sol = Polynomial()
        for each in sol_dic:
            sol[each] = sol_dic[each]
        return sol

    def __mul__(self, value):
        sol_dic = {}
        for idx_self in self.cof:
            for idx_value in value.cof:
                if idx_self + idx_value in sol_dic:
                    sol_dic[idx_self + idx_value] += self.cof[idx_self] * \
                        value.cof[idx_value]
                else:
                    sol_dic[idx_self + idx_value] = self.cof[idx_self] * \
                        value.cof[idx_value]
        sol = Polynomial()
        for each in sol_dic:
            sol[each] = sol_dic[each]
        return sol

    def __eq__(self, value):
        return True if self.cof == value.cof else False

    def eval(self, x):
        sol = 0
        for each in self.cof:
            sol += self.cof[each] * x ** each
        return sol

    def deriv(self):
        sol_dic = {
            idx -
            1: self.cof[idx] *
            idx for idx in set(
                self.cof) if idx != 0}
        sol = Polynomial()
        for each in sol_dic:
            sol[each] = sol_dic[each]
        return sol

    def __str__(self):
        str = ''
        for idx, cof in dict(
            sorted(
                self.cof.items(), key=lambda item: item[0], reverse=True)).items():
            if idx == 0:
                str += '%s+' % cof
            else:
                str += '%sx^%s+' % (cof, idx)
        str = str.strip("+")
        return str

    def __repr__(self):
        return self.cof
