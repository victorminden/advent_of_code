open Core
open Util

let sums s =
  let sum_lines s =
    s |> String.split ~on:'\n' |> List.filter ~f:not_empty
    |> List.map ~f:Int.of_string |> List.fold ~init:0 ~f:( + )
  in
  s
  |> Str.split (Str.regexp "\n\n")
  |> List.filter ~f:not_empty |> List.map ~f:sum_lines

let part_one s = s |> sums |> List.fold ~init:Int.min_value ~f:max

let part_two s =
  let s1, s2 = List.split_n (sums s) 3 in
  let h = Pairing_heap.of_list s1 ~cmp:( - ) in
  let process x =
    if x > Pairing_heap.top_exn h then (
      Pairing_heap.remove_top h;
      Pairing_heap.add h x)
  in

  List.iter s2 ~f:process;
  Pairing_heap.fold h ~init:0 ~f:( + )

let example_data =
  {|
        1000
        2000
        3000

        4000

        5000
        6000

        7000
        8000
        9000

        10000
|}
  |> String.split ~on:'\n' |> List.tl_exn |> List.map ~f:String.strip
  |> String.concat ~sep:"\n"

let%test_unit "part_one" = [%test_eq: int] (example_data |> part_one) 24000
let%test_unit "part_two" = [%test_eq: int] (example_data |> part_two) 45000
