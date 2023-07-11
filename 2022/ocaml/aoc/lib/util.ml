let ( >> ) f g x = g (f x)

type list_or_int = Atom of int | VList of list_or_int list
