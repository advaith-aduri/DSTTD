
def SCOAP(model, logfile = ""):
    net_cc = dict()
    for key in model.net_dict.keys():
        net_cc[key] = dict()
        net_cc[key]["cc0"] = 1
        net_cc[key]["cc1"] = 1
        net_cc[key]["co"] = 0
    
    # Starting algo for controllibility
    for i in range(1, model.max_level + 1):
        for gate in model.logic_dict[i]:
            if gate.type == "not":
                net_cc[gate.output]["cc0"] = net_cc[gate.input[0]]["cc1"] + 1
                net_cc[gate.output]["cc1"] = net_cc[gate.input[0]]["cc0"] + 1 
            elif gate.type == "buf":
                net_cc[gate.output]["cc0"] = net_cc[gate.input[0]]["cc0"]
                net_cc[gate.output]["cc1"] = net_cc[gate.input[0]]["cc1"]
            elif gate.type == "and":
                net_cc[gate.output]["cc0"] = min(net_cc[gate.input[0]]["cc0"], net_cc[gate.input[1]]["cc0"]) + 1
                net_cc[gate.output]["cc1"] = net_cc[gate.input[0]]["cc1"] + net_cc[gate.input[1]]["cc1"] + 1
            elif gate.type == "nand":
                net_cc[gate.output]["cc0"] = net_cc[gate.input[0]]["cc1"] + net_cc[gate.input[1]]["cc1"] + 1
                net_cc[gate.output]["cc1"] = min(net_cc[gate.input[0]]["cc0"], net_cc[gate.input[1]]["cc0"]) + 1
            elif gate.type == "or":
                net_cc[gate.output]["cc0"] = net_cc[gate.input[0]]["cc0"] + net_cc[gate.input[1]]["cc0"] + 1
                net_cc[gate.output]["cc1"] = min(net_cc[gate.input[0]]["cc1"], net_cc[gate.input[1]]["cc1"]) + 1
            elif gate.type == "nor":
                net_cc[gate.output]["cc0"] = min(net_cc[gate.input[0]]["cc1"], net_cc[gate.input[1]]["cc1"]) + 1
                net_cc[gate.output]["cc1"] = net_cc[gate.input[0]]["cc0"] + net_cc[gate.input[1]]["cc0"] + 1
            elif gate.type == "xor":
                net_cc[gate.output]["cc0"] = min(net_cc[gate.input[0]]["cc0"] + net_cc[gate.input[1]]["cc0"], net_cc[gate.input[0]]["cc1"] + net_cc[gate.input[1]]["cc1"]) + 1
                net_cc[gate.output]["cc1"] = min(net_cc[gate.input[0]]["cc1"] + net_cc[gate.input[1]]["cc0"], net_cc[gate.input[0]]["cc0"] + net_cc[gate.input[1]]["cc1"]) + 1
                
    # Starting algo for observability

    for i in range(model.max_level, 0, -1):
        for gate in model.logic_dict[i]:
            if gate.type == "buf":
                min_fanout = net_cc[gate.output]["co"]
                for f_gate in model.logic_dict[i]:
                    if f_gate.type == "buf" and f_gate.input == gate.input and f_gate.output != gate.output:
                        min_fanout = min(min_fanout, net_cc[f_gate.output]["co"])
                net_cc[gate.input[0]]["co"] = min_fanout
            elif gate.type == "not":
                net_cc[gate.input[0]]["co"] = net_cc[gate.output]["co"] + 1
            elif gate.type == "and" or gate.type == "nand":
                net_cc[gate.input[0]]["co"] = net_cc[gate.output]["co"] + net_cc[gate.input[1]]["cc1"] + 1
                net_cc[gate.input[1]]["co"] = net_cc[gate.output]["co"] + net_cc[gate.input[0]]["cc1"] + 1
            elif gate.type == "or" or gate.type == "nor":
                net_cc[gate.input[0]]["co"] = net_cc[gate.output]["co"] + net_cc[gate.input[1]]["cc0"] + 1
                net_cc[gate.input[1]]["co"] = net_cc[gate.output]["co"] + net_cc[gate.input[0]]["cc0"] + 1
            elif gate.type == "xor":
                net_cc[gate.input[0]]["co"] = net_cc[gate.output]["co"] + min(net_cc[gate.input[1]]["cc0"], net_cc[gate.input[1]]["cc1"]) + 1
                net_cc[gate.input[1]]["co"] = net_cc[gate.output]["co"] + min(net_cc[gate.input[0]]["cc0"], net_cc[gate.input[0]]["cc1"]) + 1
    
    # Logging the values
    if logfile != "":
        with open(logfile, "w") as fd:
            fd.write("**********\tSCOAP Controllability and Observability\t**********\n")
            fd.write("Net Name\t\tCC0\t\tCC1\t\tCO\n")
            for key, value in net_cc.items():
                fd.write("{:8}\t\t{:3}\t\t{:3}\t\t{:2}\n".format(key, str(value["cc0"]), str(value["cc1"]), str(value["co"])))

    return net_cc