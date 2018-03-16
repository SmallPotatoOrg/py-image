python 用到的文档
---

> [建立虚拟环境](https://docs.python.org/3/tutorial/venv.html)

# 安装非全局的依赖

1. 建立虚拟环境

```sh
python3 -m venv XXX
# run
source XXX/bin/activate
```

2. pip 管理包

```sh
# 查询本地包
pip search astronomy
# 安装包
pip install XXX
# 安装特定版本
pip install XXX==0.0.1
# 更新包
pip install --upgrade XXX
# 卸载包
pip uninstall
# 查看包的信息
pip show XXX
# 查看包的列表
pip list
# 生成包的列表
pip freeze > XXX.txt
# 更具生成的列表文件，安装所需的包
pip install -r XXX.txt
```