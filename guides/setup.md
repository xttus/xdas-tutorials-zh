# 安装与运行

## 已有可用环境的读者

先保留原项目与环境，不要为了换中文文件重新下载几 GB 数据。可以把这里七篇 `_zh.ipynb` 复制到已有教程项目根目录，与 `data/`、`outputs/`、`pyproject.toml` 同级，再使用原项目的解释器运行。

不要同时打开同名旧版误以为修改没有生效；仓库内文件名固定，版本信息写在文档和 Git 历史中。

## 首次安装

本仓库将 Notebook 与环境文件放在 `tutorials/xdas/`；这是本系列的**运行根目录**。不要求任何特定盘符。环境支持文件的上游修订与验证状态见 [SOURCES](../tutorials/xdas/SOURCES.md)。依赖未在本次重新安装，不能把静态检查当作安装成功保证。

先确认已安装 Git 和 [uv](https://docs.astral.sh/uv/)。以下命令假定已解压仓库并进入 `das-learning-zh/`。

### Git Bash

```bash
cd tutorials/xdas
# 可选：把 uv 缓存放在当前项目所在磁盘；只影响此终端及其子进程。
export UV_CACHE_DIR="$PWD/.local-cache/uv"
uv sync --frozen
uv run install.py
uv run jupyter lab
```

### PowerShell

```powershell
Set-Location .\tutorials\xdas
# 可选，与上面作用相同。
$env:UV_CACHE_DIR = Join-Path (Get-Location).Path '.local-cache\uv'
uv sync --frozen
uv run install.py
uv run jupyter lab
```

下载量较大，先看上游 `install.py` 和数据说明再运行；它包含多个外部资源准备步骤，网络或服务不可用时可能部分成功。不要使用 `--force` 作为常规重试方法。Jupyter 应选择该项目 `.venv` 的解释器。

只设置 `UV_CACHE_DIR` 不会自动迁移系统临时目录、模型缓存、conda 环境或其他软件文件，也不能保证系统盘不再增长。修改缓存位置不会迁移已经存在的缓存。

## 检查内核和工作目录

先运行一个 Notebook 代码单元格：

```python
import sys
from pathlib import Path
print('解释器：', sys.executable)
print('工作目录：', Path.cwd())
print('数据目录存在：', Path('data').is_dir())
import xdas
print('Xdas：', getattr(xdas, '__version__', '未知'), xdas.__file__)
```

解释器应属于本次项目环境，工作目录应是包含 `data/` 与 `outputs/` 的运行根目录。终端是 Git Bash、PowerShell 还是命令提示符，不决定能否运行 `uv`；命令语法、环境变量和实际内核才是关键。

## 运行顺序

从教程 1 开始，逐格运行，观察结果再继续。重启内核会清除变量、函数、模型和线程状态，需要重新执行前置定义；屏幕上保留的旧输出不代表变量仍存在。

教程 7 涉及后台线程与网络端口。若上一次异常退出，先检查任务是否停止；必要时重启内核并按顺序运行，不要在等待中的单元格后继续排队运行所有单元格。
