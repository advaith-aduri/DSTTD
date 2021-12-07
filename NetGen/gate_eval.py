def and_eval(gate, net_dict):
    inp = []
    for i in gate.input:
        inp.append(net_dict[i][1])
    out = "x"

    if "0" in inp:
        out = "0"
    elif inp[0] == "1":
        out = inp[1]
    elif inp[1] == "1":
        out = inp[0]
    elif inp[0] == "D" and inp[1] == "D":
        out = "D"
    elif inp[0] == "d" and inp[1] == "d":
        out = "d"
    elif "d" in inp and "D" in inp:
        out = "0"

    net_dict[gate.output][1] = out


def or_eval(gate, net_dict):
    inp = []
    for i in gate.input:
        inp.append(net_dict[i][1])
    out = "x"

    if "1" in inp:
        out = "1"
    elif inp[0] == "0":
        out = inp[1]
    elif inp[1] == "0":
        out = inp[0]
    elif inp[0] == "D" and inp[1] == "D":
        out = "D"
    elif inp[0] == "d" and inp[1] == "d":
        out = "d"
    elif "d" in inp and "D" in inp:
        out = "1"

    net_dict[gate.output][1] = out


def not_eval(gate, net_dict):
    inp = []
    for i in gate.input:
        inp.append(net_dict[i][1])
    out = "x"

    if "1" in inp:
        out = "0"
    elif "0" in inp:
        out = "1"
    elif "x" in inp:
        out = "x"
    elif "D" in inp:
        out = "d"
    elif "d" in inp:
        out = "D"
    net_dict[gate.output][1] = out


def buf_eval(gate, net_dict):
    inp = []
    for i in gate.input:
        inp.append(net_dict[i][1])
    out = "x"

    if "0" in inp:
        out = "0"
    elif "1" in inp:
        out = "1"
    elif "x" in inp:
        out = "x"
    elif "D" in inp:
        out = "D"
    elif "d" in inp:
        out = "d"
    net_dict[gate.output][1] = out


def xor_eval(gate, net_dict):
    inp = []
    for i in gate.input:
        inp.append(net_dict[i][1])
    out = "x"

    if inp[0] == "0":
        out = inp[1]
    elif inp[1] == "0":
        out = inp[0]
    elif inp[0] == "1":
        if inp[1] == "0":
            out = "1"
        elif inp[1] == "1":
            out = "0"
        elif inp[1] == "D":
            out = "d"
        elif inp[1] == "d":
            out = "D"
    elif inp[1] == "1":
        if inp[0] == "0":
            out = "1"
        elif inp[0] == "1":
            out = "0"
        elif inp[0] == "D":
            out = "d"
        elif inp[0] == "d":
            out = "D"
    elif inp[0] == "D":
        if inp[1] == "D":
            out = "0"
        elif inp[1] == "d":
            out = "1"
    elif inp[0] == "d":
        if inp[1] == "D":
            out = "1"
        elif inp[1] == "d":
            out = "0"
    net_dict[gate.output][1] = out


def nand_eval(gate, net_dict):
    inp = []
    for i in gate.input:
        inp.append(net_dict[i][1])
    out = "x"

    if "0" in inp:
        out = "1"
    elif inp[0] == "1":
        if inp[1] == "1":
            out = "0"
        elif inp[1] == "D":
            out = "d"
        elif inp[1] == "d":
            out = "D"
    elif inp[1] == "1":
        if inp[0] == "1":
            out = "0"
        elif inp[0] == "D":
            out = "d"
        elif inp[0] == "d":
            out = "D"
    elif "D" in inp and "d" in inp:
        out = "1"
    elif inp[0] == "d" and inp[1] == "d":
        out = "D"
    elif inp[0] == "D" and inp[1] == "D":
        out = "d"
    net_dict[gate.output][1] = out


def nor_eval(gate, net_dict):
    inp = []
    for i in gate.input:
        inp.append(net_dict[i][1])
    out = "x"

    if "1" in inp:
        out = "0"
    elif inp[0] == "0":
        if inp[1] == "0":
            out = "1"
        elif inp[1] == "D":
            out = "d"
        elif inp[1] == "d":
            out = "D"
    elif inp[1] == "0":
        if inp[0] == "0":
            out = "1"
        elif inp[0] == "D":
            out = "d"
        elif inp[0] == "d":
            out = "D"
    elif "d" in inp and "D" in inp:
        out = "0"
    elif inp[0] == "D" and inp[1] == "D":
        out = "d"
    elif inp[0] == "d" and inp[1] == "d":
        out = "D"
    net_dict[gate.output][1] = out


def xnor_eval(gate, net_dict):
    inp = []
    for i in gate.input:
        inp.append(net_dict[i][1])
    out = "x"

    if inp[0] == inp[1]:
        out = "1"
    elif "1" in inp:
        if "0" in inp:
            out = "0"
        elif "D" in inp:
            out = "D"
        elif "d" in inp:
            out = "d"
    elif "0" in inp:
        if "D" in inp:
            out = "d"
        elif "d" in inp:
            out = "D"
    elif "D" in inp and "d" in inp:
        out = "0"
    net_dict[gate.output][1] = out
    