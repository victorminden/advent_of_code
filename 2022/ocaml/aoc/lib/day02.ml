open Core
open Util

let shape_score = function
  | 'X' -> 1
  | 'Y' -> 2
  | 'Z' -> 3
  | _ -> failwith "Bad shape"

let pair_score = function
  | 'A', 'X' | 'B', 'Y' | 'C', 'Z' -> 3
  | 'A', 'Y' | 'B', 'Z' | 'C', 'X' -> 6
  | 'A', 'Z' | 'B', 'X' | 'C', 'Y' -> 0
  | _ -> failwith "Bad pair"

let list_of_pairs s =
  s |> String.split ~on:'\n' |> List.filter ~f:not_empty
  |> List.map ~f:(fun s -> (s.[0], s.[2]))

let part_one s =
  s |> list_of_pairs
  |> List.fold ~init:0 ~f:(fun acc (elf, you) ->
         acc + pair_score (elf, you) + shape_score you)

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

let part_two s =
  s |> list_of_pairs |> List.map ~f:remap_you
  |> List.fold ~init:0 ~f:(fun acc (elf, you) ->
         acc + pair_score (elf, you) + shape_score you)

let example_data =
  {|
        A Y
        B X
        C Z
|} |> String.split ~on:'\n'
  |> List.tl_exn |> List.map ~f:String.strip |> String.concat ~sep:"\n"

let%test_unit "part_one" = [%test_eq: int] (example_data |> part_one) 15
let%test_unit "part_two" = [%test_eq: int] (example_data |> part_two) 12
