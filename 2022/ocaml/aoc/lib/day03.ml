open Core
open Util

let list_of_string s = List.init (String.length s) ~f:(String.get s)
let set_of_list ell = Set.of_list (module Char) ell
let set_of_string = list_of_string >> set_of_list

let intersect3 (s1, s2, s3) =
  s1 |> Set.inter s2 |> Set.inter s3 |> Set.choose_exn

let priority c =
  let lower = Char.lowercase c in
  Char.to_int lower - 96 + if Char.is_lowercase c then 0 else 26

let part_one s =
  let item s =
    let ell = list_of_string s in
    let left, right = List.split_n ell (List.length ell / 2) in
    let inter = Set.inter (set_of_list left) (set_of_list right) in
    Set.choose_exn inter
  in
  s |> String.split ~on:'\n' |> List.filter ~f:not_empty
  |> List.map ~f:(item >> priority)
  |> List.fold ~init:0 ~f:( + )

let part_two s =
  let add_to_triples (triples, acc) x =
    match acc with
    | [ a; b ] ->
        ((set_of_string x, set_of_string a, set_of_string b) :: triples, [])
    | _ -> (triples, x :: acc)
  in
  s |> String.split ~on:'\n' |> List.filter ~f:not_empty
  |> List.fold ~init:([], []) ~f:add_to_triples
  |> fst
  |> List.fold ~init:0 ~f:(fun a b -> a + (b |> intersect3 |> priority))

let example_data =
  {|
        vJrwpWtwJgWrhcsFMMfFFhFp
        jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
        PmmdzqPrVvPwwTWBwg
        wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
        ttgJtRGJQctTZtZT
        CrZsJsPPZsGzwwsLwLmpwMDw
|}
  |> String.split ~on:'\n' |> List.tl_exn |> List.map ~f:String.strip
  |> String.concat ~sep:"\n"

let%test_unit "part_one" = [%test_eq: int] (example_data |> part_one) 157
let%test_unit "part_two" = [%test_eq: int] (example_data |> part_two) 70
