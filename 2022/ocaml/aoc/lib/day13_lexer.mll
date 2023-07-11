{
open Day13_parser

exception SyntaxError of string
}

let int = '-'? ['0'-'9'] ['0'-'9']*

rule read =
  parse
  | int      { INT (int_of_string (Lexing.lexeme lexbuf)) }
  | '['      { LEFT_BRACK }
  | ']'      { RIGHT_BRACK }
  | ','      { COMMA }
  | _ { raise (SyntaxError ("Unexpected char: " ^ Lexing.lexeme lexbuf)) }
