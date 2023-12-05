let ( >> ) f g x = g (f x)
let is_digit = function '0' .. '9' -> true | _ -> false

let char_to_int = function
  | '9' -> 9
  | '8' -> 8
  | '7' -> 7
  | '6' -> 6
  | '5' -> 5
  | '4' -> 4
  | '3' -> 3
  | '2' -> 2
  | '1' -> 1
  | _ -> 0

let list_of_string s = List.init (String.length s) (String.get s)
