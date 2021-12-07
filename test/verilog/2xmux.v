module 2xmux(a0, a1, s, o);
/*PARSER Netstart*/
input a0;
input a1;
input s;

wire s1;
wire s2;

wire s3;
wire b1;

wire b0;

output o;
/*PARSER Netend*/

/*PARSER Logicstart*/
buf buf0(s1, s);
buf buf1(s2, s);
not not0(s3, s2);
and and0(b1, a1, s1);
and and1(b0, a0, s3);
or or0(o, b0, b1);
/*PARSER Logicend*/
endmodule
