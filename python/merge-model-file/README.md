根据要求处理 [MANGO_R2.04.zip](MANGO_R2.04.zip) 中的文件。



解压后，目录中有一些`.lib`后缀的文件：

- diode.lib
- mc_model.lib
- NF_model.lib
- ……



这些文件都以类似如下的格式分段记录，

1. 第1行以`.lib` +**空白字符**+**一个名字**（如上文的`dio_tt`或`tt`）组成

   如`.lib dio_tt`。注意，这个名字（也就是后一段字符）可能是大写或者小写，但是最终处理时都要转换成小写。

   

2. 第2行为`.param`

   紧接着可能有一行（也可能不止一行）注释内容。

   `*`开始的行为注释行，这里无需关注`.lib`文件具体的语言格式，知道`*`行为注释行即可。

   

3. 接着直到出现`.lib 'xxx.lib' core`的行为止（下面说明），中间的内容就是具体的cell数据

   它们的格式均形如 `aaa = bbb`，如`dcjsws_nfmeq = 0`，等号前面的字母最前面的字符可能是`+`，如`+dis_ndio = 0`

   一行中可能又一个或多个这样形式的内容。

   

4. 然后是`.lib 'xxx.lib' core`行，

   

5. 最后是`.endl`开始的行



例如diode.lib部分内容，一段关于`dio_tt`的`lib`信息：

> ```shell
> .lib dio_tt
> .param
> * DIODE 
> +dis_ndio = 0
> +djsw_ndio = 0
> +dn_ndio = 0
> +dcj_ndio = 0
> +dcjsw_ndio = 0 
> *...省略一些行
> .lib 'diode.lib' dio_core
> .endl dio_tt
> ```

又例如NF_model.lib部分内容，一段完整的关于`tt`的`lib`信息，这里就称之为`tt`部分：````

> ```shell
> .lib tt
> .param
> * PERI THIN NORMAL VT NMOS
> +dtoxe_n_nf = 0             dtoxp_n_nf = 0              dxl_n_nf = 0                
> +dxw_n_nf = 0               dlvth0_n_nf = 0             dlu0_n_nf = 0  
> +dvsat_n_nf = 0             djtsswgd_n_nf = 0           dcjs_n_nf = 1
> +dcjd_n_nf = 1              dcjsws_n_nf = 1             dcjswd_n_nf = 1           
> +dcjswgs_n_nf = 1           dcjswgd_n_nf = 1            dcgsl_n_nf = 1
> +dcgdl_n_nf = 1             dcgso_n_nf = 1              dcgdo_n_nf = 1
> +dcf_n_nf = 1               dnfactor_n_nf = 0           dags_n_nf = 0
> +dvth0_n_nf = 0             du0_n_nf = 0                dute_n_nf = 0
> +dpu0_n_nf = 0
> .lib 'NF_model.lib' core
> .endl tt
> ```

需求是将所有文件中相同名字的`lib`部分合在一起，最终写入到一个名为`all_model.lib`的文件。

比如`tt`部分所有`.lib`后缀的文件中都存在，那么要

- 将所有文件中的`tt`部分融合成一个`tt`段



- 所有的注释行（以`*`开头）保留原样

  

- 每部分的倒数第2行`.lib xxx core`行不需要

  参看下面的例子，最终只需要一个相同的`.lib "./all_model.lib"  core`行

  

- 每个文件的都有相同的前两行（`.lib tt`及`.param`）和最后一行`endl tt`，他们在最终汇总的`tt`只需要保留一份即可，



汇总的tt形式：

这里的`#`及后面的内容只是为了方便说明，最终生成的文件不包含这些。空白行也只是为了便于阅读，最终生成的文件中不需要。

```shell
.lib tt   #注意有的文件中是TT，两者表示同一种
.param    #param行，必须

#---以下读取自第1个文件当的tt部分
* DIODE                  #第一个文件中的注释行，原样写入即可
#第1个含有tt段落的lib文件中的cell行，即使 aaa = bbb形式的行

#---以下读取自第2个文件当的tt部分
* CORE TR. CSL, YSW      #第2个文件中的注释行，原样写入即可
#第2个含有tt段落的lib文件中的cell行，即使 aaa = bbb形式的行

#...

#---以下读取自第n个文件当的tt部分
* nnnnnnn                #第n个文件中的注释行，原样写入即可
#第n个含有tt段落的lib文件中的cell行，即使 aaa = bbb形式的行

.lib "./all_model.lib"  core   #这一行是固定的
.endl tt                       #.endl都是一样的，后面是tt


.lib ff
.param

#...参照上面tt的形式


.lib "./all_model.lib"  core   #这一行是固定的
.endl ff                       #.endl都是一样的，后面是ff
```



---

参考说明，同事发来的针对该处理任务的说明邮件，根据情况有所修改：

> This time seperated model files to merge ONE file. 
>
> That's should be easy to simulate for desinger. 
>
> 
>
> Model files are same here, 순서대로 진행되어야 한다. 
>
> ```shell
> NF_model.lib     NFL_model.lib     PF_model.lib PFL_model.lib 
> 
> nflsa_model.lib    nfcsl_model.lib    nfpeq_model.lib 
> 
> nfmeq_model.lib    nfmeq_model.lib    pflsa_model.lib
> 
> NFT_model.lib     NFLT_model.lib    nft_hci_model.lib
> 
> PFT_model.lib     PFLT_model.lib    pft_heip_model.lib
> 
> nfth_hci_model.lib  nfthp_hci_model.lib  pft_heip2_model.lib 
> 
> mc_model.lib     diode.lib       resistor.lib 
> ```
>
> ​    
>
> There are 21 files,  each model looks like this,
>
> 1stly corner skew merge like this, 
>
> ![merge-files](doc-imgs/merge-files-1.png)
>
> 2ndly all model file merge like this. 
>
> this is simple copy and move from `.lib` core to `.endl` core 
>
> ![merge-files-2](doc-imgs/merge-files-2.png)

