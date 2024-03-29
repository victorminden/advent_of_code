open Core
open Util

let parse_range_pairs s =
  let ell =
    s |> String.split ~on:','
    |> List.map ~f:(String.split ~on:'-')
    |> List.map ~f:(List.map ~f:Int.of_string)
  in
  match ell with
  | [ [ a; b ]; [ c; d ] ] -> ((a, b), (c, d))
  | _ -> failwith "Bad string"

let contains (a, b) c = a <= c && c <= b
let contains_range r (c, d) = contains r c && contains r d

let part_one =
  String.split_lines
  >> List.map ~f:parse_range_pairs
  >> List.fold ~init:0 ~f:(fun acc (r1, r2) ->
         acc + Bool.to_int (contains_range r1 r2 || contains_range r2 r1))

let part_two =
  String.split_lines
  >> List.map ~f:parse_range_pairs
  >> List.fold ~init:0 ~f:(fun acc ((a, b), (c, d)) ->
         acc
         + Bool.to_int
             (contains (a, b) c
             || contains (a, b) d
             || contains (c, d) a
             || contains (c, d) b))

let example_data = {|2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
|}

let%test_unit "part_one" = [%test_eq: int] (example_data |> part_one) 2
let%test_unit "part_two" = [%test_eq: int] (example_data |> part_two) 4
