# [c672: RGB ⇆ HEX](https://zerojudge.tw/ShowProblem?problemid=c672)

寫一個顏色格式轉換的程式，輸入的格式有兩種

* `r g b`：`r`、`g` 及 `b` 為十進位數值
* `#RRGGBB`：`RR`、`GG` 及 `BB` 為兩位數的十六進位數值

`RR` 為 `r` 的十六進位值；`GG` 為 `g` 的十六進位值；`BB` 為 `b` 的十六進位值

當輸入的格式為 `r g b` 時，輸出的格式為 `#RRGGBB`；當輸入的格式為 `#RRGGBB` 時，輸出的格式為 `r g b`

## 輸入範例

```
#FFFFFF
255 0 0
```

## 輸出範例

```
255 255 255
#FF0000
```
