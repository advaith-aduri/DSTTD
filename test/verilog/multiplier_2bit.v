module multiplier_2bit(a0, a1, b0, b1, c0, c1, c2, c3);

/*PARSER Netstart*/
input a0;
input a1;
input b0;
input b1;
output c0;
output c1;
output c2;
output c3;
wire a0_0;
wire a0_1;
wire a1_0;
wire a1_1;
wire b0_0;
wire b0_1;
wire b1_0;
wire b1_1;
wire and_01;
wire and_01_0;
wire and_01_1;
wire and_10;
wire and_10_0;
wire and_10_1;
wire and_11;
wire and_11_0;
wire and_11_1;
wire cot1;
wire cot1_0;
wire cot1_1;
/*PARSER Netend*/

/*PARSER Logicstart*/
buf b0(a0_0, a0);
buf b1(a0_1, a0);
buf b2(a1_0, a1);
buf b3(a1_1, a1);
buf b4(b0_0, b0);
buf b5(b0_1, b0);
buf b6(b1_0, b1);
buf b7(b1_1, b1);
and a0(c0, a0_0, b0_0);
and a1(and_01, a1_0, b0_1);
and a2(and_10, a0_1, b1_0);
and a3(and_11, a1_1, b1_1);
buf b8(and_01_0, and_01);
buf b9(and_01_1, and_01);
buf b10(and_10_0, and_10);
buf b11(and_10_1, and_10);
buf b12(and_11_0, and_11);
buf b13(and_11_1, and_11);
and fa1a1(cot1, and_01_0, and_10_0);
xor fa1x1(c1, and_01_1, and_10_1);
buf b14(cot1_0, cot1);
buf b15(cot1_1, cot1);
and fa1a2(c3, and_11_0, cot1_0);
xor fa1x2(c2, and_11_1, cot1_1);
/*PARSER Logicend*/
endmodule