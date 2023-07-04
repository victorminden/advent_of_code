open Core

let rec zip4 a b c d =
  match List.hd d with
  | None -> []
  | Some _ ->
      (List.hd_exn a, List.hd_exn b, List.hd_exn c, List.hd_exn d)
      :: zip4 (List.tl_exn a) (List.tl_exn b) (List.tl_exn c) (List.tl_exn d)

let rec zip14 x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 =
  match List.hd x13 with
  | None -> []
  | Some _ ->
      ( List.hd_exn x0,
        List.hd_exn x1,
        List.hd_exn x2,
        List.hd_exn x3,
        List.hd_exn x4,
        List.hd_exn x5,
        List.hd_exn x6,
        List.hd_exn x7,
        List.hd_exn x8,
        List.hd_exn x9,
        List.hd_exn x10,
        List.hd_exn x11,
        List.hd_exn x12,
        List.hd_exn x13 )
      :: zip14 (List.tl_exn x0) (List.tl_exn x1) (List.tl_exn x2)
           (List.tl_exn x3) (List.tl_exn x4) (List.tl_exn x5) (List.tl_exn x6)
           (List.tl_exn x7) (List.tl_exn x8) (List.tl_exn x9) (List.tl_exn x10)
           (List.tl_exn x11) (List.tl_exn x12) (List.tl_exn x13)

let part_one s =
  let ell0 = List.init (String.length s) ~f:(String.get s) in
  let ell1 = List.tl_exn ell0 in
  let ell2 = List.tl_exn ell1 in
  let ell3 = List.tl_exn ell2 in

  let ells = zip4 ell0 ell1 ell2 ell3 in
  let maybe_pair =
    ells
    |> List.findi ~f:(fun _i (x0, x1, x2, x3) ->
           Set.length (Set.of_list (module Char) [ x0; x1; x2; x3 ]) = 4)
  in
  match maybe_pair with
  | Some (idx, _) -> idx + 4
  | None -> failwith "bad logic"

let part_two s =
  let ell0 = List.init (String.length s) ~f:(String.get s) in
  let ell1 = List.tl_exn ell0 in
  let ell2 = List.tl_exn ell1 in
  let ell3 = List.tl_exn ell2 in
  let ell4 = List.tl_exn ell3 in
  let ell5 = List.tl_exn ell4 in
  let ell6 = List.tl_exn ell5 in
  let ell7 = List.tl_exn ell6 in
  let ell8 = List.tl_exn ell7 in
  let ell9 = List.tl_exn ell8 in
  let ell10 = List.tl_exn ell9 in
  let ell11 = List.tl_exn ell10 in
  let ell12 = List.tl_exn ell11 in
  let ell13 = List.tl_exn ell12 in

  let ells =
    zip14 ell0 ell1 ell2 ell3 ell4 ell5 ell6 ell7 ell8 ell9 ell10 ell11 ell12
      ell13
  in
  let maybe_pair =
    ells
    |> List.findi
         ~f:(fun _i (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13)
            ->
           Set.length
             (Set.of_list
                (module Char)
                [ x0; x1; x2; x3; x4; x5; x6; x7; x8; x9; x10; x11; x12; x13 ])
           = 14)
  in
  match maybe_pair with
  | Some (idx, _) -> idx + 14
  | None -> failwith "bad logic"

let%test_unit "part_one" =
  [%test_eq: int] ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" |> part_one) 11

let%test_unit "part_two" =
  [%test_eq: int] ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" |> part_two) 26
