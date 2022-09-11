# 我制作的小游戏之一

中文名: 接住豆子
English name: Catch The Beans
使用 vs2022, .Net Core 6 构建
如果无法打开, 请下载 [.Net Core 6 运行时](https://dotnet.microsoft.com/zh-cn/download/dotnet/6.0/runtime)

玩法: 按 <kbd>A</kbd> 将平台向左移, <kbd>D</kbd> 将平台向右移
按上述键的同时按 <kbd>Shift</kbd>, 则移动速度加快

## 以下内容的数字皆可在 ./source/Config.cs 内修改

接住豆子得 5 分, 接不住扣 10 分
难度控制豆子移速
简单难度: 每 14 帧 \(约 0.25 秒移动一格\)
普通难度: 每 10 帧 \(约 0.16 秒移动一格\)
困难难度: 每 6 帧 \(约 0.1 秒移动一格\)
