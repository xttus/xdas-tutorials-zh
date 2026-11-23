# Xdas 中文教程索引

**运行根目录就是本目录。**首次运行先看[安装指南](../../guides/setup.md)。已有可用上游环境的读者，可以把本目录的中文 Notebook 复制到已有项目根目录运行，不需要复制整套数据。

这些是从已保存中文版本整理的学习材料，不保证与你个人电脑上最近编辑的一份相同。来源见 [SOURCES](SOURCES.md)，本次未重新执行真实数据。

| 顺序 | 内容 | 主要前置输入 | 主要成果 |
| --- | --- | --- | --- |
| [1](01_open_and_consolidate_zh.ipynb) | 打开与整合 | `data/gps_multicable/`，必要时几何 CSV | `outputs/singlecable.nc` 等虚拟组织结果 |
| [2](02_exploration_processing_zh.ipynb) | 探索与处理 | 教程 1 的单光纤文件 | 处理读图；保存 `outputs/event.nc` |
| [3](03_massive_atomic_processing_zh.ipynb) | Atom 与分块 | 教程 1、2 的输出 | 分块对照与 DAS 到时 `outputs/picks.csv` |
| [4](04_coordinates_zh.ipynb) | 坐标与几何 | 教程 1 输出、NTP 样本、路线 CSV | 时间与几何理解，不等于自动永久修复所有原文件 |
| [5](05_stations_zh.ipynb) | 台站三分量与拾取 | `data/stations/` | `outputs/station_picks.csv` |
| [6](06_gamma_catalog_zh.ipynb) | GaMMA 关联定位 | DAS／台站拾取、StationXML、几何与速度模型 | `outputs/catalog.csv` 与定位检查 |
| [7](07_streaming_zh.ipynb) | 模拟实时处理 | 教程 2 的事件文件；匹配的流处理 API | 回放、流结果与在线拾取，不是新一轮定位 |

## 两个易混点

**处理链与模型链不一定相同。**教程中高通后取绝对值常用于振幅展示；模型输入以实际检测代码和模型约定为准。

**准备环境不等于所有数据都准备好了。**主 DAS 压缩包、几何、台站和速度模型是不同资源，缺哪部分就追溯哪部分，不要全量重下。

## 执行提醒

每篇从前往后运行。教程 7 的 `prepare_output_directory` 在前部辅助单元格定义，必须先执行该格；与之配套的数据源和 `.ready` 协议不能只复制一部分。0B 不是“成功完成”，需要检查包是否收到。

版本管理采用固定文件名加 Git 历史；不要在同一公开目录并列多个 `v1`、`v2` 让读者猜哪个入口有效。
