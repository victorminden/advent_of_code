let ( >> ) f g x = g (f x)
let not_empty s = not (String.equal s "")
