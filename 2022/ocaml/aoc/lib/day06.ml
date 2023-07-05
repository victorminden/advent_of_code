open Core
open Util

let list_of_string s = List.init (String.length s) ~f:(String.get s)

let rec marker_index k ell =
  let next_k =
    let rec aux k' ell' =
      if k' = 0 then [] else List.hd_exn ell' :: aux (k' - 1) (List.tl_exn ell')
    in
    aux k >> Set.of_list (module Char)
  in
  if Set.length (next_k ell) = k then k
  else 1 + marker_index k (List.tl_exn ell)

let part_one = list_of_string >> marker_index 4
let part_two = list_of_string >> marker_index 14

let%test_unit "part_one" =
  [%test_eq: int] ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" |> part_one) 11

let%test_unit "part_two" =
  [%test_eq: int] ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" |> part_two) 26
