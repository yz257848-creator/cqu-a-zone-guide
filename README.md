# 重大 A 区新生避坑 &amp; 精力守护助手

> 一个 WorkBuddy Skill：把"重庆大学 A 区这四年怎么过得不狼狈"这件事，打包成一个能装进 AI 助手的能力。

[![下载 Skill](https://img.shields.io/badge/⬇_下载_Skill-zip-8c2f39?style=for-the-badge)](https://github.com/yz257848-creator/cqu-a-zone-guide/raw/main/cqu-a-zone-guide.zip)
[![License](https://img.shields.io/badge/license-MIT-2f6b4f?style=for-the-badge)](./LICENSE)
[![Files](https://img.shields.io/badge/6_files-18_KB-5c6672?style=for-the-badge)](#包里有什么)

---

## 这是什么

面向**重庆大学 A 区（沙坪坝老校区）大一新生**的问答技能。装进 WorkBuddy 后，助手会按一套固定的"学长学姐"逻辑回答，而不是给你一篇百科式的校园介绍。

它能回答三类问题：

| 类型 | 举例 | 依赖 |
|---|---|---|
| **校内点位与办事流程** | 哪个食堂几点人少、校园卡丢了怎么办、期末找插座多的自习室、报修找谁、开在读证明要带什么 | 离线知识库 |
| **学业资料检索** | 能转专业吗要什么条件、高数往年期末题、SRTP 怎么立项、选课细则 | 联网访问 cqu-openlib.cn |
| **作息与精力** | 天天三点睡脑子很糊、躺两小时睡不着、午睡越睡越困 | 离线话术库 |

每个地点类回答都会**额外带一句避坑提醒**——比如问食堂，除了告诉你几点去，还会说"12:00 整别去最热门那一层，换楼比排队快"。这是这个技能的核心特色。

## 安装（三步）

1. 点上面的 **下载 Skill** 按钮拿到 `cqu-a-zone-guide.zip`，**不用解压**
2. 打开 WorkBuddy → 左侧「技能 / Skills」→「导入技能」，选中这个 zip
3. 装好后回到对话，直接问就行

<details>
<summary>手动安装 / 导入失败时的办法</summary>

解压 zip 得到 `cqu-a-zone-guide/` 文件夹，整个复制到：

- **用户级**（所有项目可用）：`~/.workbuddy/skills/`
- **项目级**（仅当前仓库可用）：`<项目根>/.workbuddy/skills/`

Windows 下 `~` 即 `C:\Users\<用户名>`。也可用命令行：

```bash
git clone https://github.com/yz257848-creator/cqu-a-zone-guide.git /tmp/cqu
cp -r /tmp/cqu/SKILL.md /tmp/cqu/references ~/.workbuddy/skills/cqu-a-zone-guide/
```

</details>

## 装好后这样问

```
A 区哪个食堂人少点，几点去不排队？
校园卡丢了怎么办
期末想找个插座多的自习室
能转专业吗，要什么条件
帮忙查一下高数往年期末题
最近天天三点睡，脑子很糊
```

## 包里有什么

```
cqu-a-zone-guide/
├── SKILL.md                  # 角色、问题路由、三条工作流、输出风格、边界、自检清单
├── INSTALL.md                # 离线版安装说明
├── LICENSE
└── references/
    ├── campus.md             # A 区点位与办事流程，14 个专题
    ├── pitfalls.md           # 11 类高频踩坑清单
    ├── wellness.md           # 作息模板、睡眠原理、话术库、就医升级条件
    └── openlib.md            # CQU-openlib 检索细则
```

**纯 Markdown，没有脚本、没有依赖、没有隐私数据。** 任何平台都能装。

### campus.md 覆盖的 14 个专题

校区方位 · 食堂 · 教学楼与自习 · 图书馆 · 快递驿站 · 校医院 · 开水房澡堂洗衣 · 校园卡 · 宿舍报修 · 网费网络 · 证明与盖章 · 校车与校内交通 · 打印复印 · 通用办事原则

### pitfalls.md 覆盖的 11 类场景

开学第一周 · 选课 · 自习 · 食堂 · 快递 · 办事 · 社团 · 转专业 · 竞赛与 SRTP · 社交与生活 · 身体与作息

## 设计上的几个取舍

**不编造。** 电话、营业时间、房间号、老师姓名，知识库没有的就说"不太确定"，让你去看公示或问辅导员。宁可答得不全，也不给错信息。

**一次只答一件事。** 回答 3–8 行，列表最多 5 条。不长篇大论，不顺手发散到无关话题。

**避坑只说一句。** 连甩三条提醒会像说教，所以每个场景只取一条最贴切的。

**不是医生。** 涉及持续失眠、心悸、体重骤降等情况，明确建议去校医院或正规医院，不做任何自我诊断。

## 内容时效

校内时间、电话、房号会变。`campus.md` 记录的是**常见规律与办事路径，不是实时公告**，回答统一按"以现场公示 / 学校官方通知为准"表述。

发现某条过期了？直接改对应的 `.md` 文件即可生效，不用重新打包。欢迎提 Issue 或 PR 更正。

## 许可

MIT，可自由使用、修改、再分发。

## 更新日志

- **v1.0** — 首版。14 个校园专题、11 类踩坑清单、5 类作息诉求话术、CQU-openlib 检索工作流。
