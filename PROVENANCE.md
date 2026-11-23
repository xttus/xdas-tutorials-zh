# 来源、许可与验证边界

## 上游与中文整理

基础教程与代码来自 [xdas-dev/tutorials](https://github.com/xdas-dev/tutorials)。本项目是独立中文学习整理，不是官方翻译，不代表原作者背书。原作者及项目贡献者的权利与署名保留，根目录 `LICENSE.md` 是上游 GPL 第 3 版全文。

翻译、解释和代码适配形成的学习版沿用上游 GPL-3.0 许可；不可因中文整理而去掉上游许可。其他软件、模型权重、数据与外部图件遵循各自条款，本项目的许可不会替代它们。

中文学习过程：稚方Xttus负责运行实践、提出问题、尝试读图与反馈；ChatGPT（Codex）协助翻译、代码解释、资料核对与组织。补充说明不自动等同于原作者意图，需要区分明确来源与教学推断。

## 本次收录与改动

七篇来自已经保存的中文版本，具体文件名见 [来源清单](tutorials/xdas/SOURCES.md)。它们不被宣称为用户本地最新修改副本，也未在本次重新执行。

本次仅统一文件名，新增仓库级阅读提示，将教程 1、2 说明中的个人盘符改为运行根目录或相对路径。不修改既有代码单元格、输出或图片附件。第七篇已保存版本本身包含目录备份函数与跨平台回放辅助实现；如果本地缺少定义，先核对文件版本与执行顺序。

`tutorials/xdas/` 中的 `install.py`、`pyproject.toml`、`uv.lock`、`.python-version` 及许可证取自上游修订 `c579ae3f8425b16da8ed7897d19042d63eef263b`。这是本次准备的上游环境快照，不是对这些历史中文版本逐篇验证过的环境声明。公开前应在目标系统运行并记录兼容性；保留自己的已验证环境，不要无条件升级。

## 检查范围

本次检查 JSON 与 Notebook 结构、Python 语法、图像附件引用、文档本地链接及代码单元格与收录前一致性。静态检查无法证明数据可下载、模型正确、依赖可安装、图形显示美观或实时线程安全。

公开状态应区分：已整理、静态检查通过、指定环境运行通过、科学结果验证通过。不要用一个“完成”代替这些不同层次。

## 引用与事实依据

- [Xdas 教程及贡献者](https://github.com/xdas-dev/tutorials)
- [Xdas 官方文档](https://xdas.readthedocs.io/)
- [Xdas 处理单元](https://xdas.readthedocs.io/en/latest/user-guide/pipeline/atoms.html)
- [超出内存的数据处理](https://xdas.readthedocs.io/en/latest/user-guide/pipeline/processing.html)
- [Xdas Toy DAS Datasets](https://doi.org/10.5281/zenodo.11212055)
- [PhaseNet 原始论文](https://doi.org/10.1093/gji/ggy423)
- [SeisBench 项目](https://github.com/seisbench/seisbench)
- [GaMMA 项目](https://github.com/AI4EPS/GaMMA)
- [SciPy 抗混叠降采样说明](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.decimate.html)

API 示例应核对实际版本。没有独立真值时，不以示例输出宣称检测准确率、定位精度或科研创新。
