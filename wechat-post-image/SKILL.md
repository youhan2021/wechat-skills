---
name: wechat-post-image
description: 微信公众号封面和配图生成——封面漫画生成、PIL叠加文字、配图生成、上传微信获取 media_id
triggers:
  - "生成公众号封面"
  - "生成公众号配图"
env:
  WECHAT_API_SCRIPT: ~/.hermes/skills/wechat-api-lite/scripts/wechat_api.py
  RESEARCH_DIR: ~/.hermes/research/
---

# 微信公众号封面和配图生成

## 重要前提

- **正文必须先通过相似度检查，才能生成封面**
- 正文未完成不做封面

## 封面生成

封面直接用 AI 生成的漫画插画，resize 到 900×383，不加任何文字叠加层。

### Step 1: 生成封面图（MiniMax 文生图）

```bash
python3 ~/.hermes/skills/ai-image-gen/scripts/gen_image.py \
  --prompt "Manga comic style, single large robot character center-left, holding a fortune stick, simple halftone background, clean composition, big bold character, no cluttered elements, 70% width illustration area, English text only, no Chinese characters" \
  --output ~/.hermes/research/imgs/cover_bg.png
```

**Prompt 要点：**
- 漫画风格：`manga comic style`
- **图画占65-70%宽度**
- 要素精简（只保留核心元素1-2个），画面要清晰
- **反复强调 "English text only / no Chinese characters / pure English labels"**
- 深色/低饱和背景（避免浅色背景对比度差）

### Step 2: 验证背景图（PIL 像素采样）

```python
from PIL import Image
img = Image.open("cover_bg.png").convert("RGB")
W, H = 900, 383
rgb = img.resize((W, H), Image.LANCZOS).convert("RGB")

regions = {"左上":(50,50),"右上":(850,50),"中心":(450,191),"左下":(50,330),"右下":(850,330)}
for name,(x,y) in regions.items():
    print(f"  {name} ({x},{y}) = {rgb.getpixel((x,y))}")
# 全白=画面偏小，需要重生成
```

### Step 3: 直接 resize 成封面

```python
from PIL import Image

BG_IMAGE = "/home/ubuntu/.hermes/research/imgs/cover_bg.png"
W, H = 900, 383

canvas = Image.open(BG_IMAGE).convert("RGB").resize((W, H), Image.LANCZOS)
canvas.save("/home/ubuntu/.hermes/research/imgs/cover.png")
print("✅ cover.png saved (无文字叠加)")
```

---

## 配图生成

### 何时加配图

- 配图是**可选的**，不是每篇必须
- 判断标准：这个段落已经有足够的"瞬间"描写了吗？如果有，不加图也行
- 如果加图，每篇不超过 3 张

### 配图风格

- 统一风格：漫画/Comic Style（manga）
- prompt：`manga comic style`，用 black ink lines、halftone shading 等元素描述
- **fig2 不用 halftone dots / speed lines**（会让画面变脏变乱）
- 颜色：高饱和抓眼但不刺眼

### 配图规划

每张配图服务于一个情绪节点：

| 文章块 | 情绪 | 画面感 |
|---|---|---|
| 第一块 | 自信 → 被打断 | 做了什么，但没人问 |
| 第二块 | 准备充分 → 被击穿 | 想解释，但说不出口 |
| 第三块 | 无人承担 | 没有人站出来 |

---

## 上传微信

所有图片生成完成后，逐张上传：

```bash
# 封面
COVER_MEDIA_ID=$(python3 ~/.hermes/skills/wechat-api-lite/scripts/wechat_api.py \
  upload-image ~/.hermes/research/imgs/cover.png 2>&1 | \
  python3 -c "import sys,json; print(json.load(sys.stdin)['media_id'])")
echo "封面 media_id: $COVER_MEDIA_ID"

# 配图1
FIG1_MEDIA_ID=$(python3 ~/.hermes/skills/wechat-api-lite/scripts/wechat_api.py \
  upload-image ~/.hermes/research/imgs/fig1.png 2>&1 | \
  python3 -c "import sys,json; print(json.load(sys.stdin)['media_id'])")

# 配图2
FIG2_MEDIA_ID=$(python3 ~/.hermes/skills/wechat-api-lite/scripts/wechat_api.py \
  upload-image ~/.hermes/research/imgs/fig2.png 2>&1 | \
  python3 -c "import sys,json; print(json.load(sys.stdin)['media_id'])")
```

---

## 交付

完成后告知用户：
- 封面 media_id：`xxx`
- 配图1/2/3 media_id：`xxx`
- 下一步：加载 `wechat-formatter` 做 HTML 排版
