### statistic-numbers目录

1. `extract-data.py`

   读取metal_2.sum中的非零有效数字，转换为千分位小数

   用法：`python3 <脚本名> <输入文件> <输出文件>`

   例：`python extract-data.py metal_2.sum step1.csv `

   输出内容为：

   ```
   0.090
   0.096
   0.097
   0.099
   0.100
   0.102
   0.105
   0.107
   0.110
   ...
   ```

2. `statistic-numbers-p2.py`

   将`1`中提取出的数字按百分位`0.0x`统计

   用法：`python3 <脚本名> <输入文件> <输出文件>`

   ==`<输入文件>`为脚本`extract-data.py`提取的文件==

   例：`statistic-numbers-p2.py step1.csv step2.csv`

   输出内容为：

   ```
   [0.09, 1.31]	[123 numbers] [percentage: 60.00%]
   [1.33, 1.5]	[18 numbers] [percentage: 8.78%]
   [1.52, 1.54]	[3 numbers] [percentage: 1.46%]
   [1.57, 1.63]	[7 numbers] [percentage: 3.41%]
   [1.65, 1.67]	[3 numbers] [percentage: 1.46%]
   ...
   ```

3. `statistic-number-p3.py`

   将`1`中提取出的数字按千分位`0.00x`统计

   用法：`python3 <脚本名> <输入文件> <输出文件>`

   ==`<输入文件>`为脚本`extract-data.py`提取的文件==

   例：`statistic-numbers-p3.py step1.csv step2.csv`

   输出内容为：

   ```
   [0.096, 0.097]	[2 numbers] [percentage: 0.25%]
   [0.099, 0.1]	[2 numbers] [percentage: 0.25%]
   [0.102]	[percentage: 0.13%]
   [0.105]	[percentage: 0.13%]
   [0.107]	[percentage: 0.13%]
   ...
   ```

   