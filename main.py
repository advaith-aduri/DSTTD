import pprint as pp
import NetGen.model as model
import NetGen.parser as parser
import SCOAP.SCOAP as SCOAP
from FaultSim.DeductiveFaultSim import DeductiveFaultSim
from FaultSim.ConcurrentFaultSim import ConcurrentFaultSim, ConcurrentFaultSimLogger

if __name__ == '__main__':
    net_dict, logic_list = parser.parser("./test/verilog/2xmux.v")
    mux = model.LogicModel(net_dict, logic_list)
    net_dict, logic_list = parser.parser("./test/verilog/multiplier_2bit.v")
    mult = model.LogicModel(net_dict, logic_list)
    net_cc = SCOAP.SCOAP(mult, "test/logs/SCOAP.log")
    pp.pprint(net_cc) 

    # DFS
    """ Inputs = [
        ["a0", "1"],
        ["a1", "0"],
        ["s", "0"]
    ]
    DFS = DeductiveFaultSim(mux, Inputs)
    print("Starting Deductive Fault Simulation(2xmux): ")
    pp.pprint(DFS) """

    Inputs = [
        ["a0", "1"],
        ["a1", "1"],
        ["b0", "1"],
        ["b1", "1"],
    ]
    """ DFS = DeductiveFaultSim(mult, Inputs)
    print("Starting Deductive Fault Simulation(mult): ")
    pp.pprint(DFS) """
"""     CFS = ConcurrentFaultSim(mult, Inputs)
    ConcurrentFaultSimLogger(CFS, "./test/logs/CFS.logs", Inputs) """
    


