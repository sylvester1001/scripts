```text
// -----M1 star_cell_000----
M1_width_1 = M1 with width == 0.001
M1_width_1{flatten M1_width_1}
M1_width_space_1 = External M1_width_1 M1 == 0.001 region
M1_width_space_1{flatten M1_width_space_1}
M1_width_space_2 = External M1_width_1 M1 == 0.002 region
M1_width_space_2{flatten M1_width_space_2}
M1_width_space_3 = External M1_width_1 M1 == 0.003 region
M1_width_space_3{flatten M1_width_space_3}
M1_width_space_4 = External M1_width_1 M1 == 0.004 region
M1_width_space_4{flatten M1_width_space_4}
M1_width_space_5 = External M1_width_1 M1 == 0.005 region
M1_width_space_5{flatten M1_width_space_5}

M1_width_2 = M1 with width == 0.002
M1_width_2{flatten M1_width_2}
M1_width_space_1 = External M1_width_2 M1 == 0.001 region
M1_width_space_1{flatten M1_width_space_1}
M1_width_space_2 = External M1_width_2 M1 == 0.002 region
M1_width_space_2{flatten M1_width_space_2}
M1_width_space_3 = External M1_width_2 M1 == 0.003 region
M1_width_space_3{flatten M1_width_space_3}
M1_width_space_4 = External M1_width_2 M1 == 0.004 region
M1_width_space_4{flatten M1_width_space_4}
M1_width_space_5 = External M1_width_2 M1 == 0.005 region
M1_width_space_5{flatten M1_width_space_5}
```

生成一个数字0-1000，width为0-1000/1000

space_var为另一组变量控制space