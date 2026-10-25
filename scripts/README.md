# 打包产物与构建脚本

本目录用于维护 `cqu-a-zone-guide.zip` 这个发行包。**技能本体不在这里**——它在仓库根目录（`SKILL.md` + `references/`）。

## 目录说明

- `site/` — 分享用的下载落地页（静态 HTML，含一键复制链接）
- `repo/` — 推送仓库时用不上的临时内容
- `cqu-a-zone-guide/` — **打包时生成的技能副本，不要直接改**。要改内容请改仓库根目录的源文件。
- `cqu-a-zone-guide.zip` — 最终发行包

## 重新打包

修改完根目录的源文件后，在仓库根目录执行：

```bash
python scripts/build_zip.py
```

脚本会：

1. 校验 `SKILL.md` 的 frontmatter（`name` 必须为 hyphen-case，`description` 不能含尖括号）
2. 按 `cqu-a-zone-guide/` 前缀重建压缩包（**必须用正斜杠**，否则 macOS / Linux 解压会失败）
3. 做 CRC 校验并打印文件清单

## 注意

- 官方 `package_skill.py` 在 Windows 下会写出反斜杠路径（`cqu-a-zone-guide\SKILL.md`），跨平台解压会出问题，所以这里自己重打包。
- 发行包里的 `SKILL.md` **不要**带 `agent_created: true`——那是本地管理标记，分发出去会干扰对方的管理逻辑。
- 每次改完源文件要重新打包，否则下载到的 zip 还是旧内容。
