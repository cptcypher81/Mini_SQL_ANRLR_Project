grammar MiniSQL;

program : statement+ EOF ;

statement : selectStmt ';' ;

selectStmt: SELECT columnList FROM tableName (WHERE condition)? ;

columnList
    : '*'                             # allColumns
    | columnName (',' columnName)*   # specificColumns
    ;

condition
    : condition OR andCond           # orCondition
    | andCond                        # singleAnd
    ;

andCond
    : andCond AND baseCond           # andCondition
    | baseCond                       # singleBase
    ;

baseCond
    : expression comparator expression  # baseCondition
    ;

expression: columnName | literal ;

comparator: '=' | '!=' | '<' | '<=' | '>' | '>=' ;

columnName : IDENTIFIER ;
tableName  : IDENTIFIER ;
literal    : STRING | NUMBER ;

// Keywords
SELECT : 'SELECT' ;
FROM   : 'FROM' ;
WHERE  : 'WHERE' ;
AND    : 'AND' ;
OR     : 'OR' ;

// Tokens
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER     : [0-9]+ ;
STRING     : '\'' (~['\r\n])* '\'' ;

// Whitespace and comments
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '--' ~[\r\n]* -> skip ;
