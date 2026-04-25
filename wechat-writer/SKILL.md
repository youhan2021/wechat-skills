---
name: wechat-writer
description: 微信公众号正文写作——写作风格指导、正文生成、存档、相似度检查
triggers:
  - "写公众号正文"
  - "写微信公众号"
env:
  RESEARCH_DIR: ~/.hermes/research/
  ARTICLE_HISTORY_FILE: ~/.hermes/research/articles_history.json
---

# 微信公众号正文写作

## 核心定位

👉 **"有判断的聊天"，而不是"完整的文章"**

👉 **更高目标："让读者经历这个道理"，而不是"讲道理给他听"**

---

## 写作层级

### Level 1：信息层（已过）

讲知识、讲概念、讲结构——对你没价值。

### Level 2：总结层（你现在在这里）

有经验、有观点、有归纳。但问题：**抽象、平、缺画面**。

典型症状：满篇"本质是……""核心问题是……""其实是因为……"

### Level 3：体验层（你要到这里）

有场景、有冲突、有"瞬间"。读者不是"理解"，而是"感受到"。

---

## 升级路径

### 找"抽象句"→ 强制转成"具体"

以下句式是"总结层语言"，每句都要改：
```
"本质是……"
"核心问题是……"
"其实是因为……"
"这说明……"
"问题在于……"
```

**每句抽象 → 强制问自己3个问题：**
1. 有没有一个真实场景？
2. 有没有一个"人"的反应？
3. 有没有一个"意外/冲突"？

### 一个点 = 3层 × 3维（扩写网格）

| 时间三层（纵向） | 维度三层（横向） |
|---|---|
| 之前（预期） | 外部（场景/对话） |
| 当下（事件） | 内部（我内心） |
| 之后（反应） | 关系（他们关心什么） |

---

## 写作技巧（经验积累）

### 开头：逗号改句号，制造"停顿+重击"

如："它们看起来五花八门。/实际上都在补同一件事：/Agent根本不是一个完整系统。"

### 结尾：终极判断转发级金句

如："在那之前，它只是一个会说话的模型"

### 每层之间：加过桥句

如："但记住还不够...问题只是从'忘了'变成'说错了'"

### 五项升级（必须逐项检查）

- [ ] **升级一（环境维度）**：关键场景有一句环境/氛围描写
- [ ] **升级二（认知断裂）**：震惊/沉默之前有"想解释但解释不了"的中间层
- [ ] **升级三（不可反驳的观察）**：总结段用"我们…他们…"对比结构
- [ ] **升级四（结构性观察）**：总结前有"因为我们不承担后果"等（≤3条）
- [ ] **升级五（行为词结尾）**：金句结尾是具象行为，不是抽象词

### Level 2 → 3 升级检查

- [ ] 没有"本质是""核心问题是""其实是因为""我意识到""我注意到"
- [ ] 每个结论有过程（不是只有瞬间）
- [ ] 让读者自己得出结论

### 删减检查

- [ ] 每句有存在理由（加细节/过程/变化三选一）
- [ ] 字数砍30%

---

## 写作模板

### 1️⃣ 开头：预期 → 反差（3行）

```
很多人觉得，自动驾驶最难的是技术。
2019年在加州，我们团队100多人，博士占一半，
技术指标跑赢所有人。
三个月推不动一台车。
```

### 2️⃣ 中间：3个块，每块过五层

每一块写进正文前，必须完整思考这五层：

| 层次 | 思考内容 | 写进正文时 |
|---|---|---|
| 背景 | 时间/地点/人物 | 融进第一句 |
| 预期 | 我原本以为 | 融进叙述 |
| 现实 | 实际发生了什么 | 直接写对话/行为 |
| 反差 | 预期 vs 现实 | 融进叙述 |
| 反应 | 那一刻我…… | 直接写感受 |

❌ 错误（正文出现标记词）：
```
【背景】2019年11月，加州，第一次给车厂做演示。
【预期】我以为他们会问准确率。
```

✅ 正确（标记词全部消失）：
```
2019年11月，加州，第一次给车厂做演示。
我准备了三个月，把所有技术指标都跑通。
总工听完，站起来说——"如果出事，谁负责？"
```

### 3️⃣ 结尾：再反转 + 一句被记住的话

```
这不是技术问题。
这是责任结构的问题。

"技术团队最容易犯的错，不是技术不够强。
是做了一堆——
没有人站出来说过'我负责'的东西。"
```

---

## 热梗库（按主题分类）

### AI / 科技类
- 「不是AI太强，是你的工种太脆」
- 「AI不会取代你，会用AI的人会取代你」
- 「大模型元年：人人都在谈，没人真正懂」
- 「你还在调参数，别人已经调好了整个公司」
- 「AI最大的阻力，从来不是技术，而是人」

### 日本 / 文化观察类
- 「躬匠精神」（讽刺日本企业的道歉文化）
- 「日本的问题不是没有AI，是AI来了也不知道干嘛」
- 「日本公司很保守。不是因为他们不懂。是因为他们更怕出错。」

### 职场 / 人生类
- 「卷不动，也躺不平」
- 「选择比努力重要，但选择本身就是一种努力」

### 对比 / 反直觉类（最适合当开头/结尾）
- 「别人在用AI降本增效，你在用Excel酝酿未来」
- 「但真正的问题不在这里」

---

## 小标题规范

**规则：小标题 = ❶❷❸ + 文章句子，不含框架标记词**

❌ 坏的小标题：
- ❺ 核心卡点 —— 一个词，读者不知道要说什么
- ❸ 第一个问题 —— 框架标记词，不是文章句子

✅ 好的小标题（具体短句）：
- ❺ 写10秒，判断要5分钟
- ❸ 但这不是我要交的版本
- ❼ 它解决表达，不解决判断

---

## 存档 + 相似度检查

### Step 1: 查历史相似度（写之前先查）

```python
import json, os

HISTORY_FILE = os.path.expanduser("~/.hermes/research/articles_history.json")
NEW_THEME_KEYWORDS = ["主题词1", "主题词2"]  # ← 每次替换

history = json.load(open(HISTORY_FILE)) if os.path.exists(HISTORY_FILE) else []
print(f"历史文章共 {len(history)} 篇")

for art in history[-10:]:
    themes = set(art.get("themes", []))
    tags = set(art.get("tags", []))
    new_kw = set(NEW_THEME_KEYWORDS)
    overlap = themes & new_kw
    if overlap:
        print(f"  ⚠️  [{art['date']}] {art['title']}: 主题重叠={overlap}")

if len(history) >= 5:
    recent_themes = set()
    for art in history[-5:]:
        recent_themes.update(art.get("themes", []))
    theme_overlap = recent_themes & set(NEW_THEME_KEYWORDS)
    if len(theme_overlap) >= 2:
        print(f"\n⚠️ 近5篇主题重叠≥2，建议先和用户确认换角度再写")
    else:
        print(f"\n✅ 主题可写")
else:
    print(f"\n✅ 历史文章不足5篇，直接写")
```

**判断：近5篇主题重叠 ≥ 2 → 先和用户确认换角度**

### Step 2: 写正文

按以上指南写完正文，保存为 `~/.hermes/research/article_*.md`

### Step 3: 存档 + 相似度检查（写完立即执行）

```python
import json, os, uuid, re
from datetime import datetime

HISTORY_FILE = os.path.expanduser("~/.hermes/research/articles_history.json")
ARTICLE_DIR  = os.path.expanduser("~/.hermes/research/")
NEW_THEMES = ["主题词1", "主题词2"]  # ← 每次替换
NEW_TITLE  = "文章标题"
NEW_FILE   = "article_xxx.md"
NEW_WORDS  = 0  # 字数

new_entry = {
    "id": str(uuid.uuid4())[:8],
    "title": NEW_TITLE,
    "date": datetime.now().strftime("%Y-%m-%d"),
    "tags": [],
    "summary": "",
    "themes": NEW_THEMES,
    "word_count": NEW_WORDS,
    "file_path": NEW_FILE
}

history = []
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE) as f:
        history = json.load(f)

def extract_content(text):
    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'---', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def char_bigrams(text):
    words = text.split()
    bigrams = set()
    for i in range(len(words)-1):
        bigrams.add(f"{words[i]}_{words[i+1]}")
    return bigrams

def load_article(file_path):
    try:
        return extract_content(open(os.path.expanduser(file_path)).read())
    except:
        return ""

recent = history[-5:] if len(history) >= 5 else history
print("=== 相似度检查 ===")

for art in recent:
    art_file = art.get("file_path", "")
    if not art_file:
        continue
    prev_text = load_article(art_file)
    new_text  = extract_content(open(os.path.expanduser(NEW_FILE)).read())
    if not prev_text or not new_text:
        continue

    prev_words = set(prev_text.split())
    new_words  = set(new_text.split())
    jaccard = len(prev_words & new_words) / max(1, len(prev_words | new_words))

    prev_bg = char_bigrams(prev_text)
    new_bg  = char_bigrams(new_text)
    bg_jaccard = len(prev_bg & new_bg) / max(1, len(prev_bg | new_bg))

    theme_overlap = set(NEW_THEMES) & set(art.get("themes", []))
    flag = "⚠️" if jaccard > 0.05 or len(theme_overlap) >= 2 else ("⚡" if jaccard > 0.02 else "✅")
    print(f"  {flag} [{art['date']}] {art['title']}: 词Jaccard={jaccard:.2%} bg={bg_jaccard:.2%} 主题={theme_overlap}")

all_prev = " ".join([load_article(a.get("file_path","")) for a in recent])
if all_prev:
    all_prev_words = set(all_prev.split())
    new_words_set  = set(extract_content(open(os.path.expanduser(NEW_FILE)).read()).split())
    overall_jaccard = len(all_prev_words & new_words_set) / max(1, len(all_prev_words | new_words_set))
    print(f"\n整体词Jaccard: {overall_jaccard:.2%}")
    if overall_jaccard > 0.05:
        print("⚠️ 整体相似度偏高 → 返回正文调整角度")
    else:
        print("✅ 相似度可接受 → 进入封面流程")
else:
    print("✅ 无历史文章 → 直接进入封面流程")

history.append(new_entry)
with open(HISTORY_FILE, "w") as f:
    json.dump(history, f, ensure_ascii=False, indent=2)
print(f"✅ 已存档: {NEW_TITLE}")
```

### 判断规则

| 指标 | 阈值 | 结果 |
|---|---|---|
| 词集合 Jaccard | > 5% | ⚠️ 返回正文调整角度 |
| 词集合 Jaccard | 2–5% | ⚡ 可接受 |
| 词集合 Jaccard | < 2% | ✅ 直接通过 |
| 主题重叠 | ≥ 2 | ⚠️ 必须调整角度 |

---

## 人设一致性检查

- AI应用经验：约3年（2023年底至今），不是7年
- 不能出现"七年AI应用""多年AI落地"等超过人设的说法
- 核心洞察来自：自动驾驶时期"准确率92%但需求命中率11%"的经验
- 市场经验：自动驾驶（美国小马）+ ToB AI应用（日本）
- 人设档案是查错基准，不是正文信息来源——不在文章里主动提清华/哥大/微软/Facebook

---

## 输出

完成后告知用户：
- 正文已保存至 `~/.hermes/research/article_*.md`
- 相似度检查：通过 / 需调整角度
- 下一步：加载 `wechat-post-image` 生成封面和配图
