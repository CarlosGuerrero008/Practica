grammar MiGramatica;

// Regla principal: permite múltiples sentencias terminadas en ';'
programa: (sentencia ';'?)+ EOF ;

// Sentencias permitidas
sentencia
    : whileStmt   // Solo permitimos `while` y asignaciones
    | asignacion  
    ;

// Regla para `while`
whileStmt
    : 'while' '(' condicion ')' '{' (sentencia (';')?)* '}' # While
    ;

// Condiciones dentro del `while`
condicion
    : ID op=('>' | '<' | '==' | '!=') INT  # CondicionSimple
    | ID op=('>' | '<' | '==' | '!=') ID   # CondicionVariable
    ;

// Asignaciones con `;`
asignacion
    : ID '=' expresion ';'? # Assign  // El ';' es opcional
    ;

// Expresiones matemáticas con prioridad de operadores
expresion
    : expresion op=('*'|'/') expresion     # MulDiv
    | expresion op=('+'|'-') expresion     # AddSub
    | INT                                  # Int
    | ID                                   # Variable
    | '(' expresion ')'                    # Parens
    ;

// Reglas léxicas
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;  // Identificadores
INT : [0-9]+ ;                   // Números enteros
WS  : [ \t\r\n]+ -> skip ;       // Ignorar espacios en blanco