<!--
 * @Date: 2022-03-30 14:49:13
 * @LastEditTime: 2022-03-30 17:07:20
 * @LastEditors: diklios
 * @Description:
 * @License: MIT
 * @Author: diklios
 * @Contact Email: diklios5768@gmail.com
 * @Github: https://github.com/diklios5768
 * @Blog:
 * @Motto: All our science, measured against reality, is primitive and childlike - and yet it is the most precious thing we have.
-->

# 使用说明

- json 文件中的格式：`变体字:常用字`
- 这种格式用于进行修正，如从 PDF 文件复制出来会有很多这种错误
- 如果需要进行混淆，需要读取文件内容到字典中之后进行反转
  - 但是如果使用总和的 json 文件，一个常用文字会有多个变体字，要注意，在字典中这是不允许的
  - 建议增加一些处理，如改为`常用字:[变体字]`，即使用数组的这种形式
- 象形文字博大精深，暂时也只是收录了一部分，如果遇到没有的字，需要自行参考给出的资料查找

## 总和表

- 以下对照表的总和
  - [总和表](all.json)
- 一般来说，使用两个部首对照表已经足够了

## 常见部首对照表

- 不属于康熙部首的一些常见部首
- [对照表](radicals.json)

## 康熙部首对照表

- 增加了`{"戸": "⼾","户": "⼾"}`两个字的对照，所以是 216 个，而不是规定的 214 个
- 第一个是康熙部首，第二个是日常用的基本汉字
- [对照表](kang-xi-radicals.json)

## 杭州数字

- [对照表](hangzhou-num.json)

## 日本片假名(片仮名 カタカナ katakana)

- 平假名完全和汉字不一样，所以没有对照表
- [对照表](katakana.json)

## 汉语注音符号（Chinese zhuyin）

- 即汉语拼音
- [对照表](bopomofo.json)

## 汉文（宽文）

- [对照表](kanbun.json)

## 笔画文字

- [对照表](strokes.json)

## 被括号包裹的汉字

- [对照表](parenthesized.json)

## 被圆包裹的汉字

- [对照表](circle.json)

## 被方块包裹的汉字

- [对照表](square.json)

## 被括弧包裹的汉字

- 和括号不大一样
- [对照表](bracketed.json)
