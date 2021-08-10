# TDMS-Conver

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

- [背景](#背景)
- [安装](#安装)
- [示例](#示例)
- [更多](更多 )
- [维护者](#维护者)
- [如何贡献](#如何贡献)
- [使用许可](#使用许可)

## 背景

在使用NI的相关传感器采集数据时,一般的保存格式为`.tdms`,然而这种格式可能不方便用Python直接处理和阅读, 故推出了**TDMS-Conver**来将`.tdms`格式文件转换为`.xlsx`格式的Excel文件便于读写。

## 安装

这个项目基于Python3。请确保你本地安装的Python版本大于3。

```sh
$ pip install TDMS-Conver
$ # pip3 install TDMS-Conver # 如果使用的是pip3
```

## 示例

**TDMS-Conver**可以实现**单个文件**的转换和**文件夹**的转换。

```bash
# 文件夹
tdms-conver ./data-dir
# 文件
tdms-conver ./data-dir/data.tdms
# 指定保存目录
tdms-conver ./data-dir -s ./output 
```

## 更多


## 维护者

[@Littleor](https://github.com/Littleor)。

## 如何贡献

非常欢迎你的加入！[提一个 Issue](https://github.com/Littleor/TDMS-Conver/issues/new) 或者提交一个 Pull Request。


标准 Readme 遵循 [Contributor Covenant](http://contributor-covenant.org/version/1/3/0/) 行为规范。


## 使用许可

[MIT](LICENSE) © Littleor
