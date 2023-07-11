open Core

let parse line = line |> Lexing.from_string |> Day13_parser.top Day13_lexer.read

type comparison_result = LessThan | GreaterThan | Equal

let rec lt =
  let open Util in
  function
  | Atom a, Atom b ->
      if a < b then LessThan else if a > b then GreaterThan else Equal
  | VList a, Atom b -> lt (VList a, VList [ Atom b ])
  | Atom a, VList b -> lt (VList [ Atom a ], VList b)
  | VList a, VList b -> (
      let maybe_result =
        Sequence.zip (Sequence.of_list a) (Sequence.of_list b)
        |> Sequence.fold ~init:None ~f:(fun acc (i, j) ->
               match acc with
               | Some Equal ->
                   failwith "Unexpected equality during intermediate fold"
               | None -> (
                   match lt (i, j) with
                   | LessThan -> Some LessThan
                   | GreaterThan -> Some GreaterThan
                   | Equal -> None)
               | other -> other)
      in
      match maybe_result with
      | Some v -> v
      | None -> lt (Atom (List.length a), Atom (List.length b)))

let part_one s =
  s |> String.split_lines
  |> List.fold ~init:([], []) ~f:(fun (pairs, curr) -> function
       | "" -> (List.rev curr :: pairs, []) | line -> (pairs, parse line :: curr))
  |> fst |> List.rev
  |> List.map ~f:(function
       | [ a; b ] -> (a, b)
       | _ -> failwith "did not get list of 2")
  |> List.foldi ~init:0 ~f:(fun i acc pair ->
         match lt pair with LessThan -> acc + i + 1 | _ -> acc)

let compare a b =
  match lt (a, b) with LessThan -> -1 | Equal -> 0 | GreaterThan -> 1

let part_two s =
  let xs =
    s |> String.split_lines |> List.filter ~f:(fun x -> not (String.equal x ""))
  in
  let xs' = "[[2]]" :: "[[6]]" :: xs |> List.map ~f:(fun x -> (x, parse x)) in
  let sorted = xs' |> List.sort ~compare:(fun a b -> compare (snd a) (snd b)) in
  let find lst v =
    match List.findi ~f:(fun _ x -> String.equal (fst x) v) lst with
    | Some (i, _) -> i + 1
    | _ -> failwith "Bad sort"
  in
  find sorted "[[2]]" * find sorted "[[6]]"

let example_data =
  {|[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]|}

let%test_unit "part_one" = [%test_eq: int] (example_data |> part_one) 13
let%test_unit "part_two" = [%test_eq: int] (example_data |> part_two) 140
