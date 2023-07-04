open Core
open Util

let score (elf, you) =
  let shape_score = function
    | 'X' -> 1
    | 'Y' -> 2
    | 'Z' -> 3
    | _ -> failwith "Bad shape"
  in
  let pair_score = function
    | 'A', 'X' | 'B', 'Y' | 'C', 'Z' -> 3
    | 'A', 'Y' | 'B', 'Z' | 'C', 'X' -> 6
    | 'A', 'Z' | 'B', 'X' | 'C', 'Y' -> 0
    | _ -> failwith "Bad pair"
  in
  pair_score (elf, you) + shape_score you

let list_of_pairs = String.split_lines >> List.map ~f:(fun s -> (s.[0], s.[2]))

let part_one =
  list_of_pairs >> List.fold ~init:0 ~f:(fun acc pair -> acc + score pair)

let part_two =
  let remap_you = function
    | 'A', 'X' -> ('A', 'Z')
    | 'A', 'Y' -> ('A', 'X')
    | 'A', 'Z' -> ('A', 'Y')
    | 'B', 'X' -> ('B', 'X')
    | 'B', 'Y' -> ('B', 'Y')
    | 'B', 'Z' -> ('B', 'Z')
    | 'C', 'X' -> ('C', 'Y')
    | 'C', 'Y' -> ('C', 'Z')
    | 'C', 'Z' -> ('C', 'X')
    | _ -> failwith "Bad pair"
  in
  list_of_pairs >> List.map ~f:remap_you
  >> List.fold ~init:0 ~f:(fun acc pair -> acc + score pair)

let example_data = {|A Y
B X
C Z
|}

let%test_unit "part_one" = [%test_eq: int] (example_data |> part_one) 15
let%test_unit "part_two" = [%test_eq: int] (example_data |> part_two) 12
