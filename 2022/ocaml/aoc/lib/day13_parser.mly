%token <int> INT
%token LEFT_BRACK
%token RIGHT_BRACK
%token COMMA
%start <Util.list_or_int> top
%%

top:
  | v = value  {v};

value:
  | LEFT_BRACK; vl = list_fields; RIGHT_BRACK { Util.VList vl }
  | i = INT                                   { Util.Atom i };

list_fields:
    vl = separated_list(COMMA, value)         { vl } ;
