# image-prompt-reverse · 图片反推提示词生成器

> 上传一张图片，自动识别图片类型，按 **「0-任务目标 + 5S + 约束条件」** 结构生成可直接喂给 GPT image 2.5 的完整中文提示词，并把每条结果**独立保存为 txt**。

一个 WorkBuddy / CodeBuddy 通用 Skill。

---

## ✨ 特性

- 🖼️ **上传即用**：只需要一张图片，无需任何额外输入
- 🏷️ **自动识别类型**：人像 / 电商产品 / 海报平面 / 风景建筑 / 插画动漫 / 美食 / UI / Logo / 宠物 / 其他
- 🧩 **结构化输出**：0-任务目标 + 5S（Subject / Style / Shot / Setting / Scene lighting）+ 6-约束条件
- 🇨🇳 **完整中文提示词**：可直接投喂 GPT image 2.5，高度还原参考图
- 📄 **独立保存**：每次反推生成一个新 txt，绝不覆盖、绝不堆砌
- 🔒 **纯本地运行**：无网络请求、无凭据读取、无破坏性操作

## 📁 目录结构

```
image-prompt-reverse/
├── SKILL.md                        # 技能主流程
├── references/
│   ├── prompt-template.md          # 反推提示词模板（0-任务目标 + 5S + 约束条件）
│   └── image-type-taxonomy.md      # 图片类型识别维度 + 各类型关注重点
├── scripts/
│   └── save_prompt.py              # 唯一文件名 + UTF-8 保存 txt
├── examples/
│   ├── sample_landscape.png        # 示例输入图
│   └── sample_output_landscape.txt # 示例输出提示词
├── LICENSE
└── README.md
```

## 🚀 安装

将整个 `image-prompt-reverse/` 目录放入技能目录：

| 范围 | 路径 |
|---|---|
| 用户级（所有项目可用） | `~/.workbuddy-ai/skills/image-prompt-reverse/` |
| 项目级（仅当前项目） | `<项目根>/.workbuddy-ai/skills/image-prompt-reverse/` |

Windows 用户级路径示例：`C:\Users\<你的用户名>\.workbuddy-ai\skills\image-prompt-reverse\`

也可以直接解压 Releases 中的 `image-prompt-reverse.zip` 到上述目录。放入后重启一次会话即可加载。

## 🎯 使用

1. 上传一张图片
2. 说「**反推提示词**」/「**复刻这张图**」/「**帮我写提示词**」
3. 得到：图片类型判定 + 保存路径 + 提示词全文

**输出目录**：当前工作区下的 `outputs/`
**文件命名**：`YYYYMMDD_HHMMSS_<图片类型>_<序号>.txt`（UTF-8，时间戳保证唯一）

## 🧱 提示词结构

| 编号 | 字段 | 说明 |
|---|---|---|
| 0 | 任务目标 | 这张图拿来做什么？视觉重点是什么？ |
| 1 | Subject 主体/核心视觉元素 | 主体外形/细节/服饰/妆造/道具/神情/姿态/站位/眼神；多主体空间关系；文案内容 |
| 2 | Style 风格 | 整体风格、主导审美、色彩语言、质感特征、是否风格融合 |
| 3 | Shot 镜头与构图 | 景别、机位角度、透视、构图、摄影参数、主体占比、虚化、视觉重心、留白、前中后景虚实 |
| 4 | Setting 场景元素与环境 | 地点、时间、天气、空间结构、前中后景元素、支撑/可省略/不可少元素、招牌标语文字 |
| 5 | Scene lighting 场景光照与影调 | 光源、方向、色温冷暖、明暗关系、轮廓光/补光/氛围光、阴影强弱与过渡 |
| 6 | 约束条件 | 必须保留什么？不要出现什么？冲突时什么优先？ |

## 🖼️ 示例

输入图（`examples/sample_landscape.png`）：一张风格化日落风景。

输出（`examples/sample_output_landscape.txt`）：

```
【反推提示词 | 图片类型：风景（风格化日落湖景 · 扁平渐变插画风）】

0-任务目标：用于生成一张风格化日落自然风景配图，可作为壁纸 / 背景 / 氛围图使用。视觉重点为：右侧偏上的发光落日、由深蓝到橙黄的渐变天空，以及由远山与暗色前景水面构成的三段式水平构图。

1-Subject主体/核心视觉元素：无人物主体。核心视觉元素为「落日」——位于画面右侧约 68% 水平位置、地平线略上方，正圆形，暖白偏黄（#FFF3C4 过渡到 #F7B733），外圈带一层大范围柔光晕……

2-Style风格：现代扁平化 / 极简插画风（flat illustration，接近矢量质感）……

3-Shot镜头与构图：超广角 / 全景视角，平视地平线。三段式水平构图……

4-Setting场景元素与环境：场景为开阔的湖面 / 水面日落。时间处于黄昏（golden hour 后段）……

5-Scene lighting场景光照与影调：单一主光源为落日（自发光，暖色，色温约 2700–3200K）……

6-约束条件：必须保留——右侧发光落日及其柔光晕……；不要出现——人物、建筑、文字、云朵、飞鸟、噪点或写实照片质感……
```

## 🛠️ 脚本用法

`scripts/save_prompt.py` 可独立使用：

```bash
# 从内容文件读取
python scripts/save_prompt.py --type "人像" --content-file prompt.txt --outdir ./outputs

# 从标准输入读取
echo "提示词内容" | python scripts/save_prompt.py --type "产品" --outdir ./outputs

# 直接传内容
python scripts/save_prompt.py --type "风景" --content "0-任务目标：..." --outdir ./outputs
```

运行后会在 stdout 打印保存文件的绝对路径。

## 📌 自定义

- **改输出结构**：编辑 `references/prompt-template.md`
- **改类型识别范围**：编辑 `references/image-type-taxonomy.md`
- **改默认输出目录**：`scripts/save_prompt.py` 中的 `DEFAULT_OUTDIR`，或运行时用 `--outdir` 指定

## 📄 License

[MIT](LICENSE)
