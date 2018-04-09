# [Assembler interpreter (part II)](http://www.codewars.com/kata/assembler-interpreter-part-ii/)

## 目標

設計一個組合語言直譯器。

以下符號名稱會有三種敘述方式，暫存器 `x`、常數 `x` 以及 `x` (兩者皆可)。

|指令               |功能|
|-------------------|-|
|`label:`           |定義標籤，可使用跳躍指令或 `call` 跳躍至指定標籤|
|`; comment`        |註解|
|`mov x, y`         |將暫存器 `x` 的值設為 `y`|
|`inc x`            |將暫存器 `x` 的值加一|
|`dec x`            |將暫存器 `x` 的值減一|
|`add x, y`         |將 `y` 加到暫存器 `x`|
|`sub x, y`         |將 `y` 減到暫存器 `x`|
|`mul x, y`         |將 `y` 乘到暫存器 `x`|
|`div x, y`         |將 `y` 除到暫存器 `x` (整數除法)|
|`cmp x, y`         |比較 `x` 跟 `y` ，其結果用在條件跳躍指令上(`jne`、`je`、`jge`、`jg`、`jle` 及 `jl`)|
|`jmp label`        |跳躍至指定標籤的位置|
|`jne label`        |當 `cmp` 的結果為 `x` 不等於 `y` 時跳躍|
|`je label`         |當 `cmp` 的結果為 `x` 等於 `y` 時跳躍|
|`jge label`        |當 `cmp` 的結果為 `x` 大於等於 `y` 時跳躍|
|`jg label`         |當 `cmp` 的結果為 `x` 大於 `y` 時跳躍|
|`jle label`        |當 `cmp` 的結果為 `x` 小於等於 `y` 時跳躍|
|`jl label`         |當 `cmp` 的結果為 `x` 小於 `y` 時跳躍|
|`call label`       |跳躍至指定標籤的位置，當分支執行到 `ret` 時，需跳躍回這一行的下個位址|
|`ret`              |跳躍回前一個 `call` 的位址|
|`msg 'msg', b, ...`|輸出訊息，後方參數可為常數字串、常數整數或暫存器值，參數數量不等|
|`end`              |程式結束，將輸出的值回傳，若沒有任何輸出時，回傳整數 `-1`|
