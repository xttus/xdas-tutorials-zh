# 上传 GitHub 前的检查

本包是仓库文件，不代表已替你创建远程仓库。

## 发布前

- 阅读 `PROVENANCE.md`，保留上游署名、许可和来源；勿改为与上游不一致的简单宽松许可。
- 七篇教程逐篇在目标环境中检查，记录实际复现状态。尤其核对教程 7 的流处理、等待、线程和结束行为。
- 确认未包含原始数据、缓存、环境、模型权重、账号、个人路径或未获许可的图片。
- 从仓库根目录运行 `python scripts/validate_repository.py`。它只检查静态结构，不运行科学计算。

## 建仓与首次提交

在 GitHub 创建你自己的仓库，名称可使用 `das-learning-zh`，自行选择公开或私有。若按下面新建本地 Git 的方法上传，远程仓库应为空，避免初始化内容冲突。

在解压后的仓库根目录用 Git Bash 执行：

```bash
git init
git branch -M main
git add README.md LICENSE.md PROVENANCE.md CONTRIBUTING.md CHANGELOG.md .gitignore .github guides topics datasets tutorials templates scripts
git status --short
git diff --cached --stat
```

确认暂存内容正确后再执行：

```bash
git commit -m "Add Chinese DAS learning guides and Xdas tutorials"
```

最后按 GitHub 空仓库页面给出的命令添加 `origin` 并推送 `main`。不要直接复制他人的仓库地址；本说明不预填用户身份或远程地址。若已有 Git 历史，先检查现状，不重复初始化或强制推送。
