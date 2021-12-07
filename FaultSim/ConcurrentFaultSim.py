from FaultSim.DeductiveFaultSim import DeductiveFaultSim
from copy import deepcopy
def ConcurrentFaultSim(model, inputs, logfile = ""):
    DFS = DeductiveFaultSim(model, inputs)
    CFS = dict()
    for i in range(1, model.max_level + 1):
        for gate in model.logic_dict[i]:
            CFS[gate.name] = dict()
            # Good gate evaluation
            model.eval(inputs)
            CFS[gate.name]["Good Gate"] = dict()
            CFS[gate.name]["Good Gate"]["input"] = []
            for inp in gate.input:
                CFS[gate.name]["Good Gate"]["input"].append([inp, model.net_dict[inp][1]])
            CFS[gate.name]["Good Gate"]["output"] = [gate.output, model.net_dict[gate.output][1]]
            # Bad Gates
            CFS[gate.name]["Bad Gates"] = []
            for fault_str in DFS[gate.output]:
                fault = fault_str.split(" ")
                model.eval(inputs, fault[0], fault[1][-1])
                temp = dict()
                temp["input"] = []
                temp["Fault"] = fault_str
                for inp in gate.input:
                    temp["input"].append([inp, model.net_dict[inp][1]])
                temp["output"] = [gate.output, model.net_dict[gate.output][1]]
                CFS[gate.name]["Bad Gates"].append(temp)
    return CFS


def ConcurrentFaultSimLogger(CFS, filename, Inputs):
    with open(filename, "w") as fd:
        fd.write("********** Concurrent Fault Simulation **********\n")
        fd.write("Test Vectors: \n")
        for i in Inputs:
            fd.write(i[0] + " : " + i[1] + "\n")
        fd.write("Starting CFS....\n\n")
        for key, value in CFS.items():
            fd.write("Gate: " + key + "\n")
            fd.write("Good Gate: \nInputs: \n")
            for i in value["Good Gate"]["input"]:
                fd.write(i[0] + " : " + i[1] + "\n")
            fd.write("Output: \n" + value["Good Gate"]["output"][0] + " : " + value["Good Gate"]["output"][1] + "\n")

            fd.write("\nBad Gates: \n\n")
            for k in value["Bad Gates"]:
                fd.write("Fault: " + k["Fault"] + "\n")
                fd.write("Inputs: \n")
                for i in k["input"]:
                    fd.write(i[0] + " : " + i[1] + "\n")
                fd.write("Output: \n" + k["output"][0] + " : " + k["output"][1] + "\n\n")
            fd.write("\n\n")
