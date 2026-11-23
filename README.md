# DAS 中文学习指南

从读懂一段光纤记录，到解释处理、检测与定位结果。

本项目从 Xdas 七篇教程的中文学习版出发，整理学习路线、数据管理、信号处理、模型推断和大规模执行方法。它不是 Xdas 官方中文文档，也不是一套已经验证适用于所有 DAS 场景的算法。

**初稿日期：2026-11-23。七篇 Notebook 已收录已保存版本；本次进行了静态检查，未重新执行真实数据、模型或网络下载。原有输出仅作示例，不代表本次运行结果。**

## 从这里开始

1. 阅读[学习路线](guides/learning-path.md)，理解七篇教程的关系。
2. 阅读[处理、检测与验证总导读](guides/workflow.md)，先知道为什么做。
3. 按[安装与运行指南](guides/setup.md)准备环境和数据。
4. 打开[教程索引](tutorials/xdas/README.md)，从教程 1 顺序运行。
5. 遇到问题先查[常见问题](guides/troubleshooting.md)，不要反复重跑所有下载。
6. 准备公开时阅读[GitHub 发布步骤](guides/github-publishing.md)，先检查再推送。

## 按问题查找

| 我想知道 | 阅读入口 |
| --- | --- |
| 文件、时间、通道、经纬度怎样对应？ | 教程 1、4；[术语表](topics/glossary.md) |
| 为什么滤波、重采样，图上有什么变化？ | 教程 2；[信号处理决策](topics/signal-processing.md) |
| PhaseNet、到时拾取和 GaMMA 是什么关系？ | 教程 3、5、6；[检测与事件解释](topics/detection.md) |
| 几百 GB 或持续到来的数据怎么办？ | 教程 3、7；[大型 DAS 数据指南](guides/large-data.md) |
| 怎样读图，怎样防止只看到了漂亮结果？ | [可视化与验证](topics/visualization.md) |
| 数据从哪里来？如何安置？ | [数据集目录](datasets/README.md)、[本地数据管理](guides/data-management.md) |

## 七篇教程

| 教程 | 学习主题 | Notebook |
| --- | --- | --- |
| 1 | 打开文件、整合多文件与保存虚拟数据集 | [打开与整合](tutorials/xdas/01_open_and_consolidate_zh.ipynb) |
| 2 | 探索、滤波、重采样、频率—波数分析 | [探索与处理](tutorials/xdas/02_exploration_processing_zh.ipynb) |
| 3 | Atom、处理链、分块执行与 DAS 震相拾取 | [分块处理](tutorials/xdas/03_massive_atomic_processing_zh.ipynb) |
| 4 | 时间坐标、采样声明、光纤几何与盘纤 | [坐标与几何](tutorials/xdas/04_coordinates_zh.ipynb) |
| 5 | 地震台站三分量波形与震相拾取 | [地震台站](tutorials/xdas/05_stations_zh.ipynb) |
| 6 | 到时关联、速度模型与事件定位 | [GaMMA 与事件目录](tutorials/xdas/06_gamma_catalog_zh.ipynb) |
| 7 | 回放、目录监听、网络流与在线拾取 | [流式处理](tutorials/xdas/07_streaming_zh.ipynb) |

## 项目边界与来源

- 基础教程：[xdas-dev/tutorials](https://github.com/xdas-dev/tutorials)。中文内容是翻译、学习解释及明确标注的兼容改动，不取代原作者工作。
- 示例数据：[Xdas Toy DAS Datasets](https://doi.org/10.5281/zenodo.11212055)。不随仓库分发原始数据。
- 中文学习版：稚方Xttus通过运行、提问、读图与反馈参与整理；ChatGPT（Codex）协助翻译、解释和文档组织。所有 AI 辅助内容仍需人工和实验核查。
- 这里的地震流程不是通用“事件分类器”。PhaseNet 拾取 P/S 候选到时，GaMMA 关联候选并估计事件参数；不等于已完成真实标签评测。

详细见[来源与许可说明](PROVENANCE.md)、[版本来源清单](tutorials/xdas/SOURCES.md)及[变更记录](CHANGELOG.md)。沿用上游 GPL-3.0 许可并附上[许可证全文](LICENSE.md)；第三方数据、模型与依赖仍遵循各自许可。

## 参与完善

请先阅读[贡献指南](CONTRIBUTING.md)和[汉化与教学规范](guides/translation-standard.md)。本阶段优先修正解释、路径、版本兼容和运行问题，不急于扩展网站或收集大量未经整理的链接。
