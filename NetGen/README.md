# Rules for writing verilog modules
## Precautions
- Present version of parser only works for combinational circuits
- Only gate level modeling is supported (and, or, not, nand, nor, xor, xnor, buf)
## Module Rules
### Defining Nets
- /\*PARSER Netstart*/ comment should precede the declaration of nets and /\*PARSER Netend*/ comment should mark the end of the net declaration.
- All the nets should be written in data dependence order with a blank line separating each level. (Primary Input - level 0, Primary Output - Max level possible)

### Defining Logic
- /\*PARSER Logicstart*/ comment should precede the start of logic declaration and /\*PARSER Logicend*/ comment should mark the end of the logic declaration.
- All gates should be in the following format: gate_type gate_name(out, in1, in2);