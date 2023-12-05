open Core
open Util

let calibration_value s =
  let digits =
    s |> list_of_string |> List.filter ~f:is_digit |> List.map ~f:char_to_int
  in
  ((digits |> List.hd_exn) * 10) + (digits |> List.rev |> List.hd_exn)

let part_one s =
  s |> String.split_lines |> List.map ~f:String.strip
  |> List.map ~f:calibration_value
  |> List.fold ~init:0 ~f:( + )

let example_data = {|1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
|}

let%test_unit "part_one" = [%test_eq: int] (example_data |> part_one) 142
