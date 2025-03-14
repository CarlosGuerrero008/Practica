echo "a = 10; b = 5 + a * 2; c = (b - 3) / 2;" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig MiGramatica programa -tokens
[@0,0:0='a',<ID>,1:0]
[@1,2:2='=',<'='>,1:2]
[@2,4:5='10',<INT>,1:4]
[@3,6:6=';',<';'>,1:6]
[@4,8:8='b',<ID>,1:8]
[@5,10:10='=',<'='>,1:10]
[@6,12:12='5',<INT>,1:12]
[@7,14:14='+',<'+'>,1:14]
[@8,16:16='a',<ID>,1:16]
[@9,18:18='*',<'*'>,1:18]
[@10,20:20='2',<INT>,1:20]
[@11,21:21=';',<';'>,1:21]
[@12,23:23='c',<ID>,1:23]
[@13,25:25='=',<'='>,1:25]
[@14,27:27='(',<'('>,1:27]
[@15,28:28='b',<ID>,1:28]
[@16,30:30='-',<'-'>,1:30]
[@17,32:32='3',<INT>,1:32]
[@18,33:33=')',<')'>,1:33]
[@19,35:35='/',<'/'>,1:35]
[@20,37:37='2',<INT>,1:37]
[@21,38:38=';',<';'>,1:38]
[@22,40:39='<EOF>',<EOF>,2:0]

$ echo "a = 10; b = 5 + a * 2; c = (b - 3) / 2;" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig MiGramatica programa -tree

(programa (expresion a = (expresion 10)) ; (expresion (expresion b = (expresion 5)) + (expresion (expresion a) * (expresion 2))) ; (expresion (expresion c = (expresion ( (expresion (expresion b) - (expresion 3)) ))) / (expresion 2)) ;)