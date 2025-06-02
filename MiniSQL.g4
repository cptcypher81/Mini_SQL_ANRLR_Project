grammar MiniSQL;

program : statement+ EOF ;

statement
    : selectStmt ';'
    | insertStmt ';'
    | deleteStmt ';'
    | updateStmt ';'
    ;

// SELECT
selectStmt
    : SELECT distinctModifier? columnList FROM tableName (WHERE condition)? (ORDER BY orderList)? (LIMIT NUMBER)?
    ;

columnList
    : '*'                             # allColumns
    | columnName (',' columnName)*   # specificColumns
    ;

// INSERT
insertStmt
    : INSERT INTO tableName '(' columnName (',' columnName)* ')' VALUES '(' literal (',' literal)* ')'
    ;

// DELETE
deleteStmt
    : DELETE FROM tableName (WHERE condition)?
    ;

// UPDATE
updateStmt
    : UPDATE tableName SET assignment (',' assignment)* (WHERE condition)?
    ;

assignment
    : columnName '=' literal
    ;

// WHERE condition
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

// ORDER BY
orderList
    : orderItem (',' orderItem)*
    ;

orderItem
    : columnName (ASC | DESC)?
    ;    

distinctModifier
    : DISTINCT
    ;

expression
    : columnName
    | literal
    ;

comparator
    : '=' | '!=' | '<' | '<=' | '>' | '>='
    ;

// Terminals
columnName : IDENTIFIER ;
tableName  : IDENTIFIER ;
literal    : STRING | NUMBER ;

// Keywords
SELECT : 'SELECT' ;
INSERT : 'INSERT' ;
INTO   : 'INTO' ;
VALUES : 'VALUES' ;
DELETE : 'DELETE' ;
FROM   : 'FROM' ;
WHERE  : 'WHERE' ;
UPDATE : 'UPDATE' ;
SET    : 'SET' ;
AND    : 'AND' ;
OR     : 'OR' ;
ORDER : 'ORDER' ;
BY    : 'BY' ;
ASC : 'ASC';
DESC : 'DESC';
LIMIT: 'LIMIT';
DISTINCT : 'DISTINCT';

// Tokens
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER     : [0-9]+ ;
STRING     : '\'' (~['\r\n])* '\'' ;

// Whitespace and comments
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '--' ~[\r\n]* -> skip ;
