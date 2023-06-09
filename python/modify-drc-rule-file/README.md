### modify-drc-rule-file目录脚本usage

1. `interval-modify-drc-rule-file.py`

   读取一个![image-20230606104958012](C:\Users\CHJS\AppData\Roaming\Typora\typora-user-images\image-20230606104958012.png)这样格式的文件，按区间生成

   用法：`python3 <脚本名> <cell名> <起始值> <结束值> <步长> <输入文件> <输出文件>`

   例：`python3 interval-modify.py M1 0 1 0.5 interval.txt output.csv`

   生成如下内容

   ```
   // -----M1 start_cell_000----
   M1_width_1 = M1 with width >= 0.01 <= 0.23
   M1_w1s1_0 = External M1_width_1 M1 > 0.0 <= 0.5 opposite region
   M1_w1s1_1 = M1_w1s1_0 outside M1
   M1_w1s1_2 = not touch edge M1_w1s1_1 M1
   M1_w1s1_2{flatten M1_w1s1_2}
   
   M1_w1s2_0 = External M1_width_1 M1 > 0.5 <= 1.0 opposite region
   M1_w1s2_1 = M1_w1s2_0 outside M1
   M1_w1s2_2 = not touch edge M1_w1s2_1 M1
   M1_w1s2_2{flatten M1_w1s2_2}
   
   M1_width_2 = M1 with width >= 0.25 <= 0.29
   M1_w2s1_0 = External M1_width_2 M1 > 0.0 <= 0.5 opposite region
   M1_w2s1_1 = M1_w2s1_0 outside M1
   M1_w2s1_2 = not touch edge M1_w2s1_2 M1
   M1_w2s1_2{flatten M1_w2s1_2}
   
   M1_w2s2_0 = External M1_width_2 M1 > 0.5 <= 1.0 opposite region
   M1_w2s2_1 = M1_w2s2_0 outside M1
   M1_w2s2_2 = not touch edge M1_w2s2_2 M1
   M1_w2s2_2{flatten M1_w2s2_2}
   ```

2. `new-modify-drc-rule-file.py`

   用法：`python3 <脚本名> <cell名> <起始值> <结束值> <步长> <输出文件>`

   例：`python3 new-modify.py M1 0 1.5 0.5 output.csv `

   生成如下内容:

   ```
   // -----M1 start_cell_000----
   M1_width_1 = M1 with width > 0.0 <=0.5
   M1_width_1 {flatten M1_width_1}
   M1_width_2 = M1 with width > 0.5 <=1.0
   M1_width_2 {flatten M1_width_2}
   M1_width_3 = M1 with width > 1.0 <=1.5
   M1_width_3 {flatten M1_width_3}
   // -----M1 end_cell_000----
   ```

3. `modify-drc-rule-file.py` 

   按0.001精度循环生成输入数的内容

   用法：`python3 <脚本名> <cell名> <起始值>-<结束值> <输出文件>`

   例：`python modify-drc-rule-file.py M1 1-4 output1.txt `

   生成如下内容:

   ```
   // -----M1 start_cell_000----
   M1_width_1 = M1 with width == 0.001
   M1_width_1{flatten M1_width_1}
   M1_width_2 = M1 with width == 0.002
   M1_width_2{flatten M1_width_2}
   M1_width_3 = M1 with width == 0.003
   M1_width_3{flatten M1_width_3}
   M1_width_4 = M1 with width == 0.004
   M1_width_4{flatten M1_width_4}
   // -----M1 end_cell_000----
   ```

4. `space-modify-drc-rule-file.py`

   在`3`的基础上增加space

   用法：`python3 <脚本名> <cell名> <起始值>-<结束值> <space起始值>-<space结束值> <输出文件>`

   例：`python space-modify-drc-rule-file.py M1 1-4 1-2 spaceoutput1.txt`

   生成如下内容：

   ```
   // -----M1 start_cell_000----
   M1_width_1 = M1 with width == 0.001
   M1_width_1{flatten M1_width_1}
   M1_width1_space_1 = External M1_width_1 M1 == 0.001 region
   M1_w1s1 = M1_width1_space_1 outside M1
   M1_w1s1{flatten M1_w1s1}
   M1_width1_space_2 = External M1_width_1 M1 == 0.002 region
   M1_w1s2 = M1_width1_space_2 outside M1
   M1_w1s2{flatten M1_w1s2}
   
   M1_width_2 = M1 with width == 0.002
   M1_width_2{flatten M1_width_2}
   M1_width2_space_1 = External M1_width_2 M1 == 0.001 region
   M1_w2s1 = M1_width2_space_1 outside M1
   M1_w2s1{flatten M1_w2s1}
   M1_width2_space_2 = External M1_width_2 M1 == 0.002 region
   M1_w2s2 = M1_width2_space_2 outside M1
   M1_w2s2{flatten M1_w2s2}
   ... 
   ```

