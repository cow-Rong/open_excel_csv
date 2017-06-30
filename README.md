# open_excel_csv
##### 这是一个读取Excel/csv文件的Python类

> 可读取xls、xlsx、csv文件

- fileChar属性
  - 判断输入的文件的encoding
  - 若encoding值为None，建议将文件转换为csv文件
- fileOrdir属性
  - 判断输入的path是文件还是目录
  - 若是目录，输出目录下包含的文件与目录的绝对路径
  - 若是文件，输出文件绝对路径
- results属性
  - 使用Python open()函数，以‘rb’方式打开文件，对文件内容进行处理
  - 删除‘\r\n’，将'\t'替换为‘,’
  - 基于第二条，不建议文档中包含','字符，以免给后续数据分割带来麻烦
- 。。。