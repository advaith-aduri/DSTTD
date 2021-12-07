from NetGen import model


def parser(file):
    """

    :param file: Path to verilog source
    :return parser_out: (net_dict, logic_list)
    :var net_dict: A dictionary consisting of nets along with their level and value
    """
    net_dict = dict()
    logic_list = list()

    print("Satrting file parsing...")
    with open(file, "r") as fd:
        while True:
            line = fd.readline()
            if not line:
                break
            line = line.lstrip()
            line = line.rstrip()
            line = line.rstrip("\n")

            # Start reading nets
            if "/*PARSER Netstart*/" in line:
                while True:
                    line = fd.readline()                            
                    line = line.lstrip()
                    line = line.rstrip()
                    line = line.rstrip("\n")
                    line = line.rstrip(";")
                    if "/*PARSER Netend*/" in line:
                        break
                    if line == '':
                        continue
                    line_buf = line.split(" ")
                    net_dict[line_buf[-1]] = [-1, "x"]
            
            # Start reading logic gates
            if "/*PARSER Logicstart*/" in line:
                while True:
                    line = fd.readline()
                    line = line.lstrip()
                    line = line.rstrip()
                    line = line.rstrip("\n")
                    line = line.rstrip(";")
                    if "/*PARSER Logicend*/" in line:
                        break
                    line = line.replace(", ", ",")
                    line = line.replace(" ", ",")
                    line = line.replace("(", ",")
                    line_buf = line.replace(")", "")
                    logic_list.append(model.GateModel(line_buf.split(",")))
    return net_dict, logic_list



def gate_levelization(net_list, logic_list):
    net_level = dict()
    net_level_completed = set() 
    # Assign a initial level of -1 to all nets
    for i in net_list:
        net_level[i] = -1
    
    # Find primary inputs: They are not output to any gate
    for i in net_list:
        is_primary_input = True
        for gate in logic_list:
            if i == gate.output:
                is_primary_input = False
                continue
        if is_primary_input:
            net_level_completed.add(i)
            net_level[i] = 0
    
    # Finding Levels for other wires
    while len(net_level_completed) != len(net_list):
        for gate in logic_list:
            all_input_leveled = True
            for inp in gate.input:
                if inp not in net_level_completed:
                    all_input_leveled = False
            if all_input_leveled:
                net_level[gate.output] = max([net_level[inp] for inp in gate.input]) + 1
                net_level_completed.add(gate.output)

    return net_level
        

