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

let replace_words s =
  s
  |> Re2.rewrite_exn (Re2.create_exn "one") ~template:"one1one"
  |> Re2.rewrite_exn (Re2.create_exn "two") ~template:"two2two"
  |> Re2.rewrite_exn (Re2.create_exn "three") ~template:"three3three"
  |> Re2.rewrite_exn (Re2.create_exn "four") ~template:"four4four"
  |> Re2.rewrite_exn (Re2.create_exn "five") ~template:"five5five"
  |> Re2.rewrite_exn (Re2.create_exn "six") ~template:"six6six"
  |> Re2.rewrite_exn (Re2.create_exn "seven") ~template:"seven7seven"
  |> Re2.rewrite_exn (Re2.create_exn "eight") ~template:"eight8eight"
  |> Re2.rewrite_exn (Re2.create_exn "nine") ~template:"nine9nine"

let part_two s =
  s |> String.split_lines |> List.map ~f:String.strip
  |> List.map ~f:replace_words
  |> List.map ~f:calibration_value
  |> List.fold ~init:0 ~f:( + )

let example_data_one = {|1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
|}

let example_data_two =
  {|two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
|}

let%test_unit "part_one" = [%test_eq: int] (example_data_one |> part_one) 142
let%test_unit "part_two" = [%test_eq: int] (example_data_two |> part_two) 281
