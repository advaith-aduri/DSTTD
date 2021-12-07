from NetGen import gate_eval
from NetGen import parser

class GateModel:
    def __init__(self, gate_param):
        self.type = gate_param[0]
        self.name = gate_param[1]
        self.output = gate_param[2]
        self.input = gate_param[3:]

    def __str__(self):
        return f"Name: {self.name}\nType: {self.type}\nInputs: {self.input}\nOutput: {self.output}\n"


class LogicModel:
    def __init__(self, net_dict, logic_list):
        self.net_dict = net_dict
        self.logic_list = logic_list
        net_list = [key for key in net_dict.keys()]
        net_level = parser.gate_levelization(net_list, logic_list)
        for key, value in net_level.items():
            self.net_dict[key][0] = value

        self.logic_dict = dict()
        self.max_level = 0
        for key, val in self.net_dict.items():
            if val[0] > self.max_level:
                self.max_level = val[0]
        for i in range(1, self.max_level + 1):
            self.logic_dict[i] = []
        for key, value in self.net_dict.items():
            for gate in logic_list:
                if gate.output == key:
                    self.logic_dict[value[0]].append(gate)
        # self.print_gates()

    def get_nets(self):
        nets = []
        for i in self.net_dict.keys():
            nets.append(i)
        return nets

    def eval(self, input_list, F_Net="", F_Val="x"):
        """
        :raise error: Need to implement data dependence checking
        """
        for i in input_list:
            self.net_dict[i[0]][1] = i[1]

        for key in self.net_dict.keys():
            if key == F_Net and self.net_dict[key][0] == 0:
                self.net_dict[key][1] = F_Val

        for i in range(1, self.max_level + 1):
            for gate in self.logic_dict[i]:
                self.gate_ce(gate)
                if F_Net == gate.output:
                    self.net_dict[F_Net][1] = F_Val


    def reset_model(self):
        for key, value in self.net_dict.items():
            value[1] = "x"

    def print_gates(self):
        for key, value in self.logic_dict.items():
            print("Level ", key)
            for gate in value:
                print(gate)

    def gate_ce(self, gate):
        if gate.type == "and":
            gate_eval.and_eval(gate, self.net_dict)
        elif gate.type == "or":
            gate_eval.or_eval(gate, self.net_dict)
        elif gate.type == "not":
            gate_eval.not_eval(gate, self.net_dict)
        elif gate.type == "buf":
            gate_eval.buf_eval(gate, self.net_dict)
        elif gate.type == "xor":
            gate_eval.xor_eval(gate, self.net_dict)
        elif gate.type == "nand":
            gate_eval.nand_eval(gate, self.net_dict)
        elif gate.type == "nor":
            gate_eval.nor_eval(gate, self.net_dict)
        elif gate.type == "xnor":
            gate_eval.xnor_eval(gate, self.net_dict)