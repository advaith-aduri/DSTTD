from copy import deepcopy

def DeductiveFaultSim(model, inputs):
    DFS = dict()
    for net in model.get_nets():
        DFS[net] = set()
    
    model.eval(inputs)

    for i in inputs:
        if i[1] == "1":
            DFS[i[0]].add(str(i[0])+" s@0")
        elif i[1] == "0":
            DFS[i[0]].add(str(i[0])+" s@1")
    
    for i in range(1, model.max_level + 1):
            for gate in model.logic_dict[i]:
                if gate.type == "and":
                    a_val = model.net_dict[gate.input[0]][1]
                    b_val = model.net_dict[gate.input[1]][1]
                    a_set_ = deepcopy(DFS[gate.input[0]])
                    b_set_ = deepcopy(DFS[gate.input[1]])
                    c_val = model.net_dict[gate.output][1]
                    c_net = gate.output
                    DFS[gate.output] = and_propogation(a_val, b_val, a_set_, b_set_, c_net, c_val)
                elif gate.type == "or":
                    a_val = model.net_dict[gate.input[0]][1]
                    b_val = model.net_dict[gate.input[1]][1]
                    a_set_ = deepcopy(DFS[gate.input[0]])
                    b_set_ = deepcopy(DFS[gate.input[1]])
                    c_val = model.net_dict[gate.output][1]
                    c_net = gate.output
                    DFS[gate.output] = or_propogation(a_val, b_val, a_set_, b_set_, c_net, c_val)
                elif gate.type == "nand":
                    a_val = model.net_dict[gate.input[0]][1]
                    b_val = model.net_dict[gate.input[1]][1]
                    a_set_ = deepcopy(DFS[gate.input[0]])
                    b_set_ = deepcopy(DFS[gate.input[1]])
                    c_val = model.net_dict[gate.output][1]
                    c_net = gate.output
                    DFS[gate.output] = nand_propogation(a_val, b_val, a_set_, b_set_, c_net, c_val)
                elif gate.type == "nor":
                    a_val = model.net_dict[gate.input[0]][1]
                    b_val = model.net_dict[gate.input[1]][1]
                    a_set_ = deepcopy(DFS[gate.input[0]])
                    b_set_ = deepcopy(DFS[gate.input[1]])
                    c_val = model.net_dict[gate.output][1]
                    c_net = gate.output
                    DFS[gate.output] = nor_propogation(a_val, b_val, a_set_, b_set_, c_net, c_val)
                elif gate.type == "xor":
                    a_val = model.net_dict[gate.input[0]][1]
                    b_val = model.net_dict[gate.input[1]][1]
                    a_set_ = deepcopy(DFS[gate.input[0]])
                    b_set_ = deepcopy(DFS[gate.input[1]])
                    c_val = model.net_dict[gate.output][1]
                    c_net = gate.output
                    DFS[gate.output] = xor_propogation(a_val, b_val, a_set_, b_set_, c_net, c_val)
                elif gate.type == "xnor":
                    a_val = model.net_dict[gate.input[0]][1]
                    b_val = model.net_dict[gate.input[1]][1]
                    a_set_ = deepcopy(DFS[gate.input[0]])
                    b_set_ = deepcopy(DFS[gate.input[1]])
                    c_val = model.net_dict[gate.output][1]
                    c_net = gate.output
                    DFS[gate.output] = xnor_propogation(a_val, b_val, a_set_, b_set_, c_net, c_val)
                elif gate.type == "not":
                    a_val = model.net_dict[gate.input[0]][1]
                    a_set_ = deepcopy(DFS[gate.input[0]])
                    c_val = model.net_dict[gate.output][1]
                    c_net = gate.output
                    DFS[gate.output] = not_propogation(a_val, a_set_, c_net, c_val)
                elif gate.type == "buf":
                    a_val = model.net_dict[gate.input[0]][1]
                    a_set_ = deepcopy(DFS[gate.input[0]])
                    c_val = model.net_dict[gate.output][1]
                    c_net = gate.output
                    DFS[gate.output] = buf_propogation(a_val, a_set_, c_net, c_val)
    
    return DFS



def and_propogation(a_val, b_val, a_set, b_set, c_net="", c_val=None):
    c_set = set()
    if a_val == "1" and b_val == "1":
        c_set = a_set | b_set
    if a_val == "1" and b_val == "0":
        c_set = b_set - a_set
    if a_val == "0" and b_val == "1":
        c_set = a_set - b_set
    if a_val == "0" and b_val == "0":
        c_set = a_set & b_set
    
    if c_val != None:
        if c_val == "1":
            c_val = "0"
        elif c_val == "0":
            c_val = "1"
        else:
            raise ValueError
        c_set.add(c_net + " s@" + c_val)
    return c_set

def or_propogation(a_val, b_val, a_set, b_set, c_net="", c_val=None):
    c_set = set()
    if a_val == "0" and b_val == "0":
        c_set = a_set | b_set
    if a_val == "0" and b_val == "1":
        c_set = b_set - a_set
    if a_val == "1" and b_val == "0":
        c_set = a_set - b_set
    if a_val == "1" and b_val == "1":
        c_set = a_set & b_set
        
    if c_val != None:
        if c_val == "1":
            c_val = "0"
        elif c_val == "0":
            c_val = "1"
        else:
            raise ValueError
        c_set.add(c_net + " s@" + c_val)
    return c_set

def not_propogation(a_val, a_set_, c_net="", c_val=None):
    c_set = set()

    c_set = deepcopy(a_set_)

    if c_val != None:
        if c_val == "1":
            c_val = "0"
        elif c_val == "0":
            c_val = "1"
        else:
            raise ValueError
        c_set.add(c_net + " s@" + c_val)
    return c_set

def buf_propogation(a_val, a_set_, c_net="", c_val=None):
    c_set = set()

    c_set = deepcopy(a_set_)

    if c_val != None:
        if c_val == "1":
            c_val = "0"
        elif c_val == "0":
            c_val = "1"
        else:
            raise ValueError
        c_set.add(c_net + " s@" + c_val)
    return c_set

def nand_propogation(a_val, b_val, a_set_, b_set_, c_net="", c_val=None):
    c1_set = set()
    c1_set = and_propogation(a_val, b_val, a_set_, b_set_)
    c_set = set()
    c_set = not_propogation(a_val, c1_set)

    if c_val != None:
        if c_val == "1":
            c_val = "0"
        elif c_val == "0":
            c_val = "1"
        else:
            raise ValueError
        c_set.add(c_net + " s@" + c_val)
    return c_set

def nor_propogation(a_val, b_val, a_set_, b_set_, c_net="", c_val=None):
    c1_set = set()
    c1_set = or_propogation(a_val, b_val, a_set_, b_set_)
    c_set = set()
    c_set = not_propogation(a_val, c1_set)

    if c_val != None:
        if c_val == "1":
            c_val = "0"
        elif c_val == "0":
            c_val = "1"
        else:
            raise ValueError
        c_set.add(c_net + " s@" + c_val)
    return c_set

def xor_propogation(a_val, b_val, a_set_, b_set_, c_net="", c_val=None):
    ab = [a_val, b_val]

    if "0" in ab: 
        nand_val = "1"
    else:
        nand_val = "0"
    
    if "1" in ab:
        or_val = "1"
    else:
        or_val = "0"
    
    nand_set = nand_propogation(a_val, b_val, a_set_, b_set_)
    or_set = or_propogation(a_val, b_val, a_set_, b_set_)
    c_set = and_propogation(nand_val, or_val, nand_set, or_set)

    if c_val != None:
        if c_val == "1":
            c_val = "0"
        elif c_val == "0":
            c_val = "1"
        else:
            raise ValueError
        c_set.add(c_net + " s@" + c_val)
    return c_set

def xnor_propogation(a_val, b_val, a_set_, b_set_, c_net="", c_val=None):
    c1_set = set()
    c1_set = xor_propogation(a_val, b_val, a_set_, b_set_)
    c_set = set()
    c_set = not_propogation(a_val, c1_set)

    if c_val != None:
        if c_val == "1":
            c_val = "0"
        elif c_val == "0":
            c_val = "1"
        else:
            raise ValueError
        c_set.add(c_net + " s@" + c_val)
    return c_set