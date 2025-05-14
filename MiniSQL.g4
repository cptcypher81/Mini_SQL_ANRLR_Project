grammar MiniSQL;

program : statement+ EOF ;

statement : selectStmt ';';

selectStmt: SELECT columnList FROM tableName (WHERE condition)?;

columnList
    : '*'                                # allColumns
    | columnName (',' columnName)*      # specificColumns
    ;

condition: expression comparator expression;

expression: columnName | literal;

comparator: '=' | '!=' | '<' | '<=' | '>' | '>=';

columnName : IDENTIFIER ;
tableName  : IDENTIFIER ;
literal    : STRING | NUMBER ;

// Tokens
SELECT  : 'SELECT' ;
FROM    : 'FROM' ;  
WHERE   : 'WHERE' ;

IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER     : [0-9]+ ;
STRING     : '\'' (~['\r\n])* '\'' ;

// Ignore whitespace and comments
WS : [ \t\r\n]+ -> skip ;
COMMENT : '--' ~[\r\n]* -> skip ;
