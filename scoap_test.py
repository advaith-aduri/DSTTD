import NetGen.model as model
import NetGen.parser as parser
import SCOAP.SCOAP as SCOAP
import pprint as pp

if __name__ == "__main__":
    net_dict, logic_list = parser.parser("./test/verilog/multiplier_2bit.v")
    mult = model.LogicModel(net_dict, logic_list)
    net_cc = SCOAP.SCOAP(mult, "test/logs/SCOAP.log")
    pp.pprint(net_cc) 