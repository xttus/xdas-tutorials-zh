# 收录来源与检查状态

这些是已保存的中文版本，不宣称是个人电脑上的最新修改。文件名统一，版本通过 Git 历史和本清单追溯。

| 仓库文件 | 整理前文件 | 本次执行 |
| --- | --- | --- |
| [01_open_and_consolidate_zh.ipynb](01_open_and_consolidate_zh.ipynb) | `01_打开与整合DAS数据_中文版_v5.ipynb` | 未重新执行；代码和原输出保留 |
| [02_exploration_processing_zh.ipynb](02_exploration_processing_zh.ipynb) | `02_探索与处理DAS数据_中文版_v12.ipynb` | 未重新执行；代码和原输出保留 |
| [03_massive_atomic_processing_zh.ipynb](03_massive_atomic_processing_zh.ipynb) | `03_Atom流水线与DAS分块处理_中文版_v12.ipynb` | 未重新执行；代码和原输出保留 |
| [04_coordinates_zh.ipynb](04_coordinates_zh.ipynb) | `04_坐标检查与光纤地理位置_中文版_v2.ipynb` | 未重新执行；代码和原输出保留 |
| [05_stations_zh.ipynb](05_stations_zh.ipynb) | `05_地震台站与震相拾取_中文版_v1.ipynb` | 未重新执行；代码和原输出保留 |
| [06_gamma_catalog_zh.ipynb](06_gamma_catalog_zh.ipynb) | `06_GaMMA到时关联与地震定位_中文版_v4.ipynb` | 未重新执行；代码和原输出保留 |
| [07_streaming_zh.ipynb](07_streaming_zh.ipynb) | `07_DAS_Streaming_Chinese_v3.ipynb` | 未重新执行；代码和原输出保留 |

机器可读的原文件与整理后 SHA-256 见 [source-manifest.json](source-manifest.json)。哈希用于追踪来源，不表示运行或科学结果正确。

## 环境支持文件

上游修订：`c579ae3f8425b16da8ed7897d19042d63eef263b`。`install.py`、`pyproject.toml`、`uv.lock`、`.python-version` 按此修订附带，未在本次完成安装与逐篇兼容验证。上游依赖快照与历史中文 Notebook 并非同一来源修订，勿表述为已锁定复现环境。

## 已知待验证项

- 目标系统的依赖安装、外部数据服务、模型权重获取。
- 从干净内核完整顺序运行及原示例输出对照。
- 教程 7 线程、目录通知、标记协议与停止行为。
- 公式、标题和图片在 GitHub、Jupyter 中的实际渲染效果。
- 用户本地可能存在的后续修订。
