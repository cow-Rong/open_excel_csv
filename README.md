# Oel类
##### 这是一个读取Excel/csv文件的Python类

> 读取xls、xlsx、csv文件，以list输出表单中的所有row
>
> 只支持包含一个sheet的表单

- file_char方法
  - 判断输入的文件的encoding
  - 若encoding值为None，建议将文件转换为csv文件
  - 输出文件的encoding值
- file_or_dir方法
  - 判断输入的path是文件还是目录
  - 若是目录，输出目录下包含的文件与目录的绝对路径
  - 若是文件，输出文件绝对路径
- results方法
  - 使用Python open()方法，以‘rb’方式打开文件，对文件内容进行处理
  - 调用file_char()方法，对数据进行相应的decode()处理
  - 删除‘\r\n’，将'\t'替换为‘,’
  - 基于第二条，不建议表格中包含','字符，以免给后续数据分割带来麻烦
  - 以list存储表单中的值
  - 输出list
- 若处理某目录下的所有文件，先调用file_or_dir()方法，得到目录下所有文件，再循环调用results方法
- 。。。