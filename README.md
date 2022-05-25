# Tools

## 汉字对照表

- **可用于修正从 PDF 中复制的看上去很像但是不正常的汉字**

- [中日韩(越)表意(象形)文字(CJK(V) Ideographs)](./CJKVI-variants/README.md)

- 参考
  - [CJKV (Chinese Japanese Korean Vietnamese) Ideograph Database](https://github.com/cjkvi)
    - <https://github.com/cjkvi/cjkvi-variants/blob/master/non-cjk.txt>
    - <https://github.com/cjkvi/cjkvi-dict>
  - [汉字 Unicode 编码范围](https://www.qqxiuzi.cn/zh/hanzi-unicode-bianma.php)
  - 百度百科
    - [中日韩越统一表意文字](https://baike.baidu.com/item/%E4%B8%AD%E6%97%A5%E9%9F%A9%E8%B6%8A%E7%BB%9F%E4%B8%80%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97/1301611?fr=aladdin)
  - 维基百科
    - [中日韩越统一表意文字](https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%97%A5%E9%9F%93%E7%B5%B1%E4%B8%80%E8%A1%A8%E6%84%8F%E6%96%87%E5%AD%97)
    - [未统一汉字列表](https://zh.wikipedia.org/wiki/%E6%9C%AA%E7%B5%B1%E4%B8%80%E6%BC%A2%E5%AD%97%E5%88%97%E8%A1%A8)

## 中国身份证号码处理对照表

- 用途：用于快速处理身份证号码

- 特色

  - 不构建程序，而是使用 JSON 格式的数据
  - 使用 2020 年国家统计局数据，但只到第三级
    - 使用[lyhmyd1211/AreaJson_CN](https://github.com/lyhmyd1211/AreaJson_CN/tree/2020)
      - 2021 年似乎无法使用，准备后续自己写一个
    - 如果使用完整名称需要拼接，也提供了简单的文件直接使用
      - 简化脚本已经提供

- 参考
  - [lyhmyd1211/AreaJson_CN](https://github.com/lyhmyd1211/AreaJson_CN/tree/2020)
    - 分的比较细，如果需要更精细的请使用这个库
    - 相对较全，但是无特别行政区，本库进行了一点补充
    - 且因为是分等级的，所以无法直接获得完整名称
  - [karinlee1988/FakeIDCardNumber](https://github.com/karinlee1988/FakeIDCardNumber)
    - 部分地区不够全，有一些缺漏
    - 可参考身份证组成方式
  - [navyxie/idcard](https://github.com/navyxie/idcard)
    - 长时间未更新
    - 可参考计算方法和接口设计
